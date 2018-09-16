jack2serial.py: JACK Audio Connection Kit to Serial Interface Bridge

**Usage on Raspbian (One of Linux Distributions)**

* Install jackclient-python and pyserial

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

* Install This Project and Run

```bash
cd ~/Desktop
git clone https://github.com/JimmyKenMerchant/Python_Codes
cd Python_Codes/midi
# In this case, the baud rate of UART is 115200 bps, 11520 bytes per second; UART needs 2 bits for start and stop bits.
./midi2serial.py /dev/serial0 115200 0.01
```

* Back to QjackCtl, go to "Connect" and select "MIDI" tab. You can watch "MIDI-TO-SERIAL" in the right side box.

* If you want to bridge ALSA MIDI (System MIDI) and JACK MIDI, add `a2jmidid -e &` in QjackCtl (go to "Setup" and select "Options" tab. Check "Execute script after Startup", and write `a2jmidid -e &` in the textbox).

**Information about Licenses**

* License of This Project: 3-Clause BSD License

* [JACK Audio Connection Kit (JACK) Client for Python: Copyright (c) 2014-2015 Matthias Geier, MIT](https://jackclient-python.readthedocs.io)

* [pySerial: Copyright (C) 2001-2017 Chris Liechti <cliechti@gmx.net>, 3-Clause BSD License](https://pythonhosted.org/pyserial/)