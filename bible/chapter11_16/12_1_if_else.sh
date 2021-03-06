#!/bin/bash

echo input is $1

#test expression == [ expression ]

# n1 -eq n2 检查n1是否与n2相等
# n1 -ge n2 检查n1是否大于或等于n2
# n1 -gt n2 检查n1是否大于n2
# n1 -le n2 检查n1是否小于或等于n2
# n1 -lt n2 检查n1是否小于n2
# n1 -ne n2 检查n1是否不等于n2

if test $1 -eq 1; then
	echo test case 1

# str1 = str2 检查str1是否和str2相同
# str1 != str2 检查str1是否和str2不同
# str1 < str2 检查str1是否比str2小
# str1 > str2 检查str1是否比str2大
# -n str1 检查str1的长度是否非0 
# -z str1 检查str1的长度是否为0
elif [ $1 = "abc" ] || [ $1 = "xyz" ]; then
	echo test case 2

# -d file 检查file是否存在并是一个目录
# -e file 检查file是否存在
# -f file 检查file是否存在并是一个文件
# -r file 检查file是否存在并可读
# -s file 检查file是否存在并非空
# -w file 检查file是否存在并可写
# -x file 检查file是否存在并可执行
# -O file 检查file是否存在并属当前用户所有
# -G file 检查file是否存在并且默认组与当前用户相同
# file1 -nt file2 检查file1是否比file2新
# file1 -ot file2 检查file1是否比file2旧
elif [ -f $1 ]; then
	echo test case 3

else
	echo please input case:
	echo "case1=1"
	echo "case2=abc"
	echo "case3=12_1_if_else.sh"
fi
