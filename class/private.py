import random
class Phone:
    name = ''
    use_old =0


    def __init__(self,*args):
        if len(args)==0:
            pass
        elif len(args)==1:
            self.name=args[0]
        elif len(args)==2:
            self.name=args[0]
            self.use_old=args[1]
    __is_5g_enable = False
    def __check_5g(self):
        if(self.__is_5g_enable == True):
            print("5g开启")
        else:
            print("5g关闭")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中。")

# iphone = Phone()
# iphone.call_by_5g()
if __name__ =='__main__':
    myphone1 = Phone()
    myphone1.name = 'ceshi'
    myphone1.use_old = 2
    # print(myphone1)
    myphone2= Phone('yangzuhao')
    print("我的手机是" + myphone2.name + "，目前已经使用" + str(myphone2.use_old) + "年")
    print("我的手机是" + myphone1.name + "，目前已经使用" + str(myphone1.use_old) + "年")
    myphone = Phone('xiaomi14',2)
    print("我的手机是"+myphone.name+"，目前已经使用"+str(myphone.use_old)+"年")
    # print(myphone.name)
# random