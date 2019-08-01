# JACK Audio Connection Kit to Serial Interface Bridge (midi2serial)

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

* The baud rate of UART in MIDI is 31250 baud rate. However, in this README, UART is set with 115200 baud rate to drive midi2serial because of holding compatibility with microcontrollers. You can also see the MIDI plugs and jacks, MIDI IN and MIDI OUT schematics, which are needed to be DIY. I suppose this project is used with [my Raspberry Pi project](https://github.com/JimmyKenMerchant/RaspberryPi).

* I also recognize that you want DTM on Linux. You can install software MIDI Synths, e.g., ZynAddSubFx, FluidSynth, etc. These work with packages used in this project and show in the tabs of QjackCtl (these have to connect with the system in "Audio" tab to sound).

**Usage on Raspbian (One of Linux Distributions) with Raspberry Pi**

* Make sure to enable UART through `sudo raspi-config`: 5 Interfacing Options > P6 Serial > No (serial login shell) > Yes (serial interface) > OK > Finish (Reboot)

* I recommend that you add `dtoverlay=pi3-miniuart-bt` and `core_freq=250` in /boot/config.txt to enable serial0 on RasPi with the embedded wireless module, Zero W, 3B, etc. In case, there is `dtoverlay=pi3-disable-bt` which disables Bluetooth. Reboot to enable these parameters.

* Install Linux Packages

```bash
# Install QjackCtl (Audio I/O Control), a2jmidid (ALSA MIDI to JACK MIDI Bridege), jack-keyboard (Software Keyboard), Qtractor (MIDI Sequencer)
sudo apt-get install qjackctl a2jmidid jack-keyboard qtractor

# Optional Software Synths, FluidSynth Has to Set SoundFont to Sound
sudo apt-get install zynaddsubfx fluidsynth
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
# In this case, the baud rate of UART is 115200 bps, 11520 bytes per second (2nd argument);
# UART needs 2 bits for start and stop bits, plus 8 bits for data to transmit 1 byte.
# 0.01 (seconds) is the value of read timeout (3rd argument).
./midi2serial.py -s /dev/serial0 -b 115200 -t 0.01
```

* Back to QjackCtl, click "Connect" button to go to "Connections" menu, and select "MIDI" tab. You can check "MIDI-TO-SERIAL" in the right side box, "Writable Clients / Input Ports".

* Select both a port you want to connect in "Readable Clients / Output Ports" and "MIDI-TO-SERIAL" in "Writable Clients / Input Ports", then click "Connect" button. A line will be drawn to show the connection of two ports.

* For example, run jack-keyboard, then connect "midi_out" of "jack-keyboard" in "Readable Clients / Output Ports" and "input" of "MIDI-TO-SERIAL" in "Writable Clients / Input Ports".

* As another example, run Qtractor, then connect "Qtractor" of "a2j" in "Readable Clients / Output Ports" and "input" of "MIDI-TO-SERIAL" in "Writable Clients / Input Ports".

* (Optional) Pseudo polyphonic (PPP) function
	* PPP function sends multiple MIDI messages to monophonic (MIDI Mode 4) devices to make a chord.
	* If transit MIDI channel matches the PPP channel, PPP function searches inactive monophonic devices.
	* If any inactive monophonic device is searched, PPP channel is changed to PPP channel + the device ID number.
	* Device ID numbers are assigned from 1 to the number of monophonic devices.
	* Monophonic devices need to be set these own channels from the next of PPP channel in advance.

```bash
# In this case, enable PPP (4th argument), PPP channel is set to 1 (5th argument), and the number of monophonic devices is 3 (6th argument).
./midi2serial.py -s /dev/serial0 -b 115200 -t 0.01 -p -c 1 -n 3
```

**Information about Licenses**

* License of This Project: 3-Clause BSD License

* [JACK Audio Connection Kit (JACK) Client for Python: Copyright (c) 2014-2015 Matthias Geier, MIT](https://jackclient-python.readthedocs.io)

* [pySerial: Copyright (C) 2001-2017 Chris Liechti <cliechti@gmx.net>, 3-Clause BSD License](https://pythonhosted.org/pyserial/)
