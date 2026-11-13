# Orba 1 recovery notes (12 Nov 2026)

## Where things stand
- Device: Orba 1. Bootloader mode = STM32 ROM DFU, USB ID 0483:DF11. Chip has 512 KB flash.
- Driver: WinUSB, installed with Zadig. dfu-util (bundled with the Orba app) can talk to the device.
- Flash read on 12 Nov 2026 (`orba_flash_backup.bin`):
  - 0x08000000-0x0800FFFF (64 KB): **byte-for-byte identical to official firmware v0.15.13**.
  - 0x08010000-0x0807FFFF: blank. That's NORMAL: the official 0.15.13 image only uses the first 64 KB of internal flash.
  - CORRECTION: an earlier note said the main firmware was wiped. That was wrong. The STM32 firmware is intact.
- Why the app hangs: its firmware feed (storage.googleapis.com/orba_firmware_updates/appcast_fw.xml)
  is on a closed Google Cloud billing account, so it returns 403 and the app waits forever.
- The r/orba MediaFire "Orba_Software.zip" only contains OrbaWinSetup-0.15.36.exe (identical to the
  official one) plus Orbasynth. There's no firmware in it.

## Official firmware found inside the app
The signed Orba app 0.15.36 (C:\Program Files\Artiphon\Orba\Orba.exe) has the whole 0.15.13 package
embedded in it. Copies extracted to `official_0.15.13_from_app/` (CRC-checked):
- `delorean_crc 0.15.13.hex`: STM32 image (0x08000000 64 KB + a 0x20010000 segment)
- `esp32_delorean_047ca2c3.zip`, `delorean.bin`, `bootloader.bin`, `partitions_singleapp.bin`: ESP32 (Bluetooth/audio co-processor)
- `21_X0_CY8C_Touch_A0_2988ebe.cyacd`: capacitive touch chip firmware
- `CHANGELOG_BETA.md`: Artiphon's internal changelog

## What's needed (superseded, kept for reference)
The main application image for 0x08010000. Either:
1. An official `Orba_FW_v0.15.13.zip` (or another version). Check it against `official_firmware_hashes.txt`.
2. A flash dump from a WORKING Orba 1. Have the owner put it in DFU mode (hold + while powering on),
   install the WinUSB driver with Zadig, then run:
       dfu-util -a 0 -s 0x08000000:524288 -U orba1_working_dump.bin
   This is read-only and doesn't change their Orba.

## Restoring (only once a verified image is in hand)
    dfu-util -a 0 -s 0x08010000:leave -D app_image.bin
(or write a full 512 KB dump at 0x08000000). Keep `orba_flash_backup.bin` so the current bootloader can be restored.

## Firmware reverse-engineering notes (v0.15.13, from the official app; done 12 Nov 2026)
Chip: STM32F730 (64 KB flash). The internal flash holds startup, USB, buttons and drivers. A 124 KB block
at 0x20010000 (RAM) holds the engine, including the power and battery logic.

Battery monitor: function at 0x20022230 (RAM block)
- Reads the ADC, smooths it (avg += (new-avg)/2) and converts to volts: V = avg * 0.00161133 (3.3 V / 4096 * 2 divider).
  Stored as a float at state+0x1A34 (state pointer at 0x20030788).
- Low-battery shutdown: if V < 3.695 V AND not on external power (state+0x1A3A == 0),
  a counter goes up by 3 per check. Above 30 it calls 0x200111BD, then power_down(1, 2000.0) at 0x2002CB90.
  -> On USB power the firmware ALREADY skips the low-battery shutdown, so a "USB-only" patch would change nothing.
- Charging is controlled by the firmware: set_charge_enable() at 0x08000220 drives GPIOD pin 2
  (low = charge on). It's enabled when V < 3.92 V (with a 5-minute hold-off, 300000 ms) and disabled at 4.12 V or above.
  -> If the firmware never runs, the charger may never be enabled. That fits "hours on the charger, still dead".
- External-power detect: 0x08009138 reads GPIOC pin 3 (active low). 0x20022094 combines this with another check.

Experiment, 12 Nov: loaded the RAM block via DFU (0x20010000:force) and jumped to the reset handler at 0x08000000.
Result: no LEDs and no USB enumeration, so the firmware stops before USB/LED init, or the board's power-on path is faulty.

## Boot option bytes (read 12 Nov 2026), possibly important
Option bytes on the Orba (0x1FFF0000): RDP = 0xAA (level 0, unlocked), BOOT_ADD0 = 0x0040 (-> 0x00100000 = ROM bootloader),
BOOT_ADD1 = 0x2000 (-> 0x08000000 = flash firmware).
The firmware has two routines that rewrite these:
- 0x08007EC8: sets BOOT_ADD0 = 0x0040 (ROM). Called by "jump to bootloader" (0x08007F7C), which then resets the chip.
- 0x08007F20: sets BOOT_ADD0 = 0x2000 (flash) and BOOT_ADD1 = 0x0040 (ROM).
The Orba app writes an "option_bytes.bin" with ":will-reset:force" at the end of an update.
If BOOT0 is normally LOW, the current setting makes the chip boot into the ROM bootloader on every power-on,
i.e. stuck in DFU, the classic "Orba stuck after a failed update". Not yet confirmed.
WARNING: setting both BOOT_ADD0 and BOOT_ADD1 to flash would leave no way into the bootloader without an SWD debugger.

## Final status (13 Nov 2026, ~07:15)
PROVEN
- The PC talks to the STM32 ROM bootloader (WinUSB driver via Zadig; dfu-util from the Orba app).
- Internal flash (64 KB) is byte-identical to official v0.15.13. Checked again after all experiments: 0 bytes differ.
- Option bytes are unchanged throughout: BOOT_ADD0=0x0040 (ROM), BOOT_ADD1=0x2000 (flash). Plugged in with power only, it boots to the bootloader.
- RAM writes work: proof test wrote 512 bytes to 0x20020000 and read back 512/512 identical.
NOT PROVEN
- That any code loaded via DFU ever executed. No output was ever retrieved. After every "leave", the Orba disconnected
  and never came back without a replug (which loses RAM).
- The theories in the RE notes (engine on the external SPI flash, power-latch on GPIOB15, long-press shutdown,
  stuck after an app update attempt) are inferences from disassembly, not tested.
OBSERVED
- In bootloader mode the Orba stays powered for anything from a few seconds to over 30 minutes, and once lost power
  mid-write. Next step suggested: inspect and replace the battery and check the connectors, then retest with stable power.

## tools/
- reverse-engineering/: Capstone-based helpers (need `pip install capstone`). load.py parses the Intel HEX.
  Usage: python orbadis.py <dir> "<hex>" <addr> ; func.py <dir> "<hex>" <start> <end> ; xref.py <dir> "<hex>" <addr...>
- device-scripts/: PowerShell watchers and the recovery attempt (recover.ps1). These use absolute scratch paths; edit before reuse.
- diag-stub/ and proof-test/: Keystone-assembled RAM-only test programs (need `pip install keystone-engine`).
- firmware-segments/: the two segments extracted from the official 0.15.13 HEX (0x08000000 64 KB, 0x20010000 125,792 bytes).
