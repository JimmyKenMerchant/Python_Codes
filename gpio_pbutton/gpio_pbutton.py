#!/usr/bin/python3

# Author: Kenta Ishii
# SPDX short identifier: BSD-3-Clause
# ./gpio_pbutton.py 0.01

import tkinter as tk
import RPi.GPIO as gpio
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
version_info = "GPIO Push Button 0.9.2 Beta"
indicator_info = "NOW: "
button1_text = "Button1"
button2_text = "Button2"
button3_text = "Button3"
button4_text = "Button4"
button5_text = "Button5"
button6_text = "Button6"
button7_text = "Button7"
button8_text = "Button8"
button9_text = "Button9"
button10_text = "Button10"
button11_text = "Button11"
button12_text = "Button12"
button13_text = "Button13"
button14_text = "Button14"
button15_text = "Button15"
button16_text = "Button16"
button17_text = "Button17"
button18_text = "Button18"
button19_text = "Button19"
button20_text = "Button20"
button21_text = "Button21"
button22_text = "Button22"
button23_text = "Button23"
button24_text = "Button24"
button25_text = "Button25"
button26_text = "Button26"
button27_text = "Button27"
button28_text = "Button28"
button29_text = "UP"
button30_text = "DOWN"
button31_text = "CLEAR"
label0_text = ""

