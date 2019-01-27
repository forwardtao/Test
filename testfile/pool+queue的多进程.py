from multiprocessing import Process,Pool,Manager
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

def crawler(q,index):
    Process_id = "Process-"+str(index)
    while not q.empty():
        url = q.get(timeout=2)
        try:
            r=requests.get(url,timeout=20)
            print(Process_id,q.qsize(),r.status_code,url)
        except Exception as e:
            print(q.qsize(),url,"error:",e)

if __name__ == '__main__':
    manger=Manager()
    workQueue=manger.Queue(1000)

    for url in link_list:
        workQueue.put(url)

    pool=Pool(processes=3)
    for i in range(4):
        pool.apply_async(crawler,args=(workQueue,i))
        print("startprocesss")
        pool.close()
        pool.join()
        end=time.time()

        print("总时间", end - start)
        print("main process finish")
