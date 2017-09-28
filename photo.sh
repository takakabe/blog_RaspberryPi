raspistill -vf -hf -o /home/pi/raspberry_bot/scripts/wawawa.jpg
curl -F file=@/home/pi/raspberry_bot/scripts/wawawa.jpg -F channels=C6R8F8SGL -F token=xoxb-248950932854-tiJxmBvFvki6PSAigTV2V4Ji https://slack.com/api/files.upload
#curl -F file=@/home/pi/raspberry_bot/scripts/wawawa.jpg -F channels=C3XDJAEKY -F token=xoxb-248950932854-tiJxmBvFvki6PSAigTV2V4Ji https://slack.com/api/files.upload

