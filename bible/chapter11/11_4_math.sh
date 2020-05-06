#!/bin/bash

echo "1.expr expression  ---------------------"

# ARG1 | ARG2  如果ARG1既不是null也不是零值，返回ARG1；否则返回ARG2
# ARG1 & ARG2  如果没有参数是null或零值，返回ARG1；否则返回0
# ARG1 < ARG2  如果ARG1小于ARG2，返回1；否则返回0
# ARG1 <= ARG2 如果ARG1小于或等于ARG2，返回1；否则返回0
# ARG1 = ARG2  如果ARG1等于ARG2，返回1；否则返回0
# ARG1 != ARG2 如果ARG1不等于ARG2，返回1；否则返回0
# ARG1 >= ARG2 如果ARG1大于或等于ARG2，返回1；否则返回0
# ARG1 > ARG2  如果ARG1大于ARG2，返回1；否则返回0
# ARG1 + ARG2  返回ARG1和ARG2的算术运算和
# ARG1 - ARG2  返回ARG1和ARG2的算术运算差
# ARG1 * ARG2  返回ARG1和ARG2的算术乘积
# ARG1 / ARG2  返回ARG1被ARG2除的算术商
# ARG1 % ARG2  返回ARG1被ARG2除的算术余数
# STRING : REGEXP     如果REGEXP匹配到了STRING中的某个模式，返回该模式匹配
# match STRING REGEXP 如果REGEXP匹配到了STRING中的某个模式，返回该模式匹配
# substr STRING POS LENGTH 返回起始位置为POS（从1开始计数）、长度为LENGTH个字符的子字符串
# index STRING CHARS  返回在STRING中找到CHARS字符串的位置；否则，返回0
# length STRING       返回字符串STRING的数值长度
# + TOKEN             将TOKEN解释成字符串，即使是个关键字
# (EXPRESSION)        返回EXPRESSION的值

echo "expr 1+5" = $(expr 1+5)
echo "expr 1 + 5" = $(expr 1 + 5)

m=$(expr 1 \| 5)
echo -n "m=\$(expr 1 \| 5); echo \$m" = 
echo $m

echo "expr 2 \* 5" = $(expr 2 \* 5)

echo "expr length \"abcdefg\"" = $(expr length "abcdefg")
echo "expr substr \"abcdefg\" 1 3" = $(expr substr "abcdefg" 1 3)
echo "expr index \"abcdefg\" e" = $(expr index "abcdefg" e)

echo "2.[expression] int type ---------------------"
echo "\$[100 + 5]" = $[100 + 5]
echo "\$[100 / (4 + 3)]" = $[100 / (4 + 3)]

echo "2.\$(echo \"options; expression\" | bc) float type ---------------------"

x=$(echo "scale=4; 3.44 / 5" | bc)
echo -n "\$(echo \"scale=4; 3.44 / 5\" | bc)" = 
echo $x

var1=10.46 
var2=43.67 
var3=33.2 
var4=71 
var5=$(bc << EOF 
scale = 4
a1 = ( $var1 * $var2)
b1 = $var3 * $var4)
a1 + b1
EOF
)

echo The final answer for this mess is $var5
