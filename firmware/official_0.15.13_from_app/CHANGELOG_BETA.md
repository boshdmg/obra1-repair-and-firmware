# 0.15.13

## Built from:

    delorean_software: a52d3f7
	esp32_bt: 047ca2c
	audio_engine: b511fdb
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Change limiter settings on headphones to prevent clipping
- Fix issue with charging not being re-enabled for 5 minutes after USB plug in (PROD-3024)
- Fix issue with automatic power off being killed by watchdog (PROD-3024)

# 0.15.12

## Built from:

    delorean_software: 17d568d
	esp32_bt: 047ca2c
	audio_engine: b511fdb
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Add new default presets from other branch
- Minor fixes to MIDI routing and looper crashing during pad mashing (PROD-3022)

# 0.15.11

## Built from:

    delorean_software: 2d29780
	esp32_bt: 047ca2c
	audio_engine: b511fdb
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Fixed issue where battery overtemp logic could be inadvertently triggered (PROD-3017)

# 0.15.10

## Built from:

    delorean_software: 3c00a9a
	esp32_bt: 047ca2c
	audio_engine: b511fdb
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features
- Add support for X10 PCBA with PCM1748E DAC (PROD-2938)
- Add RED LED indication if overtemperature condition detected on battery (PROD-3017)

## Bug Fixes
- Fixed issue with battery charging cycling too quickly (PROD-3017)
- Increased dead battery power off voltage to higher level (PROD-3017)
- Fixed potential issue with power off logic not working in noisy conditions (PROD-3017)

# 0.15.9

## Built from:

    delorean_software: f96fc58
	esp32_bt: 047ca2c
	audio_engine: b511fdb
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Fixed issue with clipping audio engine on certain presets (PROD-3010, PROD-3009, PROD-3007)

# 0.15.8

## Built from:

    delorean_software: 6617740
	esp32_bt: 047ca2c
	audio_engine: 4defcfa
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Fixed bug where looper could crash if multiple duplicate looped notes were played simultaneously (PROD-2994)

# 0.15.7

## Built from:

    delorean_software: b61ef88
	esp32_bt: 047ca2c
	audio_engine: 4defcfa
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Fixed bug where looper would disallow all recording if a single part was full instead of the active part being full (PROD-2993)
- Fixed bug where crash could happen if looper automatically ended itself due to full memory (PROD-2996)

# 0.15.6

## Built from:

    delorean_software: 5efd2e0
	esp32_bt: 047ca2c
	audio_engine: 4defcfa
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features
- Volume increases and decreases faster (PROD-2976)
- Support for temporary mute with Prism (PROD-2971)
- Support for Prism metronome sync (PRIS-710)

## Bug Fixes
- Fixed rare bug in audio engine
- Major looper stability improvements (PROD-2616, PROD-2973)


## Notes

# 0.15.4

## Built from:

    delorean_software: 22f36ad
	esp32_bt: 047ca2c
	audio_engine: 5f444ef
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features
- Updated audio engine and improved shaker sounds
- Updated FW to automatically detect PCB revision for DAC driver

## Bug Fixes

## Notes

# 0.15.2

## Built from:

    delorean_software: 15c2a9f
	esp32_bt: 047ca2c
	audio_engine: 6af0939
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Another fix for issue where bump would never be output (PROD-2561)

## Notes


# 0.15.1

## Built from:

    delorean_software: f7ddda0
	esp32_bt: 047ca2c
	audio_engine: 6af0939
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes

## Notes
- Disables quantization by default to allow releasing of volume per part, ESP32 updater fixes
- Updated audio engine for reduced code size

# 0.15.0

## THIS VERSION HAS QUANTIZE ON BY DEFAULT

## Built from:

    delorean_software: 6f3742c
	esp32_bt: 047ca2c
	audio_engine: 5a82e20
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features
- Added volume adjustment per part by holding A + PART + volume buttons (PROD-2002)
- Added 'groove' quantize option (PROD-2566, PROD-2069)
- Added ability to manually turn haptic on for testing (PROD-2572)

## Bug Fixes

# 0.14.19

## THIS VERSION HAS QUANTIZE ON BY DEFAULT

