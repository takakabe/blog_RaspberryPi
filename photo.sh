#!/bin/bash

raspistill -vf -hf -o /home/pi/raspberry_bot/scripts/wawawa.jpg
curl -F file=@/home/pi/raspberry_bot/scripts/wawawa.jpg -F channels=CHANNELID -F token=xoxb-000000000000-XXXXXXXXXXXXXXXXXXXXXXXX https://slack.com/api/files.upload

