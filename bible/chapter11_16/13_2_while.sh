#!/bin/bash

echo "1.test while-do-done"

m=1

while test $m -lt 10 
do
    m=$[$m + 1]
	echo $m
done

echo "2.test while more cond"

m=1

while [ $m -lt 10 ]
	[ $m -lt 5 ]
do
    m=$[$m + 1]
	echo $m
done



