'''
#查询本机cpu核心数
from multiprocessing import cpu_count
print(cpu_count())
'''
from multiprocessing import Queue,Process
import time
import requests

link_list =[]
with open("C:/Users/小仙女/Desktop/Python 网络爬虫-从入门到实践代码/Cha 7 -提升爬"
          "虫的速度/alexa.txt",'r') as f:
    f_list=f.readlines()
    for each in f_list:
        link=each.split()[1]
        link=link.replace('\n','')
        link_list.append(link)
start=time.time()

class MyProcess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q=q
    def run(self):
        print("starting" ,self.pid)
        while not self.q.empty():
            crawler(self.q)
        print("exiting",self.pid)
def crawler(q):
    url = q.get(timeout=2)
    try:
        r=requests.get(url,timeout=20)
        print(q.qsize(),r.status_code,url)
    except Exception as e:
        print(q.qsize(),url,"error:",e)
if __name__ == '__main__':
    ProcessName=["Process-1","Process-2","Process-3"]
    workQueue=Queue(1000)

    #填充队列
    for url in link_list:
        workQueue.put(url)
    for i in range(3):
        p=MyProcess(workQueue)
        p.daemon=True
        p.start()
        p.join()
    end=time.time()
    print("总时间",end-start)
    print("main process finish")

