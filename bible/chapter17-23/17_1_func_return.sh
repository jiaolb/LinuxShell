#!/bin/bash

echo "1.>>>> test default return value"

function func1 {
	echo "hello function 1: who"
	who
}

func1
echo "test func1 return value $?"

echo "2.>>>> test 'return' return value (int 0-255)"

function func2 {
	echo "hello function 2: who"
	date
	return 2
}

func2
echo "test func2 return value $?"

echo "3.>>>> test 'echo ' return value"

function dbl { 
 read -p "Enter a value: " value 
 echo $[ $value * 2 ] 
} 
result=$(dbl) 
echo "The new value is $result"
