'''
data 18-12-24
z主要学习 nametuple,deque,defaultdict,OrderDict,Counter,以及子模块collections.abc
'''
#nametuple: 一个函数，作用是创建命名元组
#nametuple 对象是只读的（read-only）
from collections import namedtuple
Point = namedtuple('Point','x y')
x = Point(1,2)
print(x)
Name = namedtuple('Name','first,last')
name = Name('tom','willia')
print(name)

#deque(双向队列) ：弥补了list插入，删除的效率问题
#构造：class collections.deque([iterable[, maxlen]])
#接受一个可迭代对象，（内置的就是str,tuple,list），第二个参数指定最大队列长度
from collections import deque
#defalutdict 默认字典
#1.增加了value的容器功能，就是可以像列表的append一样增加元素
#2.增加了计数功能
from collections import defaultdict
s=[('yellow',1),('blue',2),('red',3),('yellow',4),('red',5)]
d1={}
d2=defaultdict(list)
# for k,v in s:
#     d1[k].append(v)
for k,v in s:
    d2[k].append(v)
sorted(d2)
print(d2)
sorted(d2.items())
print(d2)
from collections import defaultdict


