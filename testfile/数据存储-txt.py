
testfile= 'Beautiful is better than ugly.'
with open ('D:/python_study/testfile/test.txt','a+') as f:
    f.write(testfile)
    f.close()

with open('test.txt', "r") as f:
    result = f.read()
    print (result)


