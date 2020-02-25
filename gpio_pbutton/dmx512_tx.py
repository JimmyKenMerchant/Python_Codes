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
count_data = 0
list_data = []

def dmx512_tx(time_delay):
    global count_data
    global list_data
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
        print(list_bit)
        gpio.output(list_bit, 1)
        gpio.output(list_gpio_output[0], 1)
        time.sleep(time_delay)
        gpio.output(list_gpio_output[0], 0) # Falling Edge of Clock
        while True:
            if gpio.event_detected(num_gpio_busy_toggle) == 1:
                i += 1
                break
    gpio.output(list_gpio_output, 0)

def start_thread(time_delay):
    thread1 = threading.Thread(name='dmx512_tx', target=dmx512_tx, args=(time_delay, ))
    thread1.setDaemon(True)
    thread1.start()
    thread1.join()
    while True:
        if gpio.event_detected(num_gpio_eop_toggle) == 1:
            break

def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    gpio.cleanup()
    sys.exit(0)

argv = sys.argv

if len(argv) == 1:
    time_delay = 0.01 # 10 Milliseconds
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

list_data = [0x01, 0x10, 0x00]
count_data = 3;
start_thread(time_delay)
