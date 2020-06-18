#!/bin/bash

echo "hello, you are /boy!" | sed -n 's/boy/good boy/p'

echo "hello, you are /boy!" | sed -n 's/\/boy/good boy/p'


