class Record:

    def __init__(self,date,order_id,money,province):
        self.date = date  #订单日期
        self.order_id = order_id #订单ID
        self.money = money #总价
        self.province = province #省份

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"


a = [1,2]
hello = Record("2023年12月10日","1234",125,"jiangxi")
a.append(hello) # 追加的是地址

print(a)