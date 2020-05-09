#!/bin/bash

echo ">>all data"
for m in 10 20 30 40 50; do
	echo $m
	for n in 11 12 13; do
		echo -n "$n -- "
	done
	echo
done 

echo "1.test break "

echo ">>break"

for m in 10 20 30 40 50; do
	echo $m
	for n in 11 12 13; do
		echo -n "$n -- "
		break
	done
	echo
done 

echo ">>break 2"

for m in 10 20 30 40 50; do
	echo $m
	for n in 11 12 13; do
		echo -n "$n -- "
		break 2
	done
	echo
done 

echo

echo "2.test continue"

echo ">>continue"

for m in 10 20 30 40 50; do
	echo $m
	for n in 11 12 13; do
		continue
		echo -n "$n -- "
	done
	echo
done 

echo "continue2"

for m in 10 20 30 40 50; do
	echo $m
	for n in 11 12 13; do
		continue 2
		echo -n "$n -- "
	done
	echo
done 

