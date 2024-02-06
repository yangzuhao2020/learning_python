f = open("D:/code/bill.txt","r",encoding = "UTF-8")
bak = open("D:/code/bill.txt.bak","w",encoding = "UTF-8")
for line in f:
    line = line.strip()
    if line.split(",")[4] == "测试":
        print(line.split(",")[4])
        continue
    bak.write(line)
    bak.write("\n")
f.close()
bak.close()
