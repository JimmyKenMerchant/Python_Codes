#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./gpio_pbutton.py

import tkinter as tk
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

list_gpio_setup = [16,19,20,21,26]
gpio.setup(list_gpio_setup, gpio.OUT)

#time.sleep(0.5)

class GraphicalInterface:
    """Dependency:tkinter as tk"""
    def __init__(self, root):

        list_gpio_button1 = [16]
        list_gpio_button2 = [19]
        list_gpio_button3 = [16,19]
        list_gpio_button4 = [20]
        list_gpio_button5 = [16,20]
        list_gpio_button6 = [19,20]
        list_gpio_button7 = [16,19,20]
        list_gpio_button8 = [21]
        list_gpio_button9 = [16,21]
        list_gpio_button10 = [19,21]
        list_gpio_button11 = [16,19,21]
        list_gpio_button12 = [20,21]
        list_gpio_button13 = [16,20,21]
        list_gpio_button14 = [19,20,21]
        list_gpio_button15 = [16,19,20,21]
        list_gpio_button16 = [26]
        list_gpio_button17 = [16,26]
        list_gpio_button18 = [19,26]
        list_gpio_button19 = [16,19,26]
        list_gpio_button20 = [20,26]
        list_gpio_button21 = [16,20,26]
        list_gpio_button22 = [19,20,26]
        list_gpio_button23 = [16,19,20,26]
        list_gpio_button24 = [21,26]
        list_gpio_button25 = [16,21,26]
        list_gpio_button26 = [19,21,26]
        list_gpio_button27 = [16,19,21,26]
        list_gpio_button28 = [20,21,26]
        list_gpio_button29 = [16,20,21,26]
        list_gpio_button30 = [19,20,21,26]
        list_gpio_button31 = [16,19,20,21,26]

        def push_button(event):
            if event.widget["text"] == "Button1":
                gpio.output(list_gpio_button1, 1)
            elif event.widget["text"] == "Button2":
                gpio.output(list_gpio_button2, 1)
            elif event.widget["text"] == "Button3":
                gpio.output(list_gpio_button3, 1)
            elif event.widget["text"] == "Button4":
                gpio.output(list_gpio_button4, 1)
            elif event.widget["text"] == "Button5":
                gpio.output(list_gpio_button5, 1)
            elif event.widget["text"] == "Button6":
                gpio.output(list_gpio_button6, 1)
            elif event.widget["text"] == "Button7":
                gpio.output(list_gpio_button7, 1)
            elif event.widget["text"] == "Button8":
                gpio.output(list_gpio_button8, 1)
            elif event.widget["text"] == "Button9":
                gpio.output(list_gpio_button9, 1)
            elif event.widget["text"] == "Button10":
                gpio.output(list_gpio_button10, 1)
            elif event.widget["text"] == "Button11":
                gpio.output(list_gpio_button11, 1)
            elif event.widget["text"] == "Button12":
                gpio.output(list_gpio_button12, 1)
            elif event.widget["text"] == "Button13":
                gpio.output(list_gpio_button13, 1)
            elif event.widget["text"] == "Button14":
                gpio.output(list_gpio_button14, 1)
            elif event.widget["text"] == "Button15":
                gpio.output(list_gpio_button15, 1)
            elif event.widget["text"] == "Button16":
                gpio.output(list_gpio_button16, 1)
            elif event.widget["text"] == "Button17":
                gpio.output(list_gpio_button17, 1)
            elif event.widget["text"] == "Button18":
                gpio.output(list_gpio_button18, 1)
            elif event.widget["text"] == "Button19":
                gpio.output(list_gpio_button19, 1)
            elif event.widget["text"] == "Button20":
                gpio.output(list_gpio_button20, 1)
            elif event.widget["text"] == "Button21":
                gpio.output(list_gpio_button21, 1)
            elif event.widget["text"] == "Button22":
                gpio.output(list_gpio_button22, 1)
            elif event.widget["text"] == "Button23":
                gpio.output(list_gpio_button23, 1)
            elif event.widget["text"] == "Button24":
                gpio.output(list_gpio_button24, 1)
            elif event.widget["text"] == "Button25":
                gpio.output(list_gpio_button25, 1)
            elif event.widget["text"] == "Button26":
                gpio.output(list_gpio_button26, 1)
            elif event.widget["text"] == "Button27":
                gpio.output(list_gpio_button27, 1)
            elif event.widget["text"] == "Button28":
                gpio.output(list_gpio_button28, 1)
            elif event.widget["text"] == "Button29":
                gpio.output(list_gpio_button29, 1)
            elif event.widget["text"] == "Button30":
                gpio.output(list_gpio_button30, 1)
            elif event.widget["text"] == "Button31":
                gpio.output(list_gpio_button31, 1)

        def release_button(event):
            if event.widget["text"] == "Button1":
                gpio.output(list_gpio_button1, 0)
            elif event.widget["text"] == "Button2":
                gpio.output(list_gpio_button2, 0)
            elif event.widget["text"] == "Button3":
                gpio.output(list_gpio_button3, 0)
            elif event.widget["text"] == "Button4":
                gpio.output(list_gpio_button4, 0)
            elif event.widget["text"] == "Button5":
                gpio.output(list_gpio_button5, 0)
            elif event.widget["text"] == "Button6":
                gpio.output(list_gpio_button6, 0)
            elif event.widget["text"] == "Button7":
                gpio.output(list_gpio_button7, 0)
            elif event.widget["text"] == "Button8":
                gpio.output(list_gpio_button8, 0)
            elif event.widget["text"] == "Button9":
                gpio.output(list_gpio_button9, 0)
            elif event.widget["text"] == "Button10":
                gpio.output(list_gpio_button10, 0)
            elif event.widget["text"] == "Button11":
                gpio.output(list_gpio_button11, 0)
            elif event.widget["text"] == "Button12":
                gpio.output(list_gpio_button12, 0)
            elif event.widget["text"] == "Button13":
                gpio.output(list_gpio_button13, 0)
            elif event.widget["text"] == "Button14":
                gpio.output(list_gpio_button14, 0)
            elif event.widget["text"] == "Button15":
                gpio.output(list_gpio_button15, 0)
            elif event.widget["text"] == "Button16":
                gpio.output(list_gpio_button16, 0)
            elif event.widget["text"] == "Button17":
                gpio.output(list_gpio_button17, 0)
            elif event.widget["text"] == "Button18":
                gpio.output(list_gpio_button18, 0)
            elif event.widget["text"] == "Button19":
                gpio.output(list_gpio_button19, 0)
            elif event.widget["text"] == "Button20":
                gpio.output(list_gpio_button20, 0)
            elif event.widget["text"] == "Button21":
                gpio.output(list_gpio_button21, 0)
            elif event.widget["text"] == "Button22":
                gpio.output(list_gpio_button22, 0)
            elif event.widget["text"] == "Button23":
                gpio.output(list_gpio_button23, 0)
            elif event.widget["text"] == "Button24":
                gpio.output(list_gpio_button24, 0)
            elif event.widget["text"] == "Button25":
                gpio.output(list_gpio_button25, 0)
            elif event.widget["text"] == "Button26":
                gpio.output(list_gpio_button26, 0)
            elif event.widget["text"] == "Button27":
                gpio.output(list_gpio_button27, 0)
            elif event.widget["text"] == "Button28":
                gpio.output(list_gpio_button28, 0)
            elif event.widget["text"] == "Button29":
                gpio.output(list_gpio_button29, 0)
            elif event.widget["text"] == "Button30":
                gpio.output(list_gpio_button30, 0)
            elif event.widget["text"] == "Button31":
                gpio.output(list_gpio_button31, 0)

        self.__root = root
        self.__root.title("GPIO Push Button Ver.0.8")

        frame = tk.Frame(self.__root, bg="blue")
        frame.pack(padx=10, pady=10, ipadx=10, ipady=10, side=tk.BOTTOM)

        button_1 = tk.Button(frame, width=6, height=2, text="Button1", font=("Roboto", "20"), bg="black", fg="blue")
        button_1.grid(row=0, column=0, columnspan=1, padx=(25,5), pady=(25,5), ipadx=10, ipady=10)
        button_2 = tk.Button(frame, width=6, height=2, text="Button2", font=("Roboto", "20"), bg="black", fg="green")
        button_2.grid(row=0, column=1, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_3 = tk.Button(frame, width=6, height=2, text="Button3", font=("Roboto", "20"), bg="black", fg="red")
        button_3.grid(row=0, column=2, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_4 = tk.Button(frame, width=6, height=2, text="Button4", font=("Roboto", "20"), bg="black", fg="cyan")
        button_4.grid(row=0, column=3, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_5 = tk.Button(frame, width=6, height=2, text="Button5", font=("Roboto", "20"), bg="black", fg="magenta")
        button_5.grid(row=0, column=4, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_6 = tk.Button(frame, width=6, height=2, text="Button6", font=("Roboto", "20"), bg="black", fg="yellow")
        button_6.grid(row=0, column=5, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)

        button_7 = tk.Button(frame, width=6, height=2, text="Button7", font=("Roboto", "20"), bg="gray", fg="blue")
        button_7.grid(row=1, column=0, columnspan=1, padx=(25,5), pady=5, ipadx=10, ipady=10)
        button_8 = tk.Button(frame, width=6, height=2, text="Button8", font=("Roboto", "20"), bg="gray", fg="green")
        button_8.grid(row=1, column=1, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_9 = tk.Button(frame, width=6, height=2, text="Button9", font=("Roboto", "20"), bg="gray", fg="red")
        button_9.grid(row=1, column=2, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_10 = tk.Button(frame, width=6, height=2, text="Button10", font=("Roboto", "20"), bg="gray", fg="cyan")
        button_10.grid(row=1, column=3, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_11 = tk.Button(frame, width=6, height=2, text="Button11", font=("Roboto", "20"), bg="gray", fg="magenta")
        button_11.grid(row=1, column=4, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_12 = tk.Button(frame, width=6, height=2, text="Button12", font=("Roboto", "20"), bg="gray", fg="yellow")
        button_12.grid(row=1, column=5, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

        # Left Mouse Button
        button_1.bind("<Button-1>", push_button)
        button_1.bind("<ButtonRelease-1>", release_button)
        button_2.bind("<Button-1>", push_button)
        button_2.bind("<ButtonRelease-1>", release_button)
        button_3.bind("<Button-1>", push_button)
        button_3.bind("<ButtonRelease-1>", release_button)
        button_4.bind("<Button-1>", push_button)
        button_4.bind("<ButtonRelease-1>", release_button)
        button_5.bind("<Button-1>", push_button)
        button_5.bind("<ButtonRelease-1>", release_button)
        button_6.bind("<Button-1>", push_button)
        button_6.bind("<ButtonRelease-1>", release_button)
        button_7.bind("<Button-1>", push_button)
        button_7.bind("<ButtonRelease-1>", release_button)
        button_8.bind("<Button-1>", push_button)
        button_8.bind("<ButtonRelease-1>", release_button)
        button_9.bind("<Button-1>", push_button)
        button_9.bind("<ButtonRelease-1>", release_button)
        button_10.bind("<Button-1>", push_button)
        button_10.bind("<ButtonRelease-1>", release_button)
        button_11.bind("<Button-1>", push_button)
        button_11.bind("<ButtonRelease-1>", release_button)
        button_12.bind("<Button-1>", push_button)
        button_12.bind("<ButtonRelease-1>", release_button)

        self.__root.mainloop()

    def __del__(self):
            print("END")

root = tk.Tk()
gui = GraphicalInterface(root)
del gui
gpio.cleanup()

