import time
import network
import urequests as requests
import dht
from machine import Pin

#inisialisasi
sensor = dht.DHT22(Pin(13))
led = Pin("LED", Pin.OUT)
led.off()
ssid = 'tws@IOT'
password = ''
url = ""

#connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
  if wlan.status() < 0 or wlan.status() >=3:
    break
  max_wait -= 1
  print('waiting for connection...')
  time.sleep(1)

if wlan.status() != 3:
  print('network connection failed')
else:
  led.on()
  print('connected')
  time.sleep(2)
  led.off()
  time.sleep(2)

while True:
  try:
    led.on()
    print('sending...')
    sensor.measure()
    temperature = sensor.temperature() 
    humidity = sensor.humidity()
    response = requests.post(url, )
    text = response.text
    print(text)
    response.close()
    time.sleep(15)
  except:
    led.off()
    print("could not connect (status = " + str(wlan.status()) + ")")
    if wlan.status() < 0 or wlan.status >= 3:
      print('try to reconnect...')
      wlan.disconnect()
      time.sleep(1)
      wlan.connect(ssid, password)
      if wlan.status() == 3:
        led.on()
        print('connected')
        time.sleep(2)
        led.off()
        time.sleep(2)
      else:
        print('failed')
  
  time.sleep(5)