## Built from:

    delorean_software: 7df7fe2
	esp32_bt: 047ca2c
	audio_engine: 5a82e20
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Fixed issue where CCs could be added outside the loop length and eventually lead to a crash (PROD-2562)
- Fixed issue where bump gesture wouldn't be output (PROD-2561)
- Fixed issue where quantized looper output could override newly played user input (PROD-2560)
- Fixed issue where notes would disappear with quantize and cause a crash (PROD-2511, PROD-2528)
- Fixed bug where notes could get stuck in a phantom on state and continuously stream CC's due to missed note off (PROD-2514)
- Fixed various bugs with USB and BLE MIDI where FW updates could fail, MIDI / SYSEX packets could be lost, USB CDC issuese,  and communication could fail. (PROD-2439)


# 0.14.18
## Built from:

    delorean_software: c29e6fe
	esp32_bt: 047ca2c
	audio_engine: 5a82e20
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features
- Quantization is turned on by default (constant length, snap to 1/16 notes) (PROD-2130)

## Bug Fixes
- Various bug fixes with quantization (PROD-2447, 2174)
- Various bug fixes with updating MIDI looper config (PROD-2506)
- Moving some stuff around flash/RAM for housekeeping purposes (PROD-2505)

# 0.14.17
## Built from:

    delorean_software: c0ecef3
	esp32_bt: 047ca2c
	audio_engine: 5a82e20
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features
- Add FW field to comms to allow app to turn metronome on / off (PROD-2074)

## Bug Fixes

## Notes
- Removes ability for looper semitone shift. 

# 0.14.16
## Built from:

    delorean_software: c0ecef3
	esp32_bt: 047ca2c
	audio_engine: 5a82e20
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.30

## New Features

## Bug Fixes
- Fix bug where looper fastforward algorithm could leave looper in bad state and cause crash (PROD-2411)
- Fix issue where a play immediately after a pause could cause zero duration notes to be recorded in looper (PROD-2412)
- Fix various MIDI barfing issues that could lead to buffer overflow if tick changed to dramatically (PROD-2441)
- Fixed issue where disabling the haptic motor during a haptic event could cause the haptic to get stuck on (PROD-2442)
- Fixed issue where BLE messages could build up delay if too many messages were sent during one connection interval (PROD-2449)
- Fixed issue where sometimes malformed packets could be sent to ESP32 and cause the ESP32 to crash (PROD-2342)


# 0.14.15
## Built from:

    delorean_software: d8a5fdb
	esp32_bt: 0a24e926
	audio_engine: 5a82e20
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

## Bug Fixes
- Fix bug where pitch bend / aftertouch recorded as global CCs could cause crash (PROD-2397)

## Notes
- This build is based on 0.14.14 and has no key changing support. 

# 0.14.13
## Built from:

    delorean_software: bb387a4
	esp32_bt: 0a24e926
	audio_engine: 5a82e20
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Added ability to change Orba's key by sliding on the OCT pad. (PROD-2129)
- Updated audio engine to latest version. 

# Bug Fixes


# 0.14.12
## Built from:

    delorean_software: 69b532a
	esp32_bt: 0a24e926
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

# Bug Fixes
- Major fixes to BLE firmware that address instability with Android devices. Connection should be significantly improved on Android devices. Minor improvements in iOS. (PROD-2219, PROD-2214, PROD-2268)
- Fix issue where channel pressure wasn't sent via BLE MIDI (PROD-2151)
- Fix issue where turning off Orba sounds when notes were playing could cause stuck notes (PROD-2210)
- Fix issues where exiting overdub when notes that crossed the loop boundary were playing could cause looper corruption (PROD-2274, PROD-2355, PROD-2367)

# 0.14.11
## Built from:

    delorean_software: d35570d
	esp32_bt: 93c49aae
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

# Bug Fixes
- Fixes some issues introduced with refactoring for quantization. 

# 0.14.10
## Built from:

    delorean_software: d35570d
	esp32_bt: 93c49aae
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Change articomm start bytes to match artiphon MIDI manufacturer ID
- Add support for event source list queries
- Add support for tuning broadcast messages


# 0.14.9
## Built from:

    delorean_software: 648d83b
	esp32_bt: 32e761fd
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Add 'single port MIDI' mode to allow USB MIDI on Android (PROD-2126)
- Add USB descriptors for Android MIDI mode (PROD-2043)

