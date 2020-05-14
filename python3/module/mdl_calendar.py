#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar as cld

#calendar.calendar(year,w=2,l=1,c=6)
#返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 
#每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数
print (cld.calendar(2017, 1, 2, 2))
cld.prcal(2017, 1, 1, 3) # = print cld.calendar(2017, 1, 1, 3)

#返回一个多行字符串格式的year年month月日历，两行标题，一周一行
cal = cld.month(2017, 4, 1, 1)
print ('\n', u'2017年4月份的日历:')
print (cal)
print ('\n', u'2017年5月份的日历:')
print (cld.prmonth(2017, 5, 1, 1)) # = print cld.month(2017, 5, 1, 1)

#是闰年返回True，否则为false。
print (cld.isleap(2017))
#返回在Y1，Y2两年之间的闰年总数
print (cld.leapdays(2000,2017))


#返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。
#Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
print (cld.monthcalendar(2017, 4))

#返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。
#日从0（星期一）到6（星期日）;月从1到12。
print (u'本月开始星期%d+1,本月有%d天' % cld.monthrange(2017, 4))

#每周起始日期 默认情况下，首次载入caendar模块时返回0，即星期一
print (cld.firstweekday())

#设置每周的起始日期码。0（星期一）到6（星期日）。
print (cld.setfirstweekday(3))
print (cld.firstweekday())
print (cld.prmonth(2017, 5, 1, 1))

#返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
print (cld.weekday(2017, 4, 21))
