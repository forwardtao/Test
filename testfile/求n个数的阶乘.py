a=int(input('输入一个数：\n'))
def fn(n):
    if n ==1:
        return 1
    else:
        return n*fn(n-1)
print(sum(map(fn,range(1,a+1))))
