import time
date1=time.localtime(time.time())
print('本地时间',date1)
#获取格式化时间
date2=time.asctime(time.localtime(time.time()))
print('本地时间',date2)
#格式化日期 time.strftime(format[, t])
from itertools import permutations
import itertools
s=''
list2=[]
list1=list(itertools.permutations([1, 2, 3, 4], 3))
for i in list1:
    for j in i:
        s+=str(j)
    list2.append(s)
    s=''
print(list2)



# print(list1)
#
# for i in permutations([1, 2, 3, 4], 3):
#     print(i[0], i[1], i[2])
