import RPi.GPIO as GPIO
import Adafruit_DHT
import time
  
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHTSensor = Adafruit_DHT.DHT11
  
# The pin which is connected with the sensor will be declared here
GPIO_Pin = 23
  
while True:
    humid, temper = Adafruit_DHT.read_retry(DHTSensor, GPIO_Pin)
    #print("Temperature: " + temper + "\n")
    print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temper, humid))
    time.sleep(3)
