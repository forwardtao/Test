import threading
import requests
import time
import queue as Queue

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
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.q=q
        self.name=name
    def run(self):
        print("starting"+ self.name)
        while True:
            try:
                crawler(self.name,self.q)
            except:
                break
        print("exiting"+ self.name)
def crawler(threadName,q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url,timeout=20)
        print(q.qsize(),threadName,r.status_code,url)
    except Exception as e:
        print(q.qsize(),threadName,url,"error",e)

thread_list=["thread-1","thread-2","thread-3","thread-4","thread-5"]
workQueue = Queue.Queue(1000)
threads=[]

for tname in thread_list:
    thread=MyThread(tname,workQueue)
    thread.start()
    threads.append(thread)
for url in link_list:
    workQueue.put(url)

for t in threads:
    t.join()
end=time.time()
print("总时间",end-start)
print("main thread finished")