## Bug Fixes


# 0.14.8
## Built from:

    delorean_software: e2d0233
	esp32_bt: 32e761fd
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

## Bug Fixes
- Fixed issue where you couldn't return to original octave after changing it (PROD-2121)

# 0.14.7
## Built from:

    delorean_software: 4004d9c
	esp32_bt: 32e761fd
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Added ability to turn on / off metronome tick via long press on BPM button (PROD-1725, PROD-1081)

## Bug Fixes
- Fixed issue where Orba would lose time when changing modes with looper playing (PROD-2112)
- Fixed issue where held note wouldn't get recorded (PROD-2109)
- Fixed issue where Orba could crash if multiple notes were played at the same time (PROD-2108)
- Fixed issue where holding A + any pad would erase song instead of A + REC (PROD-2102)

# 0.14.6
## Built from:

    delorean_software: 547d528
	esp32_bt: 32e761fd
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Added ability to turn haptic engine on / off (PROD-2085)

## Bug Fixes
- Fixed issue where changing tempo from app could cause a crash (PROD-2052)
- Fixed issue where Orba could crash if a single note was held for the loop length limit (PROD-2047)
- Fixed issue where loading presets in overdub could cause a crash (PROD-2016)
- Fixed issue where CCs could get lost for notes that crossed the loop restart boundary (PROD-1955)
- Fixed issue where Boomy Booms bass preset could sound scratchy (PROD-1904)
- Fixed various issues with beeping / glitching during preset loading (PROD-1881, PROD-1758)


# 0.14.4
## Built from:

    delorean_software: 48f2997
	esp32_bt: 32e761fd
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

## Bug Fixes
- Fix issue where automatic power down would happen after 1 minute instead of 10 minutes. (PROD-2045) 

# 0.14.3
## Built from:

    delorean_software: b5845cc
	esp32_bt: 32e761fd
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Add automatic power down after 10 minutes of inactivity (PROD-675)

## Bug Fixes
- Fix issue where 2 loops could be playing back the same notes (PROD-2040)
- Fix potential crash when recording a loop with a single note that needed moving to 'end' (PROD-2037)
- Fix crash if lots of CCs were being thickened simultaneously (PROD-2035)
- Fix issue where crash was possible if playing lots of notes and switching modes (PROD-2027)

# 0.14.2
## Built from:

    delorean_software: 11df6ff
	esp32_bt: 32e761fd
	audio_engine: bd3a48c
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Updated audio engine to improve code size

## Bug Fixes
- Fix issue where rotary phoning during overdub could cause crash (PROD-2017)
- Fix issue where loading presets in overdub could cause crash (PROD-2016)
- Fix issue where changing presets in overdub could cause crash (PROD-1894)

# 0.14.1
## Built from:

    delorean_software: ae0efbb
	esp32_bt: 32e761fd
	audio_engine: 314994a
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

## Bug Fixes
- Fix issue where notes could get stuck when pausing a loop from play (PROD-2009)
- Fix issues where rapidly played notes could cause a crash in overdub (PROD-2000, PROD-1999)
- Fix issue where holding a note longer than 8 bars could cause crash (PROD-1993, PROD-1992)
- Fix issue where A button press could delete note on first beat (PROD-1990)
- Fix issue where notes could get stuck when deleting a song from record / overdub (PROD-1987, PROD-1900, PROD-1898)

# 0.14.0
## Built from:

    delorean_software: 8ca9ff7
	esp32_bt: 32e761fd
	audio_engine: 314994a
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Added ability for MIDI looper to handle more notes than available playback heads (PROD-1960)
- Added feature where loops are 'intelligently' ended and notes at the end of the first bar can move to the end of the loop (PROD-1864)
- Added ability for looper to start playing ongoing notes when entering overdub, and be audible within a certain time period (PROD-1804, PROD-1803)
- Loop now ends when last note is played, not when A button is pressed (PROD-1501)

