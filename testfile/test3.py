list1=[]

for i in range(5):
    list1.append(int(input("输入%d个数"%(i+1))))
print(list1)
list2=set(list1)
list3=list(list2)
if len(list3)== 1:
    print(list3[-1])
else:
    print(list3[-2])
