#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./midi2serial.py /dev/serial0 115200 0.01

import sys
import serial
import jack
import binascii
import signal

__name = "JACK Audio Connection Kit to Serial Interface Bridge"
__version = "1.0.0"
version_info = __name + " " + __version
prompt = "\n**Press Enter to Quit**"

print (sys.version)
argv = sys.argv

uart = serial.Serial(port = argv[1], baudrate = int(argv[2]), timeout = float(argv[3]))
midiclient = jack.Client("MIDI-TO-SERIAL")
midiport = midiclient.midi_inports.register("input")

@midiclient.set_process_callback
def process(frames):
    for offset, data in midiport.incoming_midi_events():
        data = binascii.hexlify(data) # Buffer Object (Binary) to String of Ascii Characters
        bytes = [] # Empty List
        for i in range(0, len(data) >> 1, 1): # If 3 bytes, len(data) will be 6. Divided By 2 through Logical Shift Left.
            # data[start(inclusively):end(exclusively)], String to 8-bit Binary
            start = i << 1  # 0,2,4,6...
            end = start + 2 # 2,4,6,8...
            bytes.append(int(data[start:end], 16).to_bytes(1, "little"))

        #print(offset, end="\n")
        #print(data, end="\n")
        #print(bytes, end="\n")
        for byte in bytes:
                uart.write(byte)
                #print(byte)

def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    uart.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

with midiclient:
    print(version_info + prompt)
    input()
    uart.close()
	