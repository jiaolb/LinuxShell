#!/bin/bash

count=1

while [ -n "$1" ]
do
	echo "param #$count is $1"
	count=$[$count + 1]
	shift 1
done

