class AC:#父类
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def L_R_wind(self):
        """左右摆风"""
        pass
class Midea(AC):#子类
    def cool_wind(self):
        print("美的制冷空调")
    def hot_wind(self):
        print("美的制热空调")
    def L_R_wind(self):
        print("美的摆风")

class gree(AC):#子类
    def cool_wind(self):
        print("格力制冷空调")
    def hot_wind(self):
        print("格力制热空调")
    def L_R_wind(self):
        print("格力摆风")

def air_condition(ac:AC):#函数定义
    ac.hot_wind()

cool = Midea()#将cool 变为对象
hot = gree()#将hot 变为对象

air_condition(cool) # 调用函数
air_condition(hot) # 调用函数
#最后通过子类的对象，实现了不同的输出
