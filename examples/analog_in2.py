#!/usr/bin/env python3

import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.AI1) # pin to get value from

"""returns the voltage in ain pin"""
def get_voltage(ain):
    adc_v = (ain.value * 1.8) / (1 << 12)
    opamp_v = 61.0 * adc_v / 11.0
    ain_v = (9.9 - opamp_v) / 0.98
    return ain_v

sam = 100 # number of samples per period
secs = 10.0 # sampling period in seconds

while True:
    vin = 0
    for i in range(sam):
        vin += get_voltage(analog_in)
        time.sleep(secs/sam)
    print(vin/sam)
