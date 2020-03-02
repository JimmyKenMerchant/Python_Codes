# DMX512

License: BSD-3-Clause

**PURPOSE**

* DMX512 is aimed to use for DMX512 Transmitter Test (dmx512_tx_test) in Kenta Ishii's project on Raspberry Pi (RasPi), [Aloha Operating System (Aloha OS)](https://github.com/JimmyKenMerchant/RaspberryPi).

**USAGE**

* Connect GPIO on RasPi with Raspbian and GPIO on RasPi with dmx512_tx_test. Make sure to connect GND on each RasPi because the difference of voltage on each GND makes incorrect detecting logical high or low.

* First, power on RasPi with dmx512_tx_test, then execute dmx512*.py. Otherwise, the RasPi doesn't receive commands for its initialization.

* GPIO12 as Clock OUT, Connect to GPIO27 (Clock IN for Buttons) of dmx512_tx_test

* GPIO16 as Bit[0], Connect to GPIO22 (Parallel Bus Bit[0]) of dmx512_tx_test

* GPIO19 as Bit[1], Connect to GPIO23 (Parallel Bus Bit[1]) of dmx512_tx_test

* GPIO20 as Bit[2], Connect to GPIO24 (Parallel Bus Bit[2]) of dmx512_tx_test

* GPIO21 as Bit[3], Connect to GPIO25 (Parallel Bus Bit[3]) of dmx512_tx_test

* GPIO26 as Bit[4], Connect to GPIO26 (Parallel Bus Bit[4]) of dmx512_tx_test

* GPIO6 as Busy Toggle IN, Connect to GPIO15 of dmx512_tx_test

* GPIO13 as EOP (End of Packet) Toggle IN, Connect to GPIO16 of dmx512_tx_test

**COMPATIBILITY**

* Raspbian GNU/Linux 10 (buster) and Python 3.7.3
