import smbus2
import bme280
import bme280.const as oversampling

port = 1
address = 0x77
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus, address)

# Oversampling modes
sampling1 = oversampling.x1
sampling2 = oversampling.x2
sampling3 = oversampling.x4
sampling4 = oversampling.x8
sampling5 = oversampling.x16


def getAllData():
	data = bme280.sample(bus, address, sampling3)
	return data

def getTemprature():
	data = bme280.sample(bus, address, sampling3)
	return data.temperature

def getPressure():
	data = bme280.sample(bus, address, sampling3)
	return data.pressure

def getHumidity():
	data = bme280.sample(bus, address, sampling3)
	return data.humidity

def getTimeStamp():
	data = bme280.sample(bus, address, sampling1)
	return data.timestamp

def getId():
	data = bme280.sample(bus, address, sampling1)
	return data.id
