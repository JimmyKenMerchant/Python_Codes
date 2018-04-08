#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./gpio_pbutton.py

import tkinter as tk
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

list_gpio_setup = [20,21]
gpio.setup(list_gpio_setup, gpio.OUT)

#time.sleep(0.5)

class GraphicalInterface:
    """Dependency:tkinter as tk"""
    def __init__(self, root):

        list_gpio_button1 = [20]
        list_gpio_button2 = [21]
        list_gpio_button3 = [20,21]

        def push_button1(event):
            gpio.output(list_gpio_button1, 1)
        def release_button1(event):
            gpio.output(list_gpio_button1, 0)
        def push_button2(event):
            gpio.output(list_gpio_button2, 1)
        def release_button2(event):
            gpio.output(list_gpio_button2, 0)
        def push_button3(event):
            gpio.output(list_gpio_button3, 1)
        def release_button3(event):
            gpio.output(list_gpio_button3, 0)

        self.__root = root
        self.__root.title("GPIO Parallel Button Ver.0.8")

        frame = tk.Frame(self.__root, width=200, height=200)
        frame.pack(padx=5, pady=5, ipadx=10, ipady=10, side=tk.BOTTOM)

        button_1 = tk.Button(frame, text="Button1", bg="black", fg="blue")
        button_1.grid(row=0, column=0, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_2 = tk.Button(frame, text="Button2", bg="black", fg="green")
        button_2.grid(row=0, column=1, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_3 = tk.Button(frame, text="Button3", bg="black", fg="red")
        button_3.grid(row=1, column=0, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

        # Left Mouse Button
        button_1.bind("<Button-1>", push_button1)
        button_1.bind("<ButtonRelease-1>", release_button1)
        button_2.bind("<Button-1>", push_button2)
        button_2.bind("<ButtonRelease-1>", release_button2)
        button_3.bind("<Button-1>", push_button3)
        button_3.bind("<ButtonRelease-1>", release_button3)

        self.__root.mainloop()

    def __del__(self):
            print("END")

root = tk.Tk()
gui = GraphicalInterface(root)
del gui
gpio.cleanup()