## Bug Fixes
- Fixed issue where speaker could distort at high volume levels (PROD-1989)
- Fixed issues where Orba could crash if notes were held longer than the loop length (PROD-1981, PROD-1970, PROD-1966)
- Fixed issue where stuck notes could happen if the A button was pressed with ongoing notes (PROD-1980)
- Fixed issue where changing instruments in overdub could cause a crash (PROD-1962)
- Fixed issue where MIDI looper didn't use channels properly (PROD-1959)
- Fixed issue where notes shifted if ending overdub under certain conditions (PROD-1949)
- Fixed issue where All Notes Off message wasn't sent on MIDI Channel 16 (PROD-1942)
- Fixed issue where All Notes Off messages would be continually sent during preset / song loads (PROD-1928)
- Fixed issue with overdub loop not being saved if you left overdub before the loop was played back (PROD-1905)
- Fixed issue where CCs would be erased if overdubbing and the associated note wasn't active (PROD-1753)


# 0.13.21
## Built from:

    delorean_software: 6e9ceaf
	esp32_bt: 32e761fd
	audio_engine: 00756de
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

## Bug Fixes
- Fixed issue where All Notes Off MIDI messages were continually sent during preset / song load (PROD-1928)
- Fixed issue where note off message would happen between 0-2s after a note on if Orba's speaker was disabled (PROD-1935, PROD-1926, PROD-1902)
- Fixed some audio engine issues that could cause distortion or scratchy bass sounds (PROD-1904, PROD-1872)
- Fixed issue where switching modes before recording a song could cause a long delay on the metronome tick (PROD-1897)
- Fixed issues where switching modes during record ebfore recording a song could cause a crash (PROD-1892, PROD-1882)


# 0.13.20
## Built from:

    delorean_software: 0ce74b1
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Add support for alternate IMU part (PROD-1906)

## Bug Fixes


# 0.13.19
## Built from:

    delorean_software: 0a6d1d6
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features

## Bug Fixes
- Fix issue introduced in 0.13.18 where tap for BPM was largely unresponsive (PROD-1889)
- Further fixes where loop could restart one bar in when closing a loop (PROD-1885)


# 0.13.18
## Built from:

    delorean_software: dca2aef
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.10

## New Features
- Disable A button when wedge is pressed to prevent accidental menu mode activations (PROD-1877)
- Remove debounce delay from A button to make ending a loop on time easier (PROD-1876)
- Limit max loop length to 8 bars (PROD-1405)

## Bug Fixes
- Fixed issue where loop could restart one bar in when closing a loop (PROD-1885)
- Fixed crash when recording long loops (PROD-1870)
- Fixed issue where notes would get stuck on if they were held during an octave shift (PROD-1861)
- Improved USB MIDI stability by fixing various issues (PROD-1711, PROD-1663, PROD-1417, PROD-1398, PROD-1034)
- Improved USB Audio stability (PROD-1151)

# 0.13.17
## Built from:

    delorean_software: ae662dd
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.2

## New Features

## Bug Fixes
- Fixed issue where notes could get stuck during looper playback (PROD-1762, PROD-1715)
- Fixed issue where notes could get stuck if they were held longer than the loop length (PROD-1754)
- Fixed issue where it was possible to have loop playback start one bar in when switching from record to overdub (PROD-1739)

# 0.13.16
## Built from:

    delorean_software: 8a0a468
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.2

## New Features
- Changed default looper mode to allow up to 1 bar of silence at start of loop, first notes played back as recorded on time grid rather than snapped to start of loop. (PROD-1836, 1832, 1793, 1796)

## Bug Fixes
- Fixed issue in looper where a note could be missed during the first loop of playback (PROD-1807)
- Fixed issue where it was possible to enter overdubbing when looper was full and cause a crash (PROD-1790)
- Fixed issue with large packet sizes on bluetooth (PROD-1781)
- Fixed issue where Orba could crash when deleting a song (PROD-1775)
- Fixed issue where Orba could crash when overdubbing overlapping notes (PROD-1760)
- Fixed audio distortion when overdubbing lots of notes on all parts (PROD-1741, 1736)


# 0.13.15
## Built from:

    delorean_software: 3268269
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.2

## New Features

## Bug Fixes
* Fix issue where leaky channel assignments could cause looper crash (PROD-1771)
* Fixed issue where looper fastforward algorithm could overrun end of looper data and cause crash (PROD-1766)
* Fixed various issues where sliding across menu and mode buttons simultaneously could cause crash (PROD-1765, 1763, 1737, 1706, 1696, 1692)
* Fixed issue where drum LED would be red when initially recording a loop (PROD-1759)

