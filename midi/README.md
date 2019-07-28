# JACK Audio Connection Kit to Serial Interface Bridge

**Purpose**

* Connector Between JACK MIDI and Serial Interface Written by Python
	* JACK Audio Connection Kit is an audio I/O controller (sound driver), which connects between physical/software audio devices.
	* JACK MIDI shows physical/software MIDI devices which drive with JACK libraries (API), which can be written by Python.
	* ALSA is a sound driver, which controls sound cards, MIDI devices, etc. It's a part of Linux kernel.
	* ALSA MIDI shows physical/software MIDI devices which drive with ALSA libraries (API).
	* a2jmidid is a connector between ALSA MIDI and JACK MIDI.
	* Serial Interface is a UART peripheral, which is also used as a part of MIDI physical.
	* Serial Interface can also be controlled by Python.
	* So I decided to make this project with Python, a well-known language.

**Caution**

* The baud rate of UART in MIDI is 31250 baud rate. However, in this README, UART is set with 115200 baud rate. You can see the MIDI connectors and jacks, which is needed to be DIY. I suppose this project is used with [my Raspberry Pi project](https://github.com/JimmyKenMerchant/RaspberryPi).

**Usage on Raspbian (One of Linux Distributions)**

* Make sure to enable UART through `sudo raspi-config`: 5 Interfacing Options > P6 Serial > No (serial login shell) > Yes (serial interface) > OK > Finish (Reboot)

* I recommend that you add `dtoverlay=pi3-miniuart-bt` and `core_freq=250` in /boot/config.txt to enable serial0 on RasPi with the wireless module. In case, there is `dtoverlay=pi3-disable-bt` which disables Bluetooth.

* Install Linux Softwares

```bash
# Install QjackCtl (Audio I/O Control), a2jmidid (ALSA MIDI to JACK MIDI Bridege), jack-keyboard (Software Keyboard), Qtractor (MIDI Sequencer)
sudo apt-get install qjackctl a2jmidid jack-keyboard qtractor
```

* Install jackclient-python and pyserial, Python3 Libraries

```bash
# Check List of Libraries
python3 -m pip list

# Install Jack-Client If Not in List
python3 -m pip install JACK-Client --user

# Install pyserial If Not in List
python3 -m pip install pyserial --user
```

* Open QjackCtl (GUI) and "Start"

```bash
# jackd -d alsa
qjackctl
# Push "Start"
```

* To bridge ALSA MIDI (System MIDI) and JACK MIDI, add `a2jmidid -e &` in QjackCtl (go to "Setup" and select "Options" tab. Check "Execute script after Startup", and write `a2jmidid -e &` in the textbox). You can check MIDI ports, such as USB MIDI keyboard, in "a2j" at "MIDI" tab of "Connections" menu (USB MIDI keyboard can be checked in the left side box, "Readable Clients / Output Ports").

* Install This Project and Run

```bash
cd ~/Desktop
git clone https://github.com/JimmyKenMerchant/Python_Codes
cd Python_Codes/midi
chmod u+x midi2serial.py
# Check Arguments
./midi2serial.py -h
# In this case, the baud rate of UART is 115200 bps, 11520 bytes per second; UART needs 2 bits for start and stop bits.
# 0.01 (seconds) is read timeout value (3rd argument)
./midi2serial.py -s /dev/serial0 -b 115200 -t 0.01
```

* Back to QjackCtl, click "Connect" button to go to "Connections" menu, and select "MIDI" tab. You can check "MIDI-TO-SERIAL" in the right side box, "Writable Clients / Input Ports".

* Select both a port you want to connect in "Readable Clients / Output Ports" and "MIDI-TO-SERIAL" in "Writable Clients / Input Ports", then click "Connect" button. A line will be drawn to show the connection of two ports.

* For example, run jack-keyboard, then connect "midi_out" of "jack-keyboard" in "Readable Clients / Output Ports" and "input" of "MIDI-TO-SERIAL" in "Writable Clients / Input Ports".

* (Optional) Psuedo polyphonic (PPP) function
	* Psuedo polyphonic function sends MIDI message to an inactive monophonic device to make a chord on a device, such as keyboard, etc.
	* If transit MIDI channel matches PPP channel, PPP function searches inactive monophonic devices.
	* The MIDI channel is changed from PPP channel to PPP channel + device ID number if any inactive monophonic device is searched.
	* Device ID numbers are assigned from 1 to the number of monophonic devices in this program.
	* Monophonic devices need to be set these own channels from the next of PPP channel in advance.

```bash
# In this case, enable PPP (4th argument), PPP channel is set to 1 (5th argument), and the number of monophonic devices is 3 (6th argument).
# If Baud Rate Is 115200, I Recommend that you apply up to 3 devices
# because 115200 includes 3 times as many as 31250, MIDI Baud Rate.
./midi2serial.py -s /dev/serial0 -b 115200 -t 0.01 -p -c 1 -n 3
```

**Information about Licenses**

* License of This Project: 3-Clause BSD License

* [JACK Audio Connection Kit (JACK) Client for Python: Copyright (c) 2014-2015 Matthias Geier, MIT](https://jackclient-python.readthedocs.io)

* [pySerial: Copyright (C) 2001-2017 Chris Liechti <cliechti@gmx.net>, 3-Clause BSD License](https://pythonhosted.org/pyserial/)
