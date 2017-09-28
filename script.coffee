module.exports = (robot) ->
  robot.respond /写真/, (msg) ->
    @exec = require('child_process').exec
    command = "/home/pi/raspberry_bot/scripts/photo.sh"
    msg.send "Command: #{command}"
    @exec command, (error, stdout, stderr) ->
      @msg.send error if error?
      #msg.send stdout if stdout?
      #@msg.send stderr if stderr?

