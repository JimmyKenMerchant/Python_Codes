#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./dmx512_tx.py

import dmx512
import tkinter as tk
import sys
import time
import signal

# Color Settings
color_root_bg= "black"
color_frame_bg= "black"
color_odd_bg= "black"
color_even_bg= "gray"
color_label_bg= "white"

# Text Settings
version_info = "DMX512 Bar Alpha"
slider_1_text = "Slider 1"
button_1_text = "Set"

def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    sys.exit(0)
signal.signal(signal.SIGINT, handle_sigint)

argv = sys.argv
if len(argv) == 1:
    time_delay = 4
else:
    time_delay = float(argv[1])
print(sys.version)

# Call Class
dmx512 = dmx512.DMX512([12,16,19,20,21,26], 6, 13)

# Initialization of Flushing Method
list_data = [0x1E, 0x15, 0x1C]
thread1 = dmx512.start_tx(list_data, 0, 3, time_delay)
thread1.join()

# Make GUI
root = tk.Tk()
root.title(version_info)
root["bg"] = color_root_bg
frame = tk.Frame(root, bg=color_frame_bg)
frame.pack(padx=10, pady=10, ipadx=10, ipady=10, side=tk.BOTTOM)

def slide_slider_1(event):
    list_data = [0x12] # Select Slot Value Mode to Send Data
    value = slider_1.get()
    list_data.append(value & 0x0F)
    list_data.append((value >> 4) & 0x0F)
    list_data.append(0x1A) # Start Tx
    thread1 = dmx512.start_tx(list_data, 0, 4, time_delay)
    thread1.join()
    #print(slider_1.get())
slider_1 = tk.Scale(frame, from_=255, to=0, command=slide_slider_1, bg=color_odd_bg, fg="blue")
slider_1.grid(row=0, column=0, columnspan=2, padx=(25,5), pady=(25,5), ipadx=10, ipady=10)

button_1 = tk.Button(frame, width=3, height=1, text=button_1_text, font=("Roboto", "12"), bg=color_odd_bg, fg="blue")
button_1.grid(row=1, column=0, columnspan=1, padx=(25,5), pady=(25,5), ipadx=2, ipady=2)

entry_1 = tk.Entry(frame, width=8, fg="blue")
entry_1.grid(row=1, column=1, columnspan=1, padx=(25,5), pady=(25,5), ipadx=2, ipady=2)

def push_button_1(event):
    list_data = [0x11] # Select Slot Index Mode to Send Data
    value = int(entry_1.get())
    list_data.append(value & 0x0F)
    list_data.append((value >> 4) & 0x0F)
    list_data.append((value >> 8) & 0x03)
    thread1 = dmx512.start_tx(list_data, 0, 4, time_delay)
    thread1.join()
    #print(entry_1.get())
    
# Left Mouse Button
button_1.bind("<Button-1>", push_button_1)

root.mainloop()
