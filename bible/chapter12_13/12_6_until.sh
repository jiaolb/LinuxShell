#!/bin/bash

echo "1.test until-do-done"

m=1

until test $m -gt 10
do
	m=$[$m + 1]
	echo $m
done

echo "2.test until more cond"

m=1

until [ $m -gt 10 ]
	[ $m -eq 10 ]
do
	m=$[$m + 1]
	echo $m
done


