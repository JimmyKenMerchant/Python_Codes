#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./dmx512_tx.py

import RPi.GPIO as gpio
import sys
import time
import signal
import threading

version_info = "DMX512 TX Alpha"

list_gpio_output = [12,16,19,20,21,26]
num_gpio_busy_toggle = 6
num_gpio_eop_toggle = 13
list_data = []

def dmx512_tx(list_data, count_data, time_delay):
    i = 0;
    while i < count_data:
        data = list_data[i]
        list_bit = []
        if data & 0b00001:
            list_bit.append(list_gpio_output[1])
        if data & 0b00010:
            list_bit.append(list_gpio_output[2])
        if data & 0b00100:
            list_bit.append(list_gpio_output[3])
        if data & 0b01000:
            list_bit.append(list_gpio_output[4])
        if data & 0b10000:
            list_bit.append(list_gpio_output[5])
        #print(list_bit)
        gpio.output(list_gpio_output, 0)
        gpio.output(list_gpio_output[0], 1)
        gpio.output(list_bit, 1)
        gpio.output(list_gpio_output[0], 0) # Falling Edge of Clock
        while time_delay > 0:
             time_delay -= 1
        i += 1
        #while True:
        #    if gpio.event_detected(num_gpio_busy_toggle) == 1:
        #        i += 1
        #        break

def start_dmx512_tx(list_data, count_data, time_delay):
    thread = threading.Thread(name='dmx512_tx', target=dmx512_tx, args=(list_data, count_data, time_delay, ))
    thread.setDaemon(True)
    thread.start()
    return thread

def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    gpio.cleanup()
    sys.exit(0)

argv = sys.argv

if len(argv) == 1:
    time_delay = 100
else:
    time_delay = float(argv[1])

print(sys.version)

gpio.setmode(gpio.BCM)

gpio.setup(list_gpio_output, gpio.OUT)
gpio.output(list_gpio_output, 0)
gpio.setup(num_gpio_busy_toggle, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.add_event_detect(num_gpio_busy_toggle, gpio.BOTH)
gpio.setup(num_gpio_eop_toggle, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.add_event_detect(num_gpio_eop_toggle, gpio.BOTH)

def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    gpio.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

# Initialization of Flushing Method
list_data = [0x1F, 0x1B, 0x11, 0x00, 0x13]
thread1 = start_dmx512_tx(list_data, 5, time_delay)
thread1.join()

# Set Initial Values and Start
list_data = [1] * 1026
thread1 = start_dmx512_tx(list_data, 1026, time_delay)
thread1.join()

# Start DMX512 Transmission
list_data = [0x1D, 0x1A]
thread1 = start_dmx512_tx(list_data, 2, time_delay)
thread1.join()

count = 2
while True:
    list_data = [count] * 1026
    thread1 = start_dmx512_tx(list_data, 1026, time_delay)
    thread1.join()
    count += 1
    if count > 0xF:
        count = 0;
    while True:
        if gpio.event_detected(num_gpio_eop_toggle) == 1:
            break

gpio.cleanup()
