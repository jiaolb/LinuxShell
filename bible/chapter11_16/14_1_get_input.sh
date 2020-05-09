#!/bin/bash

echo "\$* all is $*"
echo "\$@ is $@"
echo "\$# total is $#"

echo "\$0 script name is $0"

echo "\$(basename \$0) is $(basename $0)"

if [ -n "$1" ]; then
	echo "\$1 is $1"
else
	echo "\$1 is not present"
fi

echo "\${!#} last param is ${!#}"

count=1

for m in "$@"
do
	echo "param #$count is $m"
	count=$[$count + 1]
done


