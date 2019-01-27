import csv

with open('D:/python_study/testfile/test.csv','r') as f:
    f_data= csv.reader(f)
    for row in f_data:
        print(row)
        print(row[0])
        print(row)
#csv 写入
stu1 = ['A5','B5','C5','D5']
stu2 = ['A6','B6','C6','D6']
#打开文件，追加a
out = open('test.csv','a', newline='')
#设定写入模式
csv_write = csv.writer(out,dialect='excel')
#写入具体内容
csv_write.writerow(stu1)
csv_write.writerow(stu2)
print ("write over")

