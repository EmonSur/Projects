#!/bin/bash

echo "Type in duration of timer wanted: "
read time

while [ $time -gt 0 ]; do
	echo "Countdowm: $time seconds remaining"
	sleep 1
	time=$(($time - 1))
done

echo "Countdown: Time's Up!"
