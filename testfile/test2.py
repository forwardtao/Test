print("-----求平均值，可输入任意多个数-------")
lst = [] #定义一个空列表
str = input("请输入数值，用空格隔开:")
lst1 = str.split(" ")#lst1用来存储输入的字符串，用空格分割
i = 0
while i <= len(lst1)+1:
	lst.append(int(lst1.pop()))#将lst1的数据转换为整型并赋值给lst
	i += 1
#print(lst)
def sum(list):
	"对列表的数值求和"
	s = 0
	for x in list:
		s += x
	return s
def average(list):
	"对列表数据求平均值"
	avg = 0
	avg = sum(list)/(len(list)*1.0) #调用sum函数求和
	return avg
print("avg = %f"%average(lst))
