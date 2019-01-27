'''
2、sys.argv是一个包含命令行参数的列表。
3、sys.path包含了一个Python解释器自动查找所需模块的路径的列表
'''
import sys
print("命令行参数如下：")
for i in sys.argv:
    print(i)
print("\n\npython路径：",sys.path)
if __name__ == '__main__':
    print('myself')
else:
    print('itself')
a = 'Hello, world.'
b = str(a)
c = eval(repr(a))
print(b)
print(repr(c))
print(a==b)
print (a==c)
print(str(a))   #对用户友好
print(repr(a))