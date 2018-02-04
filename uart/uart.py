#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./uart.py example.txt /dev/serial0 115200 0.01

import sys
import serial
import time

argv = sys.argv
#print (argv[0]) # File Name

f = open( argv[1], "rb") # Read Only
text_all = f.read()

char_star = "\x2A".encode("ascii", "replace") # Asterisk
char_lf = "\x0A".encode("ascii", "replace") # Line Feed
char_cr = "\x0D".encode("ascii", "replace") # Carriage Return
char_nak = "\x15".encode("ascii", "replace") # NAK
esc_up = "\x1B[A".encode("ascii", "replace") # Cursor Up on Escape Sequence
esc_down = "\x1B[B".encode("ascii", "replace") # Cursor Down on Escape Sequence
esc_right = "\x1B[C".encode("ascii", "replace") # Cursor Right on Escape Sequence
esc_left = "\x1B[D".encode("ascii", "replace") # Cursor Left on Escape Sequence

uart = serial.Serial(port = argv[2], baudrate = int(argv[3]), timeout = float(argv[4]))

def uart_send(uart, text, exmirror):
    for integer in text: # Integer
        char = integer.to_bytes(1, "little")
        uart_receive(uart)
        flag = True
        while flag == True:
            if char == char_lf:
               char = char_cr
            uart.write(char)
            char_res = uart.read(1) # Bytes
            if char_res == char: # Receive Succeed
                flag = False
                if exmirror == True:
                    char_res = chr(int.from_bytes(char_res, "little"))
                    print(char_res, end="")
            elif char_res == char_nak: # Receive Negative Acknowledge
                time.sleep(0.001)
            else: # Receive Fails
                flag = False

def uart_receive(uart):
        char = uart.read(1)
        while len(char) != 0:
            char = chr(int.from_bytes(char, "little"))
            print(char, end="")
            char = uart.read(1)

def uart_input(uart):
        while True:
            uart_receive(uart)
            try:
                text_input = input()
            except KeyboardInterrupt:
                break
            print("\x1B[A", end="")
            text_input += "\r"
            text_input = text_input.encode("ascii", "replace")
            uart_send(uart, text_input, False)

uart_send(uart, text_all, True)
uart_receive(uart)
uart_input(uart)
uart.close()

