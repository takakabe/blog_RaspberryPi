module.exports = (robot) ->
  robot.respond /写真/, (msg) ->
    @exec = require('child_process').exec
    command = "raspistill -vf -hf -o /home/pi/raspberry_bot/scripts/wawawa.jpg;
      curl -F file=@/home/pi/raspberry_bot/scripts/wawawa.jpg -F channels=C6R8F8SGL -F token=xoxb-248950932854-tiJxmBvFvki6PSAigTV2V4Ji https://slack.com/api/files.upload"
    #msg.send "Command: #{command}"
    msg.send "しゃしんとってるよ。ちょっとまってね。"
    @exec command, (error, stdout, stderr) ->
      @msg.send error if error?
      #msg.send stdout if stdout?
      #@msg.send stderr if stderr?

