#!/bin/bash

echo you input number is $1

case $1 in
1 | 2 | 3)
	echo case 1 testing...;;
a | b | c)
	echo case 2 testing...;;
*)
	echo unknown case...;;
esac
