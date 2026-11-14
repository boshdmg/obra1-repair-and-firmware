# Orba 1: physical repair

See also [../firmware](../firmware/README.md) for the firmware investigation.

## Symptoms
- Worked for one session, then wouldn't power on at all. No lights, even after hours on several chargers and cables.
- Only reachable in the STM32 bootloader (plus + power while plugging in). In bootloader mode it stays powered
  for anything from a few seconds to over 30 minutes, and once lost power in the middle of a write.
- The firmware on the main chip is intact (byte-identical to official v0.15.13), so the main suspect is power: battery or connections.

## Opening it
Source: Artiphon forum thread "Orba hacking knowledge base" (archived on the Wayback Machine), plus our own teardown.
1. Unplug USB.
2. Hold the top and **twist the bottom firmly clockwise**; it unscrews.
3. The base grille is held by small screws. **The screw type isn't certain:** one forum user found hex keys
   around 1.27-1.3 mm almost fitted (and stripped several screws); another reported a **Torx T6** worked.
   Use a precision set with hex 0.9/1.27/1.3/1.5 mm and Torx T5/T6/T7, test for a snug fit, press down firmly, turn slowly.
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
**where they connect to the main board (plug or solder) hasn't been checked yet.**

## Battery (photo: photos/01-battery-label.webp)
| Field | Value |
|---|---|
| Label | KNE 524048P |
| Type | Single-cell lithium-polymer pouch, 3.7 V nominal (4.2 V full) |
| Capacity | 1250 mAh, 4.625 Wh |
| Size (from the code) | ~5.2 mm thick x 40 mm wide x 48 mm long (measure to confirm) |
| Date | 23 July 2021 |
| Protection | Built-in board "PCB-362" on the side of the cell (cuts the cell off if over-discharged) |
Not visibly swollen.

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

## Option A: try to recover the original battery (cheapest)
Use a **TP4056 USB-C charger board *with* protection** (6 pads: IN+/IN-, B+/B-, OUT+/OUT-), about GBP 3:
- [Kunkune, Type-C TP4056 with battery protection (5-pack)](https://kunkune.co.uk/shop/kunkune-accessories/5x-type-c-lithium-battery-charger-module-with-battery-protection-5v-1a/)
- [SB Components, TP4056 Type-C](https://shop.sb-components.co.uk/products/lithum-battery-charger-tp4056-typec-usb)
- [38-3d, USB-C TP4056](https://38-3d.co.uk/products/usb-type-c-18650-tp4056-lithium-battery-charger-module) (check it says "with protection")

Steps:
1. Disconnect the battery from the main board.
2. Battery **red -> B+, black -> B-** (not OUT). Solder, or use crocodile clips that can't touch each other.
3. Power it with a **USB-A to USB-C cable** (many of these boards don't work with USB-C to USB-C chargers).
4. Red LED = charging, green/blue = full. Charge on a non-flammable surface and stay nearby.
   **If the battery gets warm or puffy, unplug immediately** and replace it.
5. Results:
   - Goes full, and the Orba starts once refitted: it was just flat.
   - Never goes full, or the LED keeps blinking: the battery is dead and needs replacing.
   - Charges, but the Orba still won't start: the battery's fine and the fault is elsewhere (revisit the firmware work with stable power).

## Option B: replace the battery
Requirements:
- 3.7 V single-cell LiPo **with protection circuit**
- **No bigger than 5.2 x 40 x 48 mm** (smaller is fine; ~900-1300 mAh)
- Connector matching the main-board end, **or** reuse the original plug by cutting it off with some lead and soldering it on (red to red, black to black)
- **Check polarity** before connecting: red/black positions on these plugs aren't standardised

Candidates checked (none confirmed to fit; measure the compartment first):
| Battery | Size (T x W x L) | Fits 5.2 x 40 x 48? |
|---|---|---|
| [Proto-PIC 1000 mAh (UK)](https://proto-pic.co.uk/product/lipo-battery-3-7v-1000mah-1ah) | 5.9 x 33.5 x 50.8 | No: 2.8 mm long, 0.7 mm thick |
| [PiShop 900 mAh (US)](https://www.pishop.us/product/lithium-ion-polymer-battery-3-7v-900mah/) | 6 x 30 x 48 | No: 0.8 mm thick |
| [Tinytronics LP554050 1250 mAh (NL)](https://www.tinytronics.nl/en/li-po-battery-3.7v-1250mah-jst-ph-lp554050) | 5.5 x 40 x 50 | No: slightly big, discontinued |
| [Robozar KP523450 1200 mAh](https://www.robozar.com/product/3-7v-1200mah-li-po-rechargeable-battery-kp-523450/) | 5.2 x 34 x 50 | No: 2 mm long |
Search terms for Amazon UK/eBay: `3.7V lipo 524048`, `503450`, `504045`, `523448`, `3.7V lipo 5x40x48mm`.
Never force a LiPo into a space that's too small. A phone repair shop can also source and fit an equivalent cell.

## To do
- [ ] Photograph where the battery leads connect to the main board (under the centre foam pad)
- [ ] Measure the battery compartment (length, width, depth with the case closed)
- [ ] Try Option A (TP4056)
- [ ] If needed, Option B (replacement)
