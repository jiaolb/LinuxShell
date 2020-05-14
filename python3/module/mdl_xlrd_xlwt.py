import xlrd
import xlwt

# 创建一个Workbook对象，这就相当于创建了一个Excel文件
# encoding:设置字符编码，默认是ascii
# style_compression:表示是否压缩，不常用。
book = xlwt.Workbook(encoding='utf-8', style_compression=0)

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
sheet = book.add_sheet('test', cell_overwrite_ok=True)

# 向表test中添加数据 行-列-数据
sheet.write(0, 0, 'EnglishName')
sheet.write(1, 0, 'Marcovaldo')
sheet.write(0, 1, '中文名字')
sheet.write(1, 1, '马可瓦多')

# 最后，将以上操作保存到指定的Excel文件中
book.save(r'e:\test1.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错


book = xlrd.open_workbook(r"e:\test1.xls")#得到Excel文件的book对象，实例化对象
sheet0 = book.sheet_by_index(0) # 通过sheet索引获得sheet对象
print('sheet name:', sheet0.name)

sheet_name = sheet0.name  # book.sheet_names()[0]# 获得指定索引的sheet表名字
sheet1 = book.sheet_by_name(sheet_name)# 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
nrows = sheet0.nrows    # 获取行总数
print("struct:", sheet1.nrows, sheet1.ncols)

#循环打印每一行的内容
for i in range(nrows):
    print(sheet1.row_values(i))

print(sheet0.col_values(0))     # 获得第1列的数据列表
print(sheet0.cell_value(0, 0))  #
print(sheet0.cell_value(0, 1))

