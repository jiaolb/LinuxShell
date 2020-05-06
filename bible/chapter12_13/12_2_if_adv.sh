#!/bin/bash

echo "1.(( math expression ))"

# val++ 后增
# val-- 后减
# ++val 先增
# --val 先减
# ! 逻辑求反
# ~ 位求反
# ** 幂运算
# << 左位移
# >> 右位移
# & 位布尔和
# | 位布尔或
# && 逻辑和
# || 逻辑或

val1=10

if (( $val1 ** 2 > 90 )) 
then 
	(( val2 = $val1 ** 2 )) 
	echo "The square of $val1 is $val2" 
fi

echo "2.[[ str expression ]]"

if [[ $USER == jiao* ]] 
then 
 echo "Hello $USER" 
else 
 echo "Sorry, I do not know you" 
fi

