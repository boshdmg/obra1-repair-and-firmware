# Orba 1: Firmware Reference

## Hardware overview

| Chip | Role | Notes |
|---|---|---|
| STM32F730R8 | Main MCU | 64 KB internal flash, 256 KB RAM. Runs startup, USB, buttons, power management. |
| ESP32-SOLO-1 | Bluetooth / audio co-processor | Silver module on the main board (top right). |
| CY8C (Cypress) | Capacitive touch | Separate touch-sensor board connected via P1. |

---

## Firmware files (v0.15.13)

The official 0.15.13 firmware is embedded inside the signed Orba app (`Orba.exe`). The binary firmware files are Artiphon's proprietary software and are **not distributed in this repo** incase it breaches copyright? The table below documents what exists and where to find it.

To obtain the files yourself: install the Orba app (v0.15.36) and extract them from the executable — they are embedded as named resources.

| File | Chip | Description | In repo? |
|---|---|---|---|
| `delorean_crc 0.15.13.hex` | STM32 | Main MCU image. Two segments: 64 KB at `0x08000000` (flash) and 124 KB at `0x20010000` (RAM). | No — copyright |
| `delorean.bin` | STM32 | Same image as the HEX, raw binary. | No — copyright |
| `esp32_delorean_047ca2c3.zip` | ESP32 | Bluetooth/audio firmware bundle. | No — copyright |
| `bootloader.bin` | ESP32 | ESP32 bootloader. | No — copyright |
| `partitions_singleapp.bin` | ESP32 | ESP32 partition table. | No — copyright |
| `21_X0_CY8C_Touch_A0_2988ebe.cyacd` | CY8C | Capacitive touch chip firmware. | No — copyright |
| `CHANGELOG_BETA.md` | — | Artiphon's internal changelog, included for reference. | Yes |

The firmware update feed (`https://storage.googleapis.com/orba_firmware_updates/appcast_fw.xml`) is no longer served (closed billing account — returns 403). An archived copy is at `appcast_fw.xml`.

---

## What reverse engineering found (v0.15.13 STM32 image)

### Memory layout
The STM32 image has two segments:
- **`0x08000000` (64 KB, internal flash):** startup code, USB DFU handler, GPIO drivers, button handling, option-byte routines.
- **`0x20010000` (124 KB, RAM):** the main engine — power management, battery monitor, charging logic, audio/MIDI processing. Loaded by the bootloader at startup.

### Battery monitor
Function at `0x20022230` (RAM segment):
- Reads the ADC and smooths it: `avg += (new - avg) / 2`
- Converts to volts: `V = avg × 0.00161133` (3.3 V / 4096, × 2 resistor divider)
- Stores the result as a float at `state+0x1A34` (state pointer at `0x20030788`)

### Low-battery shutdown
- If `V < 3.695 V` AND not on external power (`state+0x1A3A == 0`), a counter increments by 3 per check.
- Above 30, calls `0x200111BD`, then `power_down(1, 2000.0)` at `0x2002CB90`.
- On USB power the firmware already skips the low-battery shutdown — no patch needed for that path.

### Charging control
- `set_charge_enable()` at `0x08000220` drives **GPIOD pin 2** (low = charge on).
- Charging is enabled when `V < 3.92 V` (with a 5-minute hold-off, 300,000 ms) and disabled at `4.12 V` or above.
- **If the firmware never runs, charging is never enabled.** This explains why an Orba with a flat battery may not charge no matter how long it is left on USB.

### External power detection
- `0x08009138` reads **GPIOC pin 3** (active low).
- `0x20022094` combines this with a secondary check.

### Boot option bytes
Read from `0x1FFF0000`:

| Field | Value | Meaning |
|---|---|---|
| RDP | `0xAA` | Level 0 — read protection off, flash readable via SWD/DFU |
| BOOT_ADD0 | `0x0040` | → `0x00100000` = ROM bootloader |
| BOOT_ADD1 | `0x2000` | → `0x08000000` = internal flash |

The firmware contains two routines that rewrite these bytes:
- `0x08007EC8`: sets `BOOT_ADD0 = 0x0040` (ROM). Called by "jump to bootloader" (`0x08007F7C`), then resets.
- `0x08007F20`: sets `BOOT_ADD0 = 0x2000` (flash) and `BOOT_ADD1 = 0x0040` (ROM).

The Orba app writes an `option_bytes.bin` with `:will-reset:force` at the end of a firmware update. If `BOOT0` is permanently LOW, the current settings cause the chip to boot into the ROM bootloader on every power-on — the classic "Orba stuck in DFU after a failed update" symptom.

> **Warning:** setting both `BOOT_ADD0` and `BOOT_ADD1` to flash would leave no way back into the bootloader without an SWD debugger.

---

## Folder contents

| Path | Contents |
|---|---|
| `device-backup/` | Flash dump and option bytes read from one device (see log.md). |
| `official_0.15.13_from_app/` | Official firmware extracted from Artiphon's signed Orba app 0.15.36. |
| `official_firmware_hashes.txt` | SHA-256 / MD5 of every known official Orba 1 firmware zip. |
| `appcast_fw.xml` | Archived firmware update feed. |
| `tools/reverse-engineering/` | Capstone-based disassembly helpers. Requires `pip install capstone`. |
| `tools/device-scripts/` | PowerShell scripts for talking to the device via DFU. Edit paths before reuse. |
| `tools/diag-stub/` | RAM-only diagnostic stub (Keystone-assembled). Requires `pip install keystone-engine`. |
| `tools/proof-test/` | RAM write/read proof test. |
| `tools/firmware-segments/` | The two segments extracted from the official 0.15.13 HEX. |

### RE tool usage
```
python orbadis.py <dir> "<hex>" <addr>          # disassemble at address
python func.py    <dir> "<hex>" <start> <end>   # disassemble a function range
python xref.py    <dir> "<hex>" <addr...>       # find cross-references
```
