#!/bin/bash

echo "hello world!"
echo "hello \"world\" "

# 文本颜色是由对应的色彩码来描述的。其中包括：
# 重置=0，黑色=30，红色=31，绿色=32，黄色=33，蓝色=34，洋红=35，青色=36，白色=37。

echo -e "\e[1;31m This is red text \e[0m"

# 对于彩色背景，经常使用的颜色码是：
# 重置=0，黑色=40，红色=41，绿色=42，黄色=43，蓝色=44，洋红=45，青色=46，白色=47

echo -e "\e[1;42m Green Background \e[0m"