# 0.13.14
## Built from:

    delorean_software: 6d6a072 
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.0

## New Features
* Added support for minor chords (PROD-1699, PROD-1698)

## Bug Fixes
* REMOVED FROM 0.13.13:::: Fixed issue where starting record of a loop just before the '1' beat would result in resuming playback midway through the song (PROD-1702)
* REMOVED FROM 0.13.13:::: Fixed issue where the UI lock could become unlocked and result in buzzing during preset / song loading (PROD-1669)
* Fixed issue where CC and aftertouch messages were played per note instead of per channel (PROD-1757)


# 0.13.13
## Built from:

    delorean_software: 077bccf
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.0

## New Features
* Added FW capability to change key of loops in Orba (requires app compatibility) (PROD-1580)

## Bug Fixes
* Fixed issue where looper wouldn't record channel pressure (PROD-1712)
* Fixed issue where starting record of a loop just before the '1' beat would result in resuming playback midway through the song (PROD-1702)
* Fixed issue where long transfer times over BLE MIDI could cause the UI to become unlocked (PROD-1710)
* Fixed issue where turning off Orba sounds while the looper was playing would cause stuck notes. (PROD-1670)
* Fixed issue where the UI lock could become unlocked and result in buzzing during preset / song loading (PROD-1669)


# 0.13.12
## Built from:

    delorean_software: 8ff3d8b
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.14.0

## New Features
* User pitchbend scale is now persistent across power cycles
* Chords now respond to major / minor changes from app. 


## Bug Fixes
* Fixed issue where battery charge blink would never indicate full battery (PROD-1694)
* Fixed issue where MIDI notes > 127 could be played with enough octave shifting (PROD-1684)
* Fixed issue where overdubbing on chords could cause easy crash (PROD-1664)

# 0.13.11
## Built from:

    delorean_software: 6264c98
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.13.0

## New Features
* Playback no longer stops when clearing loop (PROD-1569)
* Note off messages are always sent over BLE MIDI (PROD-1545)


## Bug Fixes
* Fixed possible crash if playing lots of notes at once (PROD-1656)
* Fixed issue with loading songs above a certain length (PROD-1640)
* Fixed issue where full low pitch bend (and other bezier curves) would be interpreted as full high (PROD-1636)
* Fixed issues where chunks of loops could go missing (PROD-1635, 1525, 1414, 1397, 1296)
* Fixed issue where pausing Orba when nothing has been recorded wouldn't restart record correctly (PROD-1634)
* Fixed issue with bulk transfer size being too large for BLE interface (PROD-1622)
* Fixed issues with CC's not being recorded properly after loop / song erase (PROD-1561, PROD-1560)

# 0.13.10
## Built from:

    delorean_software: c71f6a9
	esp32_bt: 32e761fd
	audio_engine: 7c115e0
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.11.0

## New Features
* Updated loop recording ending logic to start playing loop from current spot if loop exceeds bar length by less than the bar end grace period (PROD-1592)
* Audio engine back end updates

## Bug Fixes
* Fixed issue where stuck notes were possible if pads were played during flash writes (PROD-1617)
* Minor BT fixes (PROD-1595)
* Fixed an issue where overdubbed notes longer than the loop length could get stuck on (PROD-1574)
* Fixed issues where notes could get stuck on erasing a loop / song while in record / overdub (PROD-1571)
* Fixed an issue where Orba would freeze if opening Logic (or sending any sysex messages via USB) (PROD-1526)

# 0.13.9
## Built from:

    delorean_software: 1597bbe
	esp32_bt: 32e761fd
	audio_engine: d899d01
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.11.0

## New Features

## Bug Fixes
* Looper bug fixes (PROD-1581, 1582, 1585, 1415)


# 0.13.8
## Built from:

    delorean_software: ac9e564
	esp32_bt: 32e761fd
	audio_engine: d899d01
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.11.0

## New Features

## Bug Fixes
* Fixed issue where switching to lead wouldn't send a MIDI program change (PROD-1572)
* Fixed issue where saving to flash was broken, causing preset loading, song saving, etc. to be broken (PROD-1568)
* Fixed issue where sliding around the pads more than once during a single menu entry would cause a crash (PROD-1566)
* Minor amounts of work on CC issues recording after loop erase, but it's not finished yet (PROD-1561, PROD-1560)



