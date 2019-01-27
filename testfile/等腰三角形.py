temp = input("打印几行：")
n = int(temp)
space=list(' '*(2*n-2))
mid=n-1
for i in range(n):
    line=space.copy()
    if i != n-1:
        line[mid-i]='*'
        line[mid+i]='*'
    else:
        line[:]='*'*(2*n-1)
    print(''.join(line))