#!/bin/bash

echo "1.test for-in-do-done"

echo ">>for m in x y z; print m"

n="x y z"

for m in $n; do
	echo $m
done

echo "2.test command"

echo ">>for m in \$(ls); print m"

for m in $(ls "../"); do
	echo $m
done

echo "3.test IFS"
echo ">>IFS=$:; str=abc;123:890;.."

str="abc;123:890;..\""

IFS_OLD=$IFS
IFS=$'\n'':'';'

count=0

for m in $str
do
	echo str is $m
done

IFS=$IFS_OLD

echo "4.test for C style"
echo "print 1-10: for (( m = 1; m <= 10; m++ ))"

for (( m = 1; m <= 10; m++ ))
do
	echo -n $m
done
echo