# 0.13.7
## Built from:

    delorean_software: 31626ef
	esp32_bt: 32e761fd
	audio_engine: d899d01
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.11.0

## New Features
* Added ability to store song name on Orba (PROD-1551)
* Added abilty for app to detect changes to looper data (PROD-1546)
* Changed A button to switch from record to overdub instead of to next part when recording first song (PROD-1505)
* Changed menu entrance to short white flash instead of constant blinking (PROD-1504)
* Changed deleting a loop to go to stop instead of back to record (PROD-1503)
* Added automatic song saving and loading on power down (persistent songs). (PROD-1502, PROD-1523, PROD-1524)
* Enabled metronome tick whenever record is active (PROD-1480)
* Turned down metronome volume by ~4dB (PROD-1479)
* Added root notes and scale to pattern data (PROD-1477)
* Added song root note and scale to Orba metadata (PROD-1420)
* Added delete song feature via A+REC for 4s and A+REC+SHAKE (PROD-1307, PROD-1234)



## Bug Fixes
* Fixed issues where erasing loops and songs could cause stuck notes (PROD-1559, PROD-1541, PROD-1529)
* Fixed issues where bad commands from app could crash looper (PROD-1532)
* Fixed issue where tilting Orba to ~90deg and pushing A button erased loops without a shake to erase (PROD-1451)
* Fixed some issues with BLE MIDI (PROD-1498)
* Fixed issues where notes would get cut off when recording a new part in a song and notes crossed the loop restart boundary (PROD-1412, PROD-1411, PROD-1406)


# 0.13.6
## Built from:

    delorean_software: fa4025f
	esp32_bt: a90f493
	audio_engine: 0065094
	capsense: 2988ebe

## Compatibility

    Orba PVT units
	Oba App >= 0.10.0

## New Features
* Added ability to export bezier curve data


## Bug Fixes
* Fixed issue where note off messages would be sent multiple times when changing synth parts (PROD-1478)
* Fixed issue where loading a preset via BLE MIDI would take ~30s (PROD-1469, PROD-1467, PROD-1446, PROD-1445, PROD-1436, PROD-1176)
* Fixed issue where A button would not work on some units (PROD-1464)
* Fixed issue where using the UI lock would cause preset loading to fail (PROD-1452)

# 0.13.5
## Built from:

    delorean_software: 1bc08ad
	esp32_bt: 96c96ab7
	audio_engine: 1301195
	capsense: 415d099

## Compatibility

    Orba PVT units
	Oba App >= 0.8.0

## New Features
* Updated audio engine shaker voice
* Added ability for app to soft reset Orba (PROD-1395)
* Added support for exporting modifier data


## Bug Fixes
* Fixed issue where tapping tempo would default to lowest tempo on first tap (PROD-1401)

# 0.13.4
## Built from:

    delorean_software: 410eb43
	esp32_bt: 96c96ab7
	audio_engine: 18ba3f2
	capsense: 415d099

## Compatibility

    Orba PVT units
	Oba App >= 0.8.0

## New Features
* Updated default chord modifier (PROD-1366)


## Bug Fixes
* Fixed issue where streaming USB audio during FW updating process could cause ESP32 FW update to fail

# 0.13.3
## Built from:

    delorean_software: 12447cd
	esp32_bt: 96c96ab7
	audio_engine: 18ba3f2
	capsense: 415d099

## Compatibility

    Orba PVT units
	Oba App >= 0.8.0

## New Features
* Updated default chord modifier (PROD-1366)


## Bug Fixes
* Fixed issue where pitch bend would report incorrect range at boot (PROD-1391)
* Fixed issue where shake to erase could be inadvertently triggered, erasing loops (PROD-1388, PROD-1387)
* Fixed issue where global CCs weren't cleared on a loop erase (PROD-1378)
* Fixed issue where global CCs would decay over time, causing loop events to be erased (PROD-1374, PROD-1340, PROD-1296)
* Fixed issue where press gesture scale was incorrect (PROD-1364)
* Fixed issue where shake to erase would cause notes to remain silent while in overdub (PROD-1361)
* Fixed bugs in audio engine waveguide calculations


