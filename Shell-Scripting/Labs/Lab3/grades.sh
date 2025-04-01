#!/bin/bash


echo "Please type in your grade as number between 0 and 100:"

read grade

if [ "${grade}" -ge 90 -a "${grade}" -le 100 ];
then
	echo "Grade is A"
fi
if [ "${grade}" -ge 80 -a "${grade}" -le 89 ];
then
        echo "Grade is B"
fi
if [ "${grade}" -ge 70 -a "${grade}" -le 79 ];
then
	echo "Grade is C"
fi
if [ "${grade}" -ge 60 -a "${grade}" -le 69 ];
then
        echo "Grade is D"
fi
if [ "${grade}" -le 60 ];
then
        echo "Grade is F"
fi
