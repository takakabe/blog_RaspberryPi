#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # 初期設定
GPIO.setup(15,GPIO.OUT) # 出力設定
GPIO.setup(14,GPIO.IN)  # 入力設定

# タクトスイッチの状態をもとに判定する
# 押す=HIGH はなす=LOW
while True:
    if GPIO.input(14) == GPIO.HIGH:
        GPIO.output(15,GPIO.HIGH) # LED点灯
    else:
        GPIO.output(15,GPIO.LOW)  # LED消灯

GPIO.cleanup() # GPIO初期化
