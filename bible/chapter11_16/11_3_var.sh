#!/bin/bash

echo 1.use env variable:
echo UID: $UID

echo 2.care the '\$' $ \$ :
echo I has $15, you has \$12

echo 3.use user variable:

echo difine var=12345, Note: there is no space on either side of = !!!
var=12345
echo echo var is : $var

echo 4.use cmd in variable:
echo difine me=\'whoami\' or date=\$\(date\)
me='whoami'
you=$(date)

echo echo me: $me
echo echo date: $date
