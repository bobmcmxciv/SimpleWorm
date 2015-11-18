import Queue
import re
import urllib2,urllib 
import time
import multiprocessing
import sys
from sgmllib import SGMLParser
from multiprocessing import Pool
data = []
urls = []
def get_geekbench_urls(a,b):#store url into an array
    for j in range(a,b):
        urls.append('http://browser.primatelabs.com/geekbench3/1152'+str(j))
    return urls
def get_geekbench_data(url): #return geekbench data
    try:
        req = urllib2.Request(url)  
        content = urllib2.urlopen(req).read() 
        match = re.compile(r"'3'>(d{6}\d{5}|\d{4}|\d{3}|\d{2}|d{1})")
        match2 = re.compile(r"eader\"><h1>")
        rawlv2 = re.findall(match,content)
        print(str(rawlv2)+', '+url[42:49])
        #sys.stdout.write(str(rawlv2)+', '+url[42:49])
        data.append(str(rawlv2)+', '+url[42:49]+'\n')
    except urllib2.URLError,e:
        print(e.reason)
        #return str(rawlv2)
#def store_geekbench_data(single_data): #store geekbench data into array
#    data.append(single_data)
def writeFile(geekbench_data): #write array into file
    f = open("text.txt",'w')
    f.writelines(geekbench_data)
    f.close()
if __name__ == '__main__':
    c=time.time()
    pool = Pool(8)#16????????????????
    geekbench_page_urls=get_geekbench_urls(700,800)
    #pool.map(get_geekbench_data, geekbench_page_urls)
    #print(data) #because of multithread have some problem, so we use singlethread now
    for i in range(700,750):
        get_geekbench_data('http://browser.primatelabs.com/geekbench3/1152'+str(i))
    writeFile(data)
    print time.time()-c
