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

# Set MIDI Channel for Psuedo Polyphonic Function (PPP Channel)
if len(argv) >= 5:
    ppp_midichannel = int(argv[4]) - 1
else:
    ppp_midichannel = None # None Type

# Set Number of Monophonic Devices for Pseudo Polyphonic Function
if len(argv) >= 6:
    ppp_numberdevices = int(argv[5])
    # Make Table to Check Active/Inactive Monophonic Devices and Current Tone Number
    ppp_devices = []
    for i in range(0, ppp_numberdevices, 1):
        ppp_devices.append(0x80) # MIDI Tone Number Is Up to 127 (0x7F)
else:
    ppp_numberdevices = None # None Type

# Set UART Connection
try:
    uart = serial.Serial(port = argv[1], baudrate = int(argv[2]), timeout = float(argv[3]))
except serial.SerialException as e:
    print(version_info + ": Error on UART Settings")
    sys.exit(1)

# Set MIDI Connection and Callback
midiclient = jack.Client("MIDI-TO-SERIAL")
midiport = midiclient.midi_inports.register("input")

@midiclient.set_process_callback
def process(frames):
    for offset, data in midiport.incoming_midi_events():
        data = binascii.hexlify(data) # Buffer Object (Binary) to String of Ascii Characters
        bytes = [] # Empty List
        for i in range(0, len(data) >> 1, 1): # If 3 bytes, len(data) will be 6. Divided By 2 through Logical Shift Right.
            # data[start(inclusively):end(exclusively)], String to 8-bit Binary
            start = i << 1  # 0,2,4,6... Multiplied By 2 through Logical Shift Left.
            end = start + 2 # 2,4,6,8...
            bytes.append(int(data[start:end], 16))

        bytes = psuedo_polyphonic(bytes)

        #print(offset, end="\n")
        #print(data, end="\n")
        #print(bytes, end="\n")

        for byte_int in bytes:
            byte = byte_int.to_bytes(1, "little")
            uart.write(byte)
            #print(byte)

# This Function Assumes That Only One MIDI Message Is Captured by Client
def psuedo_polyphonic(bytes):
    for count, byte_int in enumerate(bytes):
        if byte_int >= 0x80: # If Status Byte
            if ppp_midichannel is not None:
                midichannel = byte_int & 0xF # Only Bit[3:0], 0 to 15
                if ppp_midichannel == midichannel: # If Channel Is Matched with Psuedo Polyphonic Channel
                    midistatus = byte_int >> 4 # Only Bit[7:4], 8 to 15

                    if midistatus <= 8: # If Note Off
                        for i in range(0, ppp_numberdevices, 1): # If 3 bytes, len(data) will be 6. Divided By 2 through Logical Shift Right.
                            if ppp_devices[i] == bytes[count + 1]:
                                bytes[count] = (byte_int & 0xF0) + ((ppp_midichannel + i + 1) & 0xF)
                                ppp_devices[i] = 0x80

                                break # Break For Loop, Not If Syntax

                        return bytes

                    elif midistatus <= 9: # If Note On
                        for i in range(0, ppp_numberdevices, 1): # If 3 bytes, len(data) will be 6. Divided By 2 through Logical Shift Right.
                            if ppp_devices[i] >= 0x80:
                                bytes[count] = (byte_int & 0xF0) + ((ppp_midichannel + i + 1) & 0xF)
                                ppp_devices[i] = bytes[count + 1]

                                break # Break For Loop, Not If Syntax

                        return bytes

                    elif midistatus <= 10: # If Polyphonic Key Pressure
                        for i in range(0, ppp_numberdevices, 1): # If 3 bytes, len(data) will be 6. Divided By 2 through Logical Shift Right.
                            if ppp_devices[i] == bytes[count + 1]:
                                bytes[count] = (byte_int & 0xF0) + ((ppp_midichannel + i + 1) & 0xF)

                                break # Break For Loop, Not If Syntax

                        return bytes

                    else: # If Other Messages, Pitch Bend, etc.
                        bytes_tuple = tuple(bytes) # Make Constant List from Dynamic List
                        bytes.clear() # Clear to Empty List
                        for i in range(0, ppp_numberdevices, 1):
                            for byte_tuple_int in bytes_tuple:
                                if byte_tuple_int >= 0x80: # If Status Byte
                                    bytes.append((byte_tuple_int & 0xF0) + ((ppp_midichannel + i + 1) & 0xF))
                                else: # If Data Byte
                                    bytes.append(byte_tuple_int)

                        return bytes

    return bytes

# Set Keyboard Interrupt
def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    uart.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

# Activate MIDI Client by "with" Syntax
#midiclient.activate()
#midiclient.deactivate()
#midiclient.close()
with midiclient:
    print(version_info + prompt)
    input()
    uart.close()
