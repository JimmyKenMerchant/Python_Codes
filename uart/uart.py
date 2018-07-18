#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./uart.py example.txt /dev/serial0 115200 0.01

import sys
import serial
import time

char_star = "\x2A".encode("ascii", "replace") # Asterisk
char_lf = "\x0A".encode("ascii", "replace") # Line Feed
char_cr = "\x0D".encode("ascii", "replace") # Carriage Return
char_nak = "\x15".encode("ascii", "replace") # NAK
char_esc = "\x1B".encode("ascii", "replace") # Escape 
char_sepa = "|".encode("ascii", "replace") # Separator
esc_up = "\x1B[A".encode("ascii", "replace") # Cursor Up on Escape Sequence
esc_down = "\x1B[B".encode("ascii", "replace") # Cursor Down on Escape Sequence
esc_right = "\x1B[C".encode("ascii", "replace") # Cursor Right on Escape Sequence
esc_left = "\x1B[D".encode("ascii", "replace") # Cursor Left on Escape Sequence

class UartConsole:
    """Dependency:time"""
    def __init__(self, uart, file):
        self.__uart = uart
        self.file = file

    def send(self, text, enmirror, enwrite):
        for integer in text: # Integer
            char = integer.to_bytes(1, "little")
            self.receive(enmirror, enwrite)
            flag = True
            while flag == True:
                if char == char_lf:
                   char = char_cr
                self.__uart.write(char)
                char_res = self.__uart.read(1) # Bytes
                if char_res == char: # Receive Succeed
                    flag = False
                    if enwrite == True: # Write to File
                        self.write(char_res)
                    if enmirror == True: # External Mirror
                        char_res = chr(int.from_bytes(char_res, "little"))
                        print(char_res, end="")
                elif char_res == char_nak: # Receive Negative Acknowledge
                    time.sleep(0.001)
                else: # Receive Fails
                    flag = False

    def receive(self, enmirror, enwrite):
            char = self.__uart.read(1)
            while len(char) != 0:
                if enwrite == True:
                    self.write(char)
                if enmirror == True:
                    char = chr(int.from_bytes(char, "little"))
                    print(char, end="")
                char = self.__uart.read(1)

    def write(self,char):
        if self.file is not None:
            if char == char_cr:
                return
            char = chr(int.from_bytes(char, "little"))
            self.file.write(char)

    def input(self):
            while True:
                self.receive(True, True)
                try:
                    text_input = input()
                except KeyboardInterrupt:
                    break
                print("\x1B[A", end="")
                text_input += "\r"
                text_input = text_input.encode("ascii", "replace")
                self.send(text_input, True, False)

    def __del__(self):
        self.__uart.close()

print (sys.version)
argv = sys.argv
print (argv[0]) # File Name

fsrc = open( argv[1], "rb") # Read Only With Raw Data (Integer)
text_all = fsrc.read()
if len(argv) == 6: # If Sixth Argument Exists (File to Write)
    fdst = open( argv[5], "w+") # Write Only With UTF-8
else:
    fdst = None;

uart = serial.Serial(port = argv[2], baudrate = int(argv[3]), timeout = float(argv[4]))
uartconsole = UartConsole(uart, fdst)
uartconsole.send(text_all, True, False)
uartconsole.receive(True, True)
uartconsole.input()
uartconsole.receive(True, True)
del uartconsole

