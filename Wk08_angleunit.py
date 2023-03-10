from m5stack import *
from time import *
from machine import Pin, ADC
from servo import Servo
from easyIO import *
import wifiCfg
from m5mqtt import M5mqtt


analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog input on analog_pin
adc.atten(ADC.ATTN_11DB)  # enable full-range on ADC

wifiCfg.doConnect('ACCD','tink1930') # ACCD wifi info
mqtt_feed = M5mqtt (
    'testclient',
    'io.adafruit.com',
    1883,
    'robinkeum',
    'aio_LbYm78wxPg3C9wqL2TpYn5Lp3mDz',
    300
    )
mqtt_feed.start()


while True:
    analog_val = adc.read() # read analog value (0-4995 range)
    print(analog_val)
    mqtt_feed.publish('robinkeum/feeds/testfeed', str(analog_val))
    sleep_ms(3000)