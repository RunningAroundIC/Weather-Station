import datetime as dt
import bme280_sensor as bme
import DS18B20_sensor as DS

celcius = "°C"
humidity = "% rH"
pressure = "hPa"

def roundNumber(number):
	return round(number,2);

#print(bme.getAllData())
print(roundNumber(bme.getTemprature()), celcius)
#print(bme.getHumidity())
#print(bme.getPressure())
print(roundNumber(DS.readTemprature()), celcius)

