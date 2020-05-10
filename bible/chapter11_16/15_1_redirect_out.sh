#!/bin/bash

echo "1. exec 3>15_1.file"

exec 3>15_1.file

echo "test echo 1"
echo "test echo 2 >&3" >&3
echo "test echo 3"

echo ">>>>cat 15_1.file"

cat 15_1.file

echo 
echo "2. exec 3&>1; exec 1>15_1.file; ... exec 1&>3"

exec 3>&1
exec 1>15_1.file1

# ->1 ->file1
echo "test echo 2.1"
echo "test echo 2.2"

exec 1>&3

# ->1->3->1 -> LCD
echo "test echo 2.3"

echo ">>>>cat 15_1.file1"
cat 15_1.file1

rm 15_1.file 15_1.file1

