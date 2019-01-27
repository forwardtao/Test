def BubbleSort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if num[j] > num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]

    return (num)
list1= [5,2,45,6,8,2,1]
print(BubbleSort(list1))

