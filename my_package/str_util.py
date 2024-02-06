def str_reverse(str):
    """
    输入一个字符串，返回一个新的字符串。
    :param str:
    :return:
    """
    return str[::-1]
def substr(str, x, y):
    str2 = ""
    while(x < y):
        str2 += str[x]
        x += 1
    return str2

if __name__ == '__main__':
    print(str_reverse("yang"))
    # print(str2)
    print(substr("yang",1,4))