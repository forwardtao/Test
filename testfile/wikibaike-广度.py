import threading
import requests
import time
import re
start=time.time()
g_mutex=threading.Condition()
g_pages=[] #从中解析所有的url
g_queueurl=[] #等待爬取的url
g_existurl= [] #已经爬取的url
g_writecount= 0

class Crawler:
    def __init__(self,url,threadNum):
        self.url=url
        self.threadNum=threadNum
        self.threadpool=[]
    def craw(self):#爬虫的控制大脑
        global g_queueurl
        g_queueurl.append(url)
        depth=1
        while (depth<3):
            print("searching depth...",'depth,''...\n')
            self.downloadAll()
            self.updateQueueurl()
            g_pages=[]
            depth+=1
    def downloadAll(self):#调用多线程爬虫，在小于线程最大值和没爬完队列之前会增加线程
        global g_queueurl
        i=0
        while (i<len(g_queueurl)):
            j=0
            while j<self.threadNum and i+j <len(g_queueurl):
                threadresult=self.download(g_queueurl[i+j],j)
                j+=1
            i+=j
            for thread in self.threadpool:
                thread.join(30)
            threadpool=[]
        g_queueurl=[]
    def download(self,url,tid):#调用多线程爬虫
        crawthead=CrawlerThread(url,tid)
        self.threadpool.append(crawthead)
        crawthead.start()

    def updateQueueurl(self):
        global g_queueurl
        global g_existurl
        new_urllist=[]
        for content in g_pages:
            new_urllist+= self.geturl(content)
            g_queueurl=list(set(new_urllist)-set(g_existurl))
    def geturl(self,content):
        link_list = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>',content)
        unique_list=list(set(link_list))
        return unique_list

class CrawlerThread(threading.Thread):
    def __init__(self,url,tid):
        threading.Thread.__init__(self)
        self.url=url
        self.tid=tid
    def run(self):
        global g_mutex
        global g_writecount
        try:
            print(self.tid,"crawl",self.url)
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; '
                              'rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            r=requests.get('https://en.wikipedia.org/wiki/'+self.url,headers=headers)
            html=r.text
            link_list2 = re.findall('<a href="/wiki/([^:#=<>]*?)".*?</a>', html)
            unique_list2 = list(set(link_list2))
            for eachone in unique_list2:
                g_writecount+=1
            content2 = "No." + str(g_writecount) + "\t Thread" + str(
                self.tid) + "\t" + self.url + '->' + eachone + '\n'
            with open('title2.txt', "a+") as f:
                f.write(content2)
                f.close()
        except Exception as e:
            g_mutex.acquire()
            g_existurl.append(self.url)
            g_mutex.release()
            print('Failed downloading and saving', self.url)
            print(e)
            return None
        g_mutex.acquire()
        g_pages.append(html)
        g_existurl.append(self.url)
        g_mutex.release()

if __name__ == "__main__":
    url = "Wikipedia"
    threadNum = 5
    crawler = Crawler(url, threadNum)
    crawler.craw()
end=time.time()

print("totaltime:",end-start)




