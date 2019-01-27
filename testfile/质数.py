num = int(input("请输入一个大于1的正整数："))

n = num

f1 = []   #用于存放num以内的质数


while n >= 2:

     #用于临时判断n

    for i in range(2,n):

        if n % i ==0:   #不是质数

            f2.append(i)

            break

    if len(f2) == 0:  #是质数

        f1.append(n)

    n -= 1

print('小于等于%d的质数有%d个，分别是：' %(num,len(f1)))

print(f1)