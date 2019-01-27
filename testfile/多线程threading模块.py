import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name=name
        self.delay=delay
    def run(self):
        print("starting"+ self.name)
        print_time(self.name,self.delay)
        print("exiting"+ self.name)
def print_time(threadName,delay):
    count=0
    while count<3:
        time.sleep(delay)
        print(threadName,time.ctime())
        count+=1
threads=[]
#添加新线程
thread1=MyThread("thread-1",1)
thread2=MyThread("thread-2",2)

#开启线程
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

#等待线程完成
for t in threads:
    t.join()

print("main finished")


