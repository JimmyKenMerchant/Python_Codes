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
            if char_res == char:
                flag = False
                if exmirror == True:
                    char_res = chr(int.from_bytes(char_res, "little"))
                    print(char_res, end="")
            elif char_res == char_nak:
                time.sleep(0.001)

def uart_receive(uart):
        char = uart.read(1)
        while len(char) != 0:
            char = chr(int.from_bytes(char, "little"))
            print(char, end="")
            char = uart.read(1)

def uart_input(uart):
        flag = True
        while flag == True:
            uart_receive(uart)
            text_input = input()
            text_input_len = len(text_input)
            print("\x1B[A", end="")
            if text_input_len != 0:
                text_input += "\r"
                text_input = text_input.encode("ascii", "replace")
                uart_send(uart, text_input, False)
            else:
                flag = False # If No Input, Loop Ends

uart_send(uart, text_all, True)
uart_receive(uart)
uart_input(uart)
uart.close()
