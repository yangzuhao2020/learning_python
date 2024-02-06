def func1():
    print("func1 开始执行。")
    num = 1 / 0
    print("func1 结束执行。")

def func2():
    print("func2 开始执行。")
    func1()
    print("func2 结束执行。")

def main():
    try:
        func2() # 在高层级去捕获出现问题的地方。
        print("func3 结束执行。")
    except Exception as e:
        print("程序出问题。")
main()