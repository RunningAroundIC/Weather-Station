import time

#the number after "28-" need to changed out with your sensor's number.
DS18B20 =("/sys/bus/w1/devices/28-051693f345ff/w1_slave")

def rawRead():
	raw = open(DS18B20)
	data = raw.readlines()
	raw.close()
	return data

def readTemprature():
	data = rawRead()
	
	while data[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		data = rawRead()
	
	tEquals = data[1].find('t=')

	if tEquals != -1:
		tempratureValue = data[1][tEquals+2:]
		tempratureCelsius = float(tempratureValue) / 1000
		return tempratureCelsius
