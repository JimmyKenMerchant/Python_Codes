#!/usr/bin/python

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# python3 ./uart.py example.txt /dev/serial0 115200 0.01

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

int_star = int.from_bytes(char_star, "little")
int_cr = int.from_bytes(char_cr, "little")
list_cr = [int_star, int_cr]

uart = serial.Serial(port = argv[2], baudrate = int(argv[3]), timeout = float(argv[4]))

def uart_send(text):
    for integer in text: # Integer
        char = integer.to_bytes(1, "little")
        char_prior = uart.read(1)
        while len(char_prior) != 0:
            char_prior = chr(int.from_bytes(char_prior, "little"))
            print(char_prior, end="")
            char_prior = uart.read(1)
        flag = True
        while flag == True:
            if char == char_lf:
               char = char_cr
            uart.write(char)
            char_res = uart.read(1) # Bytes
            if char_res == char:
                flag = False
                char_res = chr(int.from_bytes(char_res, "little"))
                print(char_res, end="")
            elif char_res == char_nak:
                time.sleep(0.001)

uart_send(list_cr)
uart_send(text_all)
uart.close()
