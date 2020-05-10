#!/bin/bash 

# testing input/output file descriptor

touch 15_3.file

exec 3<> 15_3.file 
echo "This is a test line1" >&3
read line <&3 
echo "Read: $line" 
echo "This is a test line2" >&3

echo ">>>>cat file"
cat 15_3.file

exec 3>&-

rm 15_3.file
