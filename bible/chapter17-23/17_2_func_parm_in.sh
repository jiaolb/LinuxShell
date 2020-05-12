#!/bin/bash

function func1 { 
 echo $[ $1 * $2 ] 
}

if [ $# -eq 2 ] 
then 
	value=$(func1 $1 $2) 
	echo "The result is $value" 
else 
	echo "Usage: badtest1 a b" 
fi

