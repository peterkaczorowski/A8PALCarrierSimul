# XTAL Definitions

This document outlines the steps required to add the necessary crystal definitions to the standard MicroCap libraries.

## Instructions

### 1. Update `Standard.cmp`

Add the following component definitions to your **`Standard.cmp`** file under the `[compdef]` section:

#### Definition for KDS_035_46
```plaintext
[compdef]
Name=KDS_035_46
Definition=Macro
Shape=Crystal
Mask=4224
Used=5
memo=3.546894 MHz Quartz Crystal (ATARI XL PAL)
Label Offset=18,9,11,12
PinCnt=2
Pin="plus",a,0,0,-11,-4
Pin="minus",a,6,0,-12,-4
```

#### Definition for KDS_043_20
```plaintext
[compdef]
Name=KDS_043_20
Definition=Macro
Shape=Crystal
Mask=4224
Used=6
memo=4.433618 MHz Quartz Crystal (PAL color subcarrier)
Label Offset=18,9,11,12
PinCnt=2
Pin="plus",a,0,0,-11,-4
Pin="minus",a,6,0,-12,-4
```

### 2. Update `xtal.lib`

Add the following macros to the **`LIBRARY/xtal.lib`** file:

```plaintext
.macro KDS_035_46 XTAL(3.546894MEG,10,5K)
.macro KDS_043_20 XTAL(4.433618MEG,10,5K)
```

## Notes

- Ensure you save your changes in both files before using the updated libraries.
- The above definitions enable proper simulation of 3.546894 MHz and 4.433618 MHz quartz crystals in your MicroCap environment.


