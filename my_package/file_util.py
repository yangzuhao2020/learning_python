def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r",encoding = "UTF-8")
        my_list = f.readlines()
        print(my_list)
    except Exception as e:
        print(f"出现异常了。{e}")
    else:
        print("正常")
    finally:
        if None: # 如果文件有任何错误，便不会关闭文件。
            f.close()

def append_to_file(file_name,date):
    f = open(file_name,"a",encoding="UTF-8")
    f.write(date)
    f.flush()
    f.close()

if __name__ == '__main__':
    print_file_info("D:/code/text1.txt")
    append_to_file("D:/code/text.txt","借问酒家何处去，\n牧童遥指杏花村。\n")
