# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`analogio` - Analog input and output control
============================================
See `CircuitPython:analogio` in CircuitPython for more details.
Not supported by all boards.

* Author(s): Carter Nelson, Melissa LeBlanc-Williams
"""

import sys

from adafruit_blinka.agnostic import detector

# pylint: disable=ungrouped-imports,wrong-import-position,unused-import

if detector.board.microchip_mcp2221:
    from adafruit_blinka.microcontroller.mcp2221.analogio import AnalogIn
    from adafruit_blinka.microcontroller.mcp2221.analogio import AnalogOut
elif detector.board.greatfet_one:
    from adafruit_blinka.microcontroller.nxp_lpc4330.analogio import AnalogIn
    from adafruit_blinka.microcontroller.nxp_lpc4330.analogio import AnalogOut
elif detector.board.any_siemens_simatic_iot2000:
    from adafruit_blinka.microcontroller.am65xx.analogio import AnalogIn
    from adafruit_blinka.microcontroller.am65xx.analogio import AnalogOut
elif detector.chip.S5P4418:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.S5P6818:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.RK3308:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.RK3399:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.RK3588:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.RK3568:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.RK3566:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.IMX6ULL:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif detector.chip.STM32MP157:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif "sphinx" in sys.modules:
    pass
elif detector.board.pico_u2if:
    from adafruit_blinka.microcontroller.rp2040_u2if.analogio import (
        AnalogIn_Pico as AnalogIn,
    )
elif detector.board.feather_u2if:
    from adafruit_blinka.microcontroller.rp2040_u2if.analogio import (
        AnalogIn_Feather as AnalogIn,
    )
elif detector.board.qtpy_u2if:
    from adafruit_blinka.microcontroller.rp2040_u2if.analogio import (
        AnalogIn_QTPY as AnalogIn,
    )
elif detector.board.itsybitsy_u2if:
    from adafruit_blinka.microcontroller.rp2040_u2if.analogio import (
        AnalogIn_ItsyBitsy as AnalogIn,
    )
else:
    raise NotImplementedError("analogio not supported for this board.")
