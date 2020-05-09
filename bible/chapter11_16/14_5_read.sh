#!/bin/bash

echo "1.test read"

echo -n "Enter you name: "
read name

echo "hello $name, welcome!"

echo "2.test read -p -t -n"

read -n2 -t 3 -p "Enter you age: "

echo "age: $REPLY years"

echo "3.test read -s"

read -s -p "Enter you password:" password

echo "password : $password"

echo "4.test read file"

count=1
cat 14_2_shift.sh | while read line
do
	echo "#$count $line"
	count=$[$count + 1]
done
