from machine import Pin
import network
import time
import wifi
import server
import _thread
from firebase import refresh_token, write_temp

led = Pin('LED', Pin.OUT)

if wifi.connect():
    led.on()
    print('Successfully connected to Wifi')
else:
    led.off()
    print('Error connecting to Wifi')


def run_server():
    while True:
        print('Hello')


print(_thread.start_new_thread(run_server, ()))
print('After')
uid, token = refresh_token()
print(uid, token)
temp = 0
while True:
    print(write_temp(token, uid, temp))
    temp += 1
