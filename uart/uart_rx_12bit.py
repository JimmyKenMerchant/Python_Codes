#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./uart_rx_12bit.py /dev/serial0 38400 0.01

##
# Receive 12-bit 2 Channels as Follows
# First Byte: Bit[7] Always High, Bit[6:5] Channel Number, Bit[4:0] Most Significant 5 Bits
# Second Byte: Bit[7] Always Low, Bit[6:0] Least Significant 7 Bits
##

import sys
import serial
import time
import jimmyconsole.uart as console
import signal

print (sys.version)
argv = sys.argv
print (argv[0]) # File Name

uart = serial.Serial(port = argv[1], baudrate = int(argv[2]), timeout = float(argv[3]))

# Set Keyboard Interrupt
def handle_sigint(signum, frame):
    uart.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

byte_count = 0;
while True:
    byte = uart.read(1);
    if len(byte) != 0:
        byte = int.from_bytes(byte, "little")
        if byte & 0x80: # First Byte
            channel = 0x3 & (byte >> 5)
            data_10bit = 0x03FF & (byte << 7)
            byte_count = 1
        else: # Second Byte
            if byte_count == 1:
                data_10bit |= byte
                byte_count += 1
            else:
                byte_count = 0

        if byte_count == 2:
            print("Ch:", end=" ", flush=True)
            print(channel, end=" ", flush=True)
            print("Data:", end=" ", flush=True)
            print(data_10bit, flush=True)
            byte_count = 0

