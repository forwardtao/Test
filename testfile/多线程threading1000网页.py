import threading
import requests
import time

link_list=[]
with open("C:/Users/小仙女/Desktop/Python 网络爬虫-从入门到实践代码/Cha 7 -提升爬"
          "虫的速度/alexa.txt",'r') as f:
    f_list=f.readlines()

    for eachone in f_list:
        link=eachone.split()[1]
        link=link.replace('\n','')
        link_list.append(link)
start=time.time()

class MyThread(threading.Thread):
    def __init__(self,name,link_range):
        threading.Thread.__init__(self)
        self.link_range=link_range
        self.name=name
    def run(self):
        print("starting"+ self.name)
        crawler(self.name,self.link_range)
        print("exiting"+ self.name)
def crawler(threadName,link_range):
    for i in range(link_range[0],link_range[1]+1):
        try:
            r=requests.get(link_list[i],timeout=20)
            print(threadName,r.status_code,link_list[i])
        except Exception as e:
            print(threadName,"error",e)
thread_list=[]
link_range_list=[(0,200),(201,400),(401,600),(601,800),(801,1000)]
#创建新线程
for i  in range(1,6):
    thread=MyThread("thread-"+str(i),link_range_list[i-1])
    thread.start()
    thread_list.append(thread)

for thread in thread_list:
    thread.join()
end=time.time()
print("总时间",end-start)