# 0.13.2
## Built from:

    delorean_software: 1366c5f
	esp32_bt: 96c96ab7
	audio_engine: ca1907c

## Compatibility

    Orba PVT units
	Oba App >= 0.8.0

## New Features
* Add ability to erase loops while in record mode by shake or long press on menu + rec button (PROD-1307)
* Updated audio engine to reduce quantization effects


## Bug Fixes
* Fixed issue where global CCs were not recorded during overdubbing (PROD-1328)
* Fixed issue where external MIDI notes were sent in the wrong order if a looped note was cut off in overdub (PROD-1331)
* Fixed a memory leak that could cause the looper to crash if more than 4 notes were playing simultaneously (PROD-1337)
* Fixed issue with CC thinner channel assignments that could crash looper (PROD-1338)
* Fixed issue that almost guaranteed a looper crash if overdubbing and you run out of looper memory (PROD-1339, PROD-1314)
* Fixed issue where deleting a playing loop could cause stuck notes (PROD-1273)

# 0.13.1
## Built from:

    delorean_software: c838e78
	esp32_bt: 96c96ab7
	audio_engine: 91568f5

## Compatibility

    Orba PVT units
	Oba App >= 0.6.4

## New Features
* Added ability for app to perform factory reset on Orba. 


## Bug Fixes
* Fixed issue where tapping a tempo that was too fast could cause a really slow tempo to be recorded (PROD-1247)
* Fixed some issues where overrunning the loop length could crash Orba (PROD-1250)
* Fixed some issues where changing parts while overdubbing could crash Orba (PROD-1254)
* Added UI lock to allow app to silence Orba while loading presets to prevent beeping  (PROD-1260)
* Fixed issue where Orba could freeze while updating capsense firmware (PROD-1271)
* Fixed issue where Orba could crash if the play surface was extensively palmed (PROD-1274)
* Fixed issue where looper would crash if overdubbing cut off a note that had pitch bends (PROD-1275)
* Fixed issue where looper would crash if source loop had MIDI channels recorded that were > 5 (PROD-1276)
* Fixed issue where overrunning loop length could corrupt other loops and potentially crash Orba (PROD-1285)
* Fixed issue where timestamps were not correctly calculated for CC events resulting in loop shifting in time  (PROD-1286)
* Fixed issue where bezier curve values were calculated to be zero if the input value was less than zero (PROD-1294)

# 0.13.0
## Built from:

    delorean_software: d8e7990
	esp32_bt: 96c96ab7
	audio_engine: 91568f5

## Compatibility

    Orba PVT units
	Oba App >= 0.6.4

## New Features
* Updated audio engine with headphone limiter gain
* Removed drum MIDI File Processor modifier
* Reduced pitch bend range to 1/12 semitone
* Updated factory presets to v11
* Updated loop erase by holding record to require 2s instead of 3s
* Updated looper to kick Orba out of record mode if looper is out of memory instead of crashing


## Bug Fixes
* Improved issue where Orba would crash if you overrun loop length (some strange behaviour still exists)
* Fix issue where skipping too many MIDI ticks (such as changing parts) would cause Orba to crash
* Fixed issue where looper could crash if overdubbing a note on before a CC
* Fixed various crashing bugs related to menu operations while in overdub
* Fixed issue where looper would play back all loop parts on currently active channel when in CPPOP mode
* Fixed issue where internal note trackers were not cleared if Orba was in CPPOP mode, leading to 'dead' pads in some modes, typically when palming pads

# 0.12.10
## Built from:

    delorean_software: 4a29b61
	esp32_bt: 96c96ab7
	audio_engine: 2dc17fa

## Compatibility

    Orba PVT units
	Oba App >= 0.6.1

## New Features
* Changed record to 'stop' if record is pressed while recording and no song is recorded. 
* Reset to factory defaults upon firmware update
* Updated audio engine


## Bug Fixes
* Fixed issue where Orba would crash if you slid from A button to Drum pad
* Fixed issue where orba would crash if you slid from A button to chord pad
* Updates to modifier chain / loading logic to allow loading presets with no modifiers
* Updated looper to prevent crashes during mode changes while in record / overdub
* Updates to bezier comms to talk to app. 

