#!/bin/bash
while true
do
	echo 1 > /sys/class/gpio/gpio2/value
	echo 'echo 1 > /sys/class/gpio/gpio2/value'
	sleep 1

	echo 0 > /sys/class/gpio/gpio2/value
	echo 'echo 0 > /sys/class/gpio/gpio2/value'
	sleep 1
done
