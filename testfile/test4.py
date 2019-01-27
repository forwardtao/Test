list1=[num for num in range(2,100) if not sum([num%i==0 for i in range(2,num)])]
print(list1)
list2=(filter(lambda x:all(x%i!=0 for i in range(2,x)),range(2,201)))
print(list2)
x = [1 for i in range(10)]
print(x)
lst=[num for num in range(2,100)]
print(lst)