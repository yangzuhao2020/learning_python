"""
这里是文件相关的定义
"""
import json

#先定义一个抽象类用来做顶层设计，让两个文件通过相似的方式被处理
import date_define

class FileReader:

    def read_date(self)->list[date_define.Record]:
        """读取文件，将读取到的每一条数据都转换为Record对象，都封装到list返回即可"""
        pass

class TextFilerReader(FileReader):

    def __init__(self,path):
        self.path = path #记录文件路径

    def read_date(self) ->list[date_define.Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list = []
        for l in f.readlines():
            l = l.strip() #消除\n
            l = l.split(",") #转化为列表
            record = date_define.Record(l[0],l[1],int(l[2]),l[3]) #定义了一个record的对象，并对其赋值。
            record_list.append(record) # 这种操作有点奇怪，append 直接给了追加是对象 后期可以认为他还是一个类对象，进行record.date
            #record_list.append()
        f.close()
        # print(f"结果{record_list}")
        return record_list

class JsonFilerReader(FileReader):
    def __init__(self,path):
        self.path = path #记录文件路径

    def read_date(self) ->list[date_define.Record]:
        f = open(self.path,"r",encoding = "UTF-8")
        record_list = []
        for line in f.readlines():
            my_dict = json.loads(line.strip()) #这样会得到一个字典对象
            record = date_define.Record(my_dict["date"],my_dict["order_id"],int(my_dict["money"]),my_dict["province"])#定义了一个record的对象，并对其赋值。
            record_list.append(record)
        f.close()
        return record_list

if __name__ == "__main__":
    day1 = TextFilerReader("D:/code/day1.txt")
    list1 = day1.read_date()
    for i in list1:
        print(i)
    print(f"result{list1[5].date}")

    day2 = JsonFilerReader("D:/code/day2.txt")
    list2 = day2.read_date()
    for i in list2:
        print(i)