class GraphicalInterface:
    """Dependency:tkinter as tk"""
    def __init__(self, root):

        print(version_info + ": START")

        clock_button = 13
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

        def push_button1(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button1, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button1_text)
        def push_button2(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button2, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button2_text)
        def push_button3(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button3, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button3_text)
        def push_button4(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button4, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button4_text)
        def push_button5(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button5, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button5_text)
        def push_button6(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button6, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button6_text)
        def push_button7(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button7, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button7_text)
        def push_button8(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button8, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button8_text)
        def push_button9(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button9, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button9_text)
        def push_button10(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button10, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button10_text)
        def push_button11(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button11, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button11_text)
        def push_button12(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button12, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button12_text)
        def push_button13(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button13, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button13_text)
        def push_button14(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button14, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button14_text)
        def push_button15(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button15, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button15_text)
        def push_button16(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button16, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button16_text)
        def push_button17(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button17, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button17_text)
        def push_button18(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button18, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button18_text)
        def push_button19(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button19, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button19_text)
        def push_button20(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button20, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button20_text)
        def push_button21(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button21, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button21_text)
        def push_button22(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button22, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button22_text)
        def push_button23(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button23, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button23_text)
        def push_button24(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button24, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button24_text)
        def push_button25(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button25, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button25_text)
        def push_button26(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button26, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button26_text)
        def push_button27(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button27, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button27_text)
        def push_button28(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button28, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button28_text)
        def push_button29(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button29, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button29_text)
        def push_button30(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button30, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button30_text)
        def push_button31(event):
            gpio.output(clock_button, 0)
            gpio.output(list_gpio_button31, 1)
            time.sleep(time_delay)
            gpio.output(clock_button, 1)
            label_0.config(text=indicator_info + button31_text)

        def release_button1(event):
            gpio.output(list_gpio_button1, 0)
        def release_button2(event):
            gpio.output(list_gpio_button2, 0)
        def release_button3(event):
            gpio.output(list_gpio_button3, 0)
        def release_button4(event):
            gpio.output(list_gpio_button4, 0)
        def release_button5(event):
            gpio.output(list_gpio_button5, 0)
        def release_button6(event):
            gpio.output(list_gpio_button6, 0)
        def release_button7(event):
            gpio.output(list_gpio_button7, 0)
        def release_button8(event):
            gpio.output(list_gpio_button8, 0)
        def release_button9(event):
            gpio.output(list_gpio_button9, 0)
        def release_button10(event):
            gpio.output(list_gpio_button10, 0)
        def release_button11(event):
            gpio.output(list_gpio_button11, 0)
        def release_button12(event):
            gpio.output(list_gpio_button12, 0)
        def release_button13(event):
            gpio.output(list_gpio_button13, 0)
        def release_button14(event):
            gpio.output(list_gpio_button14, 0)
        def release_button15(event):
            gpio.output(list_gpio_button15, 0)
        def release_button16(event):
            gpio.output(list_gpio_button16, 0)
        def release_button17(event):
            gpio.output(list_gpio_button17, 0)
        def release_button18(event):
            gpio.output(list_gpio_button18, 0)
        def release_button19(event):
            gpio.output(list_gpio_button19, 0)
        def release_button20(event):
            gpio.output(list_gpio_button20, 0)
        def release_button21(event):
            gpio.output(list_gpio_button21, 0)
        def release_button22(event):
            gpio.output(list_gpio_button22, 0)
        def release_button23(event):
            gpio.output(list_gpio_button23, 0)
        def release_button24(event):
            gpio.output(list_gpio_button24, 0)
        def release_button25(event):
            gpio.output(list_gpio_button25, 0)
        def release_button26(event):
            gpio.output(list_gpio_button26, 0)
        def release_button27(event):
            gpio.output(list_gpio_button27, 0)
        def release_button28(event):
            gpio.output(list_gpio_button28, 0)
        def release_button29(event):
            gpio.output(list_gpio_button29, 0)
        def release_button30(event):
            gpio.output(list_gpio_button30, 0)
        def release_button31(event):
            gpio.output(list_gpio_button31, 0)

        self.__root = root
        self.__root.title(version_info)
        self.__root["bg"] = color_root_bg

        frame = tk.Frame(self.__root, bg=color_frame_bg)
        frame.pack(padx=10, pady=10, ipadx=10, ipady=10, side=tk.BOTTOM)

        button_1 = tk.Button(frame, width=6, height=2, text=button1_text, font=("Roboto", "20"), bg=color_odd_bg, fg="blue")
        button_1.grid(row=0, column=0, columnspan=1, padx=(25,5), pady=(25,5), ipadx=10, ipady=10)
        button_2 = tk.Button(frame, width=6, height=2, text=button2_text, font=("Roboto", "20"), bg=color_odd_bg, fg="green")
        button_2.grid(row=0, column=1, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_3 = tk.Button(frame, width=6, height=2, text=button3_text, font=("Roboto", "20"), bg=color_odd_bg, fg="red")
        button_3.grid(row=0, column=2, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_4 = tk.Button(frame, width=6, height=2, text=button4_text, font=("Roboto", "20"), bg=color_odd_bg, fg="cyan")
        button_4.grid(row=0, column=3, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_5 = tk.Button(frame, width=6, height=2, text=button5_text, font=("Roboto", "20"), bg=color_odd_bg, fg="magenta")
        button_5.grid(row=0, column=4, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)
        button_6 = tk.Button(frame, width=6, height=2, text=button6_text, font=("Roboto", "20"), bg=color_odd_bg, fg="yellow")
        button_6.grid(row=0, column=5, columnspan=1, padx=5, pady=(25,5), ipadx=10, ipady=10)

        button_7 = tk.Button(frame, width=6, height=2, text=button7_text, font=("Roboto", "20"), bg=color_even_bg, fg="blue")
        button_7.grid(row=1, column=0, columnspan=1, padx=(25,5), pady=5, ipadx=10, ipady=10)
        button_8 = tk.Button(frame, width=6, height=2, text=button8_text, font=("Roboto", "20"), bg=color_even_bg, fg="green")
        button_8.grid(row=1, column=1, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_9 = tk.Button(frame, width=6, height=2, text=button9_text, font=("Roboto", "20"), bg=color_even_bg, fg="red")
        button_9.grid(row=1, column=2, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_10 = tk.Button(frame, width=6, height=2, text=button10_text, font=("Roboto", "20"), bg=color_even_bg, fg="cyan")
        button_10.grid(row=1, column=3, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_11 = tk.Button(frame, width=6, height=2, text=button11_text, font=("Roboto", "20"), bg=color_even_bg, fg="magenta")
        button_11.grid(row=1, column=4, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_12 = tk.Button(frame, width=6, height=2, text=button12_text, font=("Roboto", "20"), bg=color_even_bg, fg="yellow")
        button_12.grid(row=1, column=5, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

        button_13 = tk.Button(frame, width=6, height=2, text=button13_text, font=("Roboto", "20"), bg=color_odd_bg, fg="blue")
        button_13.grid(row=2, column=0, columnspan=1, padx=(25,5), pady=5, ipadx=10, ipady=10)
        button_14 = tk.Button(frame, width=6, height=2, text=button14_text, font=("Roboto", "20"), bg=color_odd_bg, fg="green")
        button_14.grid(row=2, column=1, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_15 = tk.Button(frame, width=6, height=2, text=button15_text, font=("Roboto", "20"), bg=color_odd_bg, fg="red")
        button_15.grid(row=2, column=2, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_16 = tk.Button(frame, width=6, height=2, text=button16_text, font=("Roboto", "20"), bg=color_odd_bg, fg="cyan")
        button_16.grid(row=2, column=3, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_17 = tk.Button(frame, width=6, height=2, text=button17_text, font=("Roboto", "20"), bg=color_odd_bg, fg="magenta")
        button_17.grid(row=2, column=4, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_18 = tk.Button(frame, width=6, height=2, text=button18_text, font=("Roboto", "20"), bg=color_odd_bg, fg="yellow")
        button_18.grid(row=2, column=5, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

        button_19 = tk.Button(frame, width=6, height=2, text=button19_text, font=("Roboto", "20"), bg=color_even_bg, fg="blue")
        button_19.grid(row=3, column=0, columnspan=1, padx=(25,5), pady=5, ipadx=10, ipady=10)
        button_20 = tk.Button(frame, width=6, height=2, text=button20_text, font=("Roboto", "20"), bg=color_even_bg, fg="green")
        button_20.grid(row=3, column=1, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_21 = tk.Button(frame, width=6, height=2, text=button21_text, font=("Roboto", "20"), bg=color_even_bg, fg="red")
        button_21.grid(row=3, column=2, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_22 = tk.Button(frame, width=6, height=2, text=button22_text, font=("Roboto", "20"), bg=color_even_bg, fg="cyan")
        button_22.grid(row=3, column=3, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_23 = tk.Button(frame, width=6, height=2, text=button23_text, font=("Roboto", "20"), bg=color_even_bg, fg="magenta")
        button_23.grid(row=3, column=4, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_24 = tk.Button(frame, width=6, height=2, text=button24_text, font=("Roboto", "20"), bg=color_even_bg, fg="yellow")
        button_24.grid(row=3, column=5, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

        button_25 = tk.Button(frame, width=6, height=2, text=button25_text, font=("Roboto", "20"), bg=color_odd_bg, fg="blue")
        button_25.grid(row=4, column=0, columnspan=1, padx=(25,5), pady=5, ipadx=10, ipady=10)
        button_26 = tk.Button(frame, width=6, height=2, text=button26_text, font=("Roboto", "20"), bg=color_odd_bg, fg="green")
        button_26.grid(row=4, column=1, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_27 = tk.Button(frame, width=6, height=2, text=button27_text, font=("Roboto", "20"), bg=color_odd_bg, fg="red")
        button_27.grid(row=4, column=2, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_28 = tk.Button(frame, width=6, height=2, text=button28_text, font=("Roboto", "20"), bg=color_odd_bg, fg="cyan")
        button_28.grid(row=4, column=3, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_29 = tk.Button(frame, width=6, height=2, text=button29_text, font=("Roboto", "20"), bg=color_odd_bg, fg="magenta")
        button_29.grid(row=4, column=4, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)
        button_30 = tk.Button(frame, width=6, height=2, text=button30_text, font=("Roboto", "20"), bg=color_odd_bg, fg="yellow")
        button_30.grid(row=4, column=5, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

        button_31 = tk.Button(frame, width=18, height=2, text=button31_text, font=("Roboto", "20"), bg=color_even_bg, fg="yellow")
        button_31.grid(row=5, column=0, columnspan=3, padx=5, pady=5, ipadx=10, ipady=10)
        label_0 = tk.Label(frame, width=18, height=2, text=label0_text, font=("Roboto", "20"), bg=color_label_bg)
        label_0.grid(row=5, column=3, columnspan=3, padx=5, pady=5, ipadx=10, ipady=10)

        # Left Mouse Button
        button_1.bind("<Button-1>", push_button1)
        button_2.bind("<Button-1>", push_button2)
        button_3.bind("<Button-1>", push_button3)
        button_4.bind("<Button-1>", push_button4)
        button_5.bind("<Button-1>", push_button5)
        button_6.bind("<Button-1>", push_button6)
        button_7.bind("<Button-1>", push_button7)
        button_8.bind("<Button-1>", push_button8)
        button_9.bind("<Button-1>", push_button9)
        button_10.bind("<Button-1>", push_button10)
        button_11.bind("<Button-1>", push_button11)
        button_12.bind("<Button-1>", push_button12)
        button_13.bind("<Button-1>", push_button13)
        button_14.bind("<Button-1>", push_button14)
        button_15.bind("<Button-1>", push_button15)
        button_16.bind("<Button-1>", push_button16)
        button_17.bind("<Button-1>", push_button17)
        button_18.bind("<Button-1>", push_button18)
        button_19.bind("<Button-1>", push_button19)
        button_20.bind("<Button-1>", push_button20)
        button_21.bind("<Button-1>", push_button21)
        button_22.bind("<Button-1>", push_button22)
        button_23.bind("<Button-1>", push_button23)
        button_24.bind("<Button-1>", push_button24)
        button_25.bind("<Button-1>", push_button25)
        button_26.bind("<Button-1>", push_button26)
        button_27.bind("<Button-1>", push_button27)
        button_28.bind("<Button-1>", push_button28)
        button_29.bind("<Button-1>", push_button29)
        button_30.bind("<Button-1>", push_button30)
        button_31.bind("<Button-1>", push_button31)

        button_1.bind("<ButtonRelease-1>", release_button1)
        button_2.bind("<ButtonRelease-1>", release_button2)
        button_3.bind("<ButtonRelease-1>", release_button3)
        button_4.bind("<ButtonRelease-1>", release_button4)
        button_5.bind("<ButtonRelease-1>", release_button5)
        button_6.bind("<ButtonRelease-1>", release_button6)
        button_7.bind("<ButtonRelease-1>", release_button7)
        button_8.bind("<ButtonRelease-1>", release_button8)
        button_9.bind("<ButtonRelease-1>", release_button9)
        button_10.bind("<ButtonRelease-1>", release_button10)
        button_11.bind("<ButtonRelease-1>", release_button11)
        button_12.bind("<ButtonRelease-1>", release_button12)
        button_13.bind("<ButtonRelease-1>", release_button13)
        button_14.bind("<ButtonRelease-1>", release_button14)
        button_15.bind("<ButtonRelease-1>", release_button15)
        button_16.bind("<ButtonRelease-1>", release_button16)
        button_17.bind("<ButtonRelease-1>", release_button17)
        button_18.bind("<ButtonRelease-1>", release_button18)
        button_19.bind("<ButtonRelease-1>", release_button19)
        button_20.bind("<ButtonRelease-1>", release_button20)
        button_21.bind("<ButtonRelease-1>", release_button21)
        button_22.bind("<ButtonRelease-1>", release_button22)
        button_23.bind("<ButtonRelease-1>", release_button23)
        button_24.bind("<ButtonRelease-1>", release_button24)
        button_25.bind("<ButtonRelease-1>", release_button25)
        button_26.bind("<ButtonRelease-1>", release_button26)
        button_27.bind("<ButtonRelease-1>", release_button27)
        button_28.bind("<ButtonRelease-1>", release_button28)
        button_29.bind("<ButtonRelease-1>", release_button29)
        button_30.bind("<ButtonRelease-1>", release_button30)
        button_31.bind("<ButtonRelease-1>", release_button31)

        gpio.output(clock_button, 1)
        self.__root.mainloop()

    def __del__(self):
        print(version_info + ": END")

argv = sys.argv

if len(argv) == 1:
    time_delay = 0.01 # 10 Milliseconds
else:
    time_delay = float(argv[1])

print(sys.version)

gpio.setmode(gpio.BCM)

list_gpio_output = [13,16,19,20,21,26]
gpio.setup(list_gpio_output, gpio.OUT)

def handle_sigint(signum, frame):
    print(version_info + ": Force Stop")
    gpio.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

root = tk.Tk()
gui = GraphicalInterface(root)
del gui
gpio.cleanup()

