def my_fuction(computing): # 你可以computing ,你也可以随便写一些什么。
    result = computing(3,5)
    print(f"返回的结果{result}")

def computing(x , y):
    return x + y

my_fuction(computing)
my_fuction(lambda x,y : x + y)