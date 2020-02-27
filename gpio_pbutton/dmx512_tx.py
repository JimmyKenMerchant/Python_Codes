#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./dmx512_tx.py

import RPi.GPIO as gpio
import threading

version_info = "DMX512 TX Alpha"

class DMX512:
    """Dependency:RPi.GPIO, threading"""
    def __init__(self, list_gpio_output, num_gpio_busy_toggle, num_gpio_eop_toggle):
        self.list_gpio_output = list_gpio_output
        self.num_gpio_busy_toggle = num_gpio_busy_toggle
        self.num_gpio_eop_toggle = num_gpio_eop_toggle
        gpio.setmode(gpio.BCM)
        gpio.setup(self.list_gpio_output, gpio.OUT)
        gpio.output(self.list_gpio_output, 0)
        gpio.setup(self.num_gpio_busy_toggle, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        #gpio.add_event_detect(num_gpio_busy_toggle, gpio.BOTH)
        gpio.setup(self.num_gpio_eop_toggle, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        #gpio.add_event_detect(num_gpio_eop_toggle, gpio.BOTH)

    def transmitter(self, list_data, index, length, time_delay):
        status_gpio_busy_toggle = gpio.input(self.num_gpio_busy_toggle)
        length += index;
        while index < length:
            data = list_data[index]
            list_bit = []
            if data & 0b00001:
                list_bit.append(self.list_gpio_output[1])
            if data & 0b00010:
                list_bit.append(self.list_gpio_output[2])
            if data & 0b00100:
                list_bit.append(self.list_gpio_output[3])
            if data & 0b01000:
                list_bit.append(self.list_gpio_output[4])
            if data & 0b10000:
                list_bit.append(self.list_gpio_output[5])
            print(list_bit)
            gpio.output(self.list_gpio_output, 0)
            gpio.output(self.list_gpio_output[0], 1) # High State of Clock
            gpio.output(list_bit, 1)
            dup_time_delay = time_delay
            while dup_time_delay > 0:
                dup_time_delay -= 1
            gpio.output(self.list_gpio_output[0], 0) # Falling Edge of Clock
            while True:
                if status_gpio_busy_toggle != gpio.input(self.num_gpio_busy_toggle):
                    status_gpio_busy_toggle = gpio.input(self.num_gpio_busy_toggle)
                    index += 1
                    break

    def start_tx(self, list_data, index, length, time_delay):
        thread = threading.Thread(name='dmx512_start_tx', target=self.transmitter, args=(list_data, index, length, time_delay, ))
        thread.setDaemon(True)
        thread.start()
        return thread

    def eop_toggle(self):
        return gpio.input(self.num_gpio_eop_toggle)

    def __del__(self):
        gpio.cleanup()

if __name__ == '__main__':
    import sys
    import time
    import signal

    def handle_sigint(signum, frame):
        print(version_info + ": Force Stop")
        sys.exit(0)
    signal.signal(signal.SIGINT, handle_sigint)

    argv = sys.argv
    if len(argv) == 1:
        time_delay = 10
    else:
        time_delay = float(argv[1])
    print(sys.version)

    # Call Class
    dmx512 = DMX512([12,16,19,20,21,26], 6, 13)

    # Initialization of Flushing Method
    list_data = [0x1F, 0x14, 0x1B, 0x11, 0x00, 0x13]
    thread1 = dmx512.start_tx(list_data, 0, 6, time_delay)
    thread1.join()

    # Set Initial Values and Start
    list_data = [1] * 1026
    thread1 = dmx512.start_tx(list_data, 0, 1026, time_delay)
    thread1.join()

    # Start DMX512 Transmission
    list_data = [0x1D, 0x1A]
    thread1 = dmx512.start_tx(list_data, 0, 2, time_delay)
    thread1.join()

    status_gpio_eop_toggle = dmx512.eop_toggle()
    count = 2
    while True:
        list_data = [count] * 1026
        thread1 = dmx512.start_tx(list_data, 0, 1026, time_delay)
        thread1.join()
        count += 1
        if count > 0xF:
            count = 0;
        while True:
            if status_gpio_eop_toggle != dmx512.eop_toggle():
                status_gpio_eop_toggle = dmx512.eop_toggle()
                break
            #if gpio.event_detected(num_gpio_eop_toggle) == 1:
            #    break
