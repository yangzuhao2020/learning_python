# f = open ("D:/code/text_for_python.txt","r",encoding="UTF-8")
# print(type(f))
# result = f.read(10)
# result = f.read()
# print(result)
# my_list =f.readlines()
# print(type(my_list),my_list)
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行的数据是，{line1}")
# print(f"第二行的数据是，{line2}")
# print(f"第三行的数据是，{line3}")
# for line in f:
#     print(f"每一行数据：{line}")

with open("D:/code/word.txt","r",encoding="UTF-8") as f:
    my_list = f.readlines()
    print(my_list)
    total = 0
    for i in my_list:
        num = i.count("ithema")
        total = total + num
    print(total)