import eeml
import eeml.datastream
import eeml.unit
import serial
import datetime
import os 
import serial
import smbus 
import time 

# parameters
API_KEY = 'Zt_ML6lnexokABX5rUtxnQhwBKiSAKxIMmRiaExlVytlUT0g'
# API_URL = '/v2/feeds/119037.xml'
API_URL = 119078

#open i2c bus
i2c = smbus.SMBus(0)
#address with pins low 
address = 0x10
dat = 20
addrl =10
addrh = 5 



while True:
  a = i2c.read_word_data(address,0)


	pac = eeml.datastream.Cosm(API_URL, API_KEY)
	at = datetime.datetime(2012, 9, 12, 11, 0, 0)

	pac.update([
        	eeml.Data(0, a, tags=('Temperature',), unit=eeml.unit.Celsius()),
        	eeml.Data(1, a, tags=('Humidity',), unit=eeml.unit.RH())])
	pac.put()
	print(pac.geteeml())
	time.sleep(30)