# 0.12.8
## Built from:

    delorean_software: 179975e
	esp32_bt: 96c96ab7
	audio_engine: ac9deea

## Compatibility

    Orba PVT units
	Oba App >= 0.6.1

## New Features
* Updated audio engine

## Bug Fixes
* Fixed issue where it is possible to get stuck chords if 2 chord note offs happen really close together
* Fixed issue where MIDI File processor could use patterns for the incorrect synth part
* Fixed issue where external MIDI messages could use up all available MPE channels and cause a crash


# 0.12.7
## Built from:

    delorean_software: 687d02e
	esp32_bt: 96c96ab7
	audio_engine: 93d2408

## Compatibility

    Orba PVT units
	Oba App >= 0.6.1

## New Features
* Updated default synth patches to 0-9
* Added watchdog so that crashes will result in orba restarting automatically. 

## Bug Fixes
* Fixed issue where looper would crash when switching loops while overdubbing
* Fixed issue where Orba would crash on a full palm press in drum mode
* Fixed issue where Orba would power off if battery is dead but you are plugged in
* Fixed issue where looper would only play first note in a loop
* Fixed issue where user played notes could not be assigned to MPE channels > 8 which would cause a crash
* Fixed audio engine issue where CCs were not registered correctly if no noted were playing
* Fixed issue with iOS / Android connectivity on ESP32 module


# 0.12.3
## Built from:

    delorean_software: eb6a2f2
	esp32_bt: 96c96ab7
	audio_engine: 230c10f

## Compatibility

    Orba PVT units
	Oba App >= 0.6.1

## New Features
* Default pitch bend range set to 2 from 48
* Bezier curves are now symmetric about 0
* Orba sound is defaulted to 'on' when connected via USB
* Menu mode now displays green when UI is detected to indicate no more UI possible
* Updated audioengine to release 1.0

## Bug Fixes

* Fixed issue where looper events could 'walk' though time if left in overdub for long periods, sometimes causing crashes. 
* Fixed issues when connecting to android devices via BT
* Fix major issue sysex messages would not be transmitted by ESP32 to STM32 in many cases

# 0.12.1
## Built from:

    delorean_software: 492ae71
	esp32_bt: fb5a0a24
	audio_engine: 9965711

## Compatibility

    Orba PVT units
	Oba App >= 0.6.1

## New Features
* Added MIDI file processor to drums part
* Added new factory presets
* MIDI looper can now record more events!
* Lots of back end work for looper / pattern stuff

## Bug Fixes

* Lots of back end looper improvements

# 0.11.8
## Built from:

    delorean_software: 6c20c16
	esp32_bt: fb5a0a24

## Compatibility

    Orba PVT units

## New Features
* Enabled pitch bend on looper recording
* Updated presets to factory default 0.2

## Bug Fixes

* Fixed looper crash bug described in PROD-1131
* Back end modification to MFP to be per-part
* Back end modification for bezier curves to be per-part


# 0.11.6
## Built from:

    delorean_software: 5797dae
	esp32_bt: fb5a0a24

## Compatibility

    Orba PVT units


## New Features
* Enabled communication over Bluetooth + app
* Pitch bend smoothed out

## Bug Fixes

* Back end updates to pattern modifier (MFP) 
* Mutexes added for preset loading
* Many looper stability improvements
* Volume range tweaked
* Fixed issue with BLE MIDI latency when sending lots of CCs

# 0.11.4
## Built from:

    delorean_software: 5797dae

## Compatibility

    Orba PVT units


## New Features

## Bug Fixes

* Fix issues where global CCs wouldn't be output
* Fix buzz during mode switch
* Fix pitch bend jumpiness when transitioning out of deadband
* Cut off notes in chord properly

## Known Issues/Bugs

* Looper does not record aftertouch or pitch bend messages

# 0.11.3
## Built from:

    delorean_software: 5797dae

## Compatibility

    Orba PVT units


## New Features

## Bug Fixes

* Fix issues where global CCs wouldn't be output
* Fix buzz during mode switch
* Fix pitch bend jumpiness when transitioning out of deadband
* Cut off notes in chord properly

## Known Issues/Bugs

* Looper does not record aftertouch or pitch bend messages

