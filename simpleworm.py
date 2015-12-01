from bs4 import BeautifulSoup
import re
import urllib2
import time
import csv
from sgmllib import SGMLParser
from multiprocessing import Pool
data = []
urls = []
exceldata = []
def get_geekbench_urls(a,b):#store url into an array
    for j in range(a,b):
        urls.append('http://browser.primatelabs.com/geekbench3/1152'+str(j))
    return urls
def MyHTMLParser(url):  
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1)')
        req.add_header('Connection','Keep-Alive')
        req.add_header('Accept-Language','zh-CN,zh;q=0.8')
        req.add_header('Accept','*/*')
        req.add_header('Accept-Charset','GBK,utf-8;q=0.7,*;q=0.3')
        req.add_header('Cache-Control','max-age=0')
        content = urllib2.urlopen(req).read()
        
        soup=BeautifulSoup(content)
        names=soup.select('div.page-header h1')
        singlescore=soup.select('td.score')
        processor=soup.select('td.value')
        OSVersion=processor[2].text
        ProcessorModel=processor[4].text
        match1=re.compile(r".*@")
        ProcessorName=re.findall(match1,ProcessorModel)[0]
        match2=re.compile(r"@.*Hz")
        ProcessorFreq=re.findall(match2,ProcessorModel)[0]
        ProcessorName=ProcessorName[:-2]
        ProcessorFreq=ProcessorFreq[2:]
        name=names[0].text[1:]
        name=name[:-1]
        print(url[42:49]+'\t'+name+'\t'+OSVersion+'\t'+ProcessorName+'\t'+ProcessorFreq+'\t'+singlescore[0].text+'\t'+singlescore[1].text)
        return [url[42:49],name,OSVersion,ProcessorName,ProcessorFreq,singlescore[0].text,singlescore[1].text]
    except urllib2.URLError,e:
        print(e.Reason)
    except re.error,e:
        print()
def writeFile(url): #write array into file
    csvfile=file('text.csv','ab')
    try:
        writer = csv.writer(csvfile)
        writer.writerow(MyHTMLParser(url))
    except Exception:
        print('Error\n')
    finally:
        csvfile.close()

if __name__ == '__main__':
    c=time.time()
    pool = Pool(8)
    geekbench_page_urls=get_geekbench_urls(100,999)
    pool.map(writeFile, geekbench_page_urls)
    print time.time()-c
