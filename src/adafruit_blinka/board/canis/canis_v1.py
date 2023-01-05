# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the Canis Board V1."""
# Enable I2C0, UART1, and SPI by adding the following lines to /boot/armbianEnv.txt
#    overlays=usbhost2 usbhost3 spi-spidev uart1 i2c0
#    param_spidev_spi_bus=0

from adafruit_blinka.microcontroller.samsung.smart4418 import pin

# Wiegand
W0 = pin.GPIO_A3
W1 = pin.GPIO_A2
# Tamper
T  = pin.GPIO_A4
# Digital inputs
I1 = pin.GPIO_A9
I2 = pin.GPIO_A8
I3 = pin.GPIO_A7
I4 = pin.GPIO_A6
I5 = pin.GPIO_A5
# Analog inputs
AI1 = pin.ADC_IN1
AI2 = pin.ADC_IN3
AI3 = pin.ADC_IN4
AI4 = pin.ADC_IN5
AI5 = pin.ADC_IN6
# Relay outputs
K1 = pin.GPIO_A20
K2 = pin.GPIO_A19
K3 = pin.GPIO_A18
K4 = pin.GPIO_A17
K5 = pin.GPIO_A16
K6 = pin.GPIO_A15
# Menu Display Buttons
SW2 = pin.GPIO_A27
SW4 = pin.GPIO_A26
SW5 = pin.GPIO_A24
# I2C to display
SC = pin.GPIO_D6
SD = pin.GPIO_D7
# Serial UART
TX0 = pin.GPIO_D18
RX0 = pin.GPIO_D14

TX1 = pin.GPIO_D19
RX1 = pin.GPIO_D15

TX2 = pin.GPIO_D20
RX2 = pin.GPIO_D16

TX3 = pin.GPIO_D21
RX3 = pin.GPIO_D17