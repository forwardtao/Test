from functools import reduce
d=[]
for i in range(5):
    d.append(int(input("请输入数字%d :"%(i+1))))
def add(x,y):
    return x+y
print(reduce(add,d))

a=[1,2,3,4,5]
def xyz(x,y):
    return x*10+y
print(reduce(xyz,a))


