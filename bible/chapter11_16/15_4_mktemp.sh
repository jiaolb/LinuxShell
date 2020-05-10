#!/bin/bash 

echo "1.>>>> creating local tmp file"
tempfile=$(mktemp 15_4.XXXXXX) 

exec 3>$tempfile 

echo "This script writes to local temp file $tempfile" 
echo "This is the first line" >&3 
echo "This is the second line." >&3 
echo "This is the last line." >&3 

exec 3>&- 

echo "Done creating temp file. The contents are:" 

cat $tempfile 

rm -f $tempfile 2> /dev/null

echo "2.>>>> creating /tmp/ tmp file"
tmpfile=$(mktemp -t 15_4.XXXXXX)

exec 3>$tmpfile 

echo "This script writes to /tmp temp file $tmpfile" 
echo "This is the first line1" >&3 
echo "This is the second line1." >&3 
echo "This is the last line1." >&3 

exec 3>&- 

echo "Done creating temp file. The contents are:" 

cat $tmpfile 

rm -f $tmpfile 2> /dev/null
