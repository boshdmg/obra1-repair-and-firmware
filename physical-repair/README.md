# Orba 1: Physical Repair

## Symptoms
- Worked for one session, then wouldn't power on at all. No lights, even after hours on several chargers and cables.
- Only reachable in the STM32 bootloader (enabled by holding power and plus button).
- The firmware on the main chip is intact (byte-identical to official v0.15.13), so the main suspect is power: battery or connections.

## Opening it (photo: photos/01-opening.webp)
Source: Artiphon forum thread "Orba hacking knowledge base" (archived on the Wayback Machine), plus my own teardown.
1. Unplug USB.
2. Hold the top and **twist the bottom firmly clockwise**; it unscrews.
3. The base grille is held by 4 small screws. A Torx T6 screw driver is needed.
4. Layers from the bottom: grille -> speaker -> battery (on the lid) -> main board -> touch-sensor board.
   Photograph each layer and note connectors before unplugging anything.

## Main board (photo: photos/02-main-board.webp)
Label: "Main Board PCBA, (c) Artiphon Inc 2021".
| Ref | What |
|---|---|
| J3 | USB-C |
| J2 | Headphone jack |
| S1 / S2 / S3 | Power / Volume Up ("plus") / Volume Down |
| J6 | Speaker (2-pin, black twisted pair) |
| Motor | Haptic motor plug (red/blue) |
| P1 | Touch-sensor board plug |
| Silver module, top right | ESP32-SOLO-1 (Bluetooth/audio co-processor) |

No visible damage (no burn marks or bulging capacitors). The battery's red/black leads run under the centre foam pad;


## Battery (photo: photos/03-battery-label.webp)
| Field | Value |
|---|---|
| Label | KNE 524048P |
| Type | Single-cell lithium-polymer pouch, 3.7 V nominal (4.2 V full) |
| Capacity | 1250 mAh, 4.625 Wh |
| Size (from the code) | ~5.2 mm thick x 40 mm wide x 48 mm long (measure to confirm) |
| Date | 23 July 2021 |
| Protection | Built-in board "PCB-362" on the side of the cell (cuts the cell off if over-discharged) |

**Visibly swollen** (photo: photos/04-battery-back.webp): the foil on the back of the cell is clearly bulging outward. This confirms the battery is damaged and should not be charged — replace it (Option B).

The protection board is part of the battery pack: cell -> protection board -> red/black leads -> main board.
A replacement is the whole pack (cell + protection + leads).

### Voltage guide (needs a multimeter, measured at the leads)
| Reading | Meaning |
|---|---|
| 4.1-4.2 V | Full |
| 3.6-3.9 V | Normal |
| 3.0-3.5 V | Flat but healthy (the Orba shuts down below ~3.7 V) |
| 2.5-3.0 V | Over-discharged, usually recoverable |
| ~0 V at the leads | Protection board has cut the cell off; the cell may still be recoverable |
| < ~2 V directly on the cell | Likely damaged, replace |

Note from the firmware: the Orba's **charging is switched on by its firmware** (GPIOD pin 2). If the firmware can't start,
the battery may never charge inside the Orba, however long it's plugged in.

