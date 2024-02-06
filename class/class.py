# class Student:
#     name = None
#
#     def say_hi(self):
#         print(f"大家好，我是{self.name}")
#
# yangzuhao = Student()
# yangzuhao.name = "杨祖豪"
# yangzuhao.say_hi()
#
# stu2 = Student()
# stu2.name = "张三"
# stu2.say_hi()

# class clock:
#     id = None# 名称
#     Price = None#价格
#
#     def ring(self,time):
#         import winsound
#         winsound.Beep(100,time)
# clock1 = clock()
# clock1.Price = 250
# clock1.id = "小杨的闹钟！"
# clock1.ring(3000)

class fish:
    def __init__(self,name,taste,length):
        self.name = name
        self.taste = taste
        self.length = length
        print(f"{self.name}的长度{self.length}味道{self.taste}")

bingbingwang = fish("鲫鱼","很甜",length="0.35m")


print("打印github")

