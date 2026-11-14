# Artiphon Orba 1: repair and firmware

Notes from trying to revive an Artiphon Orba 1 that stopped powering on, after Artiphon shut down
and its update servers went offline.

| Folder | What's in it |
|---|---|
| [physical-repair/](physical-repair/README.md) | Teardown, main-board map, battery specs (KNE 524048P, 3.7 V 1250 mAh), recovery and replacement options, photos |
| [firmware/](firmware/README.md) | Flash and option-byte backup, official v0.15.13 firmware recovered from the Orba app, reverse-engineering notes, tools and test programs |

## Current status (14 Nov 2026)
- **Firmware:** the main chip's firmware is intact (byte-identical to official v0.15.13). No custom code was ever
  shown to run, and nothing permanent on the device was changed.
- **Hardware:** the Orba is open. The battery (made July 2021) isn't visibly swollen. Power behaviour in bootloader mode
  is unstable, so the next step is charging the battery externally (TP4056), or replacing it.
