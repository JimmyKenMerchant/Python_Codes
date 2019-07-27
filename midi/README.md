# JACK Audio Connection Kit to Serial Interface Bridge

**Usage on Raspbian (One of Linux Distributions)**

* Make sure to enable UART through `sudo raspi-config`: 5 Interfacing Options > P6 Serial > No (serial login shell) > Yes (serial interface) > OK > Finish (Reboot)

* I recommend that you add `dtoverlay=pi3-miniuart-bt` and `core_freq=250` in /boot/config.txt to enable serial0 on RasPi with the wireless module.

* Install jackclient-python and pyserial

```bash
# Install QjackCtl and a2jmidid
sudo apt-get install qjackctl a2jmidid

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

* If you want to bridge ALSA MIDI (System MIDI) and JACK MIDI, add `a2jmidid -e &` in QjackCtl (go to "Setup" and select "Options" tab. Check "Execute script after Startup", and write `a2jmidid -e &` in the textbox). You can check MIDI ports, such as USB MIDI keyboard, in "a2j" at "MIDI" tab of "Connections" menu (USB MIDI keyboard can be checked in the left side box, "Readable Clients / Output Ports").

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
