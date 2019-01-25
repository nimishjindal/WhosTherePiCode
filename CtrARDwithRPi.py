from nanpy import (arduinoApi, SerialManager)
from time import sleep

ledpin = 13

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)

except:
    print("failed connection")


a.pinMode(ledpin, a.OUTPUT)

try:
    while True:
        a.digitalWrite(ledpin, a.HIGH)
        print("on")

        sleep(1)

        a.digitalWrite(ledpin, a.LOW)
        print("off")

        sleep(1)
except:
    a.digitalWrite(ledpin, a.LOW)
