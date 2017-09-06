#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

def my_callback(channnel):
    global ledState

    if channnel==14:
        # GPIO.LOWだったらHIGHに GPIO.HIGHだったらLOWに変更する
        ledState = not ledState
        print ledState

        GPIO.output(15, ledState)


GPIO.setmode(GPIO.BCM)
# initial = GPIO.LOWとすることでプログラム実行時にLEDのが消灯された状態になる
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14, GPIO.RISING, callback=my_callback, bouncetime=200)

ledState = GPIO.LOW

# プログラムが終了しないように無限ループさせている
try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass


GPIO.cleanup()
