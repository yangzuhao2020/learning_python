"""
面向对象，数据分析案例
实现步骤：
1. 设计一个类。
2. 设计一个抽象类，定义文件读取相关功能，使用子类实现具体功能
3. 读取文件，生产数据对象
4. 进行数据需求的逻辑计算
5. 通过PyEcharts 进行图形的绘制
"""
from file_define import FileReader, TextFilerReader, JsonFilerReader
from date_define import Record

textFilerReader = TextFilerReader("D:/code/day1.txt")
jsonFilerReader = JsonFilerReader("D:/code/day2.txt")

list1:list[Record] = textFilerReader.read_date()
list2:list[Record] = jsonFilerReader.read_date()

date_list = list1 + list2

date_dict = {}

for record in date_list:
    if record.date in date_dict.keys():
        date_dict[record.date] += record.money
    else:
        date_dict[record.date] = record.money

print(date_dict) # 最后以字典的形式输出