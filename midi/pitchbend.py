#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./pitchbend.py -s /dev/serial0 -b 115200 -t 0.01 -c 1 -i 128 -S 0.2

import sys
import argparse
import serial
import signal
import time

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--serial", nargs=1, metavar="STRING", required=True,
                    help="port of serial interface")
parser.add_argument("-b", "--baudrate", nargs=1, metavar="INT", required=True,
                    help="baud rate", type=int)
parser.add_argument("-t", "--timeout", nargs=1, metavar="FLOAT", required=True,
                    help="read time out", type=float)
parser.add_argument("-c", "--midichannel", nargs=1, metavar="INT",
                    help="MIDI channel", type=int)
parser.add_argument("-i", "--increment", nargs=1, metavar="INT",
                    help="incremental value", type=int)
parser.add_argument("-S", "--sleeptime", nargs=1, metavar="FLOAT",
                    help="interval", type=float)
args= parser.parse_args()
#print(args)
#argv = sys.argv

# Set Keyboard Interrupt
def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    uart.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

__name = "MIDI Pitch Bend Test"
__version = "1.0.0"
version_info = __name + " " + __version
prompt = "\n**Press Ctrl + c to Quit**"

# Set UART Connection
try:
    uart = serial.Serial(port = args.serial[0], baudrate = args.baudrate[0], timeout = args.timeout[0])
except serial.SerialException as e:
    print(version_info + ": Error on UART Settings")
    sys.exit(1)

value_pitchbend = 8192 # 0 to 16383, 8192 is Neutral
bytes = []
bytes.append(0xE0 + ((args.midichannel[0] - 1) & 0xF))
value_increment = args.increment[0]
interval_sleep = args.sleeptime[0]

while True:
    bytes.append( value_pitchbend & 0b1111111 ) # Bit[6:0] LSB
    bytes.append( (value_pitchbend >> 7) & 0b1111111 ) # Bit[13:7] MSB

    for byte_int in bytes:
        byte = byte_int.to_bytes(1, "little")
        uart.write(byte)
        #print(byte)

    print("\033[2J\033[1;1H")
    print(prompt)
    print((bytes[2] << 7) + bytes[1])
    bytes.pop(-1)
    bytes.pop(-1)

    value_pitchbend = value_pitchbend + value_increment
    if value_pitchbend > 16383:
        value_pitchbend = 16383
        value_increment = -(value_increment)
    elif value_pitchbend < 0:
        value_pitchbend = 0
        value_increment = -(value_increment)

    time.sleep(interval_sleep)

