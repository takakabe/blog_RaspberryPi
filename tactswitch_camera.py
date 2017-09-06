#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import subprocess

######################
# 関数 my_callback
######################
def my_callback(channnel):
        filename="wawawa.jpg"
        subprocess.Popen(['raspistill','-o',filename,'-t','1']) 


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO.RISING スイッチがおされたとき 
# bouncetime=300 一度イベントを検出したら300ミリ秒が次のイベントを検出しないよう設定
GPIO.add_event_detect(14, GPIO.RISING, callback=my_callback, bouncetime=300)


# プログラムが終了しないように無限ループさせている
try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass


GPIO.cleanup()
