#!/usr/bin/python
# I2C test program for RPi
# This will write one byte and then read it back to the screen

#i2c setup instructions for the pi
# allow i2c by removing from this blacklist
# sudo nano /etc/modprobe.d/raspi-blacklist.conf 

# add ic2-dev to end of this file
# sudo nano /etc/modules

# needs python-smbus, install it like this:
# sudo apt-get update
# sudo apt-get install i2c-tools
# sudo apt-get install python-smbus
# sudo adduser pi i2c
# sudo reboot -n

#not needed anymore if above worked
# sudo modprobe i2c-dev


import smbus
import time

# open Linux device /dev/ic2-0
i2c = smbus.SMBus(1)

#24c64 address with address pins low
address = 0x10
dat = 20
addrl = 10
addrh = 5


while True:
  i2c.write_word_data(address, 0x34, 0)
	time.sleep (1)
	i2c.write_word_data(address,0x34, 1)
	time.sleep (1)





d = i2c.read_word_data(address, 0)
print d
#time.sleep (0.1)
#d = i2c.read_word_data(address, 1)
#print d
#time.sleep (0.1)
#d = i2c.read_word_data(address, 2)
#print d
#time.sleep (0.1)
#d = i2c.read_word_data(address, 3)
#print d
#time.sleep (0.1)
#d = i2c.read_word_data(address, 4)
#print d
#time.sleep (0.1)
#d = i2c.read_word_data(address, 5)
#print d

