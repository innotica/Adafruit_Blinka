# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Analog in demo"""
import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.AI1)


def get_voltage(pin):
    return pin.value


while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)
