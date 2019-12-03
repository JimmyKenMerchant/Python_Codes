#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./uart_rx_bytes.py /dev/serial0 115200 0.01

import sys
import serial
import time
import jimmyconsole.uart as console

print (sys.version)
argv = sys.argv
print (argv[0]) # File Name

uart = serial.Serial(port = argv[1], baudrate = int(argv[2]), timeout = float(argv[3]))
uartconsole = console.UartConsole(uart, None)
while True:
    uartconsole.receive_bytes(True, True)
del uartconsole

