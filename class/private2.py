class Phone:
    __current_voltage = 0 #私有成员
    def __keep_single_core(self):
        print("以单核模式运行") #私有方法

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g已经开始。")

        else:
            self.__keep_single_core()
            print("抱歉电量不足。")
iphone = Phone()
iphone.call_by_5g()