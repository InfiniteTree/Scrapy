import requests
import bs4
import re
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    Raform = [[],[],[]]
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            
            tds = tr('td')
            '''for i in range(100):
                if tds[i] != None:
                    print("Now td{} is".format(i), tds[i])
            '''  
            k = 0
            while(k<len(tds[0])):
                if tds[0][k] != "/":
                    k = k + 1
                else:
                    k = k - 2
                    Raform[0] = tds[0][k]
                    
            Raform[1] = re.findall("..+大学", tds[1])
            
            j = 0
            isChinese = re.compile("([\u4e00-\u9fa5]+)+?")
            for j in range(100):
                if isChinese.findall(tds[2][j]):
                    Raform[2].append(tds[2][j])
            ulist.append([Raform[0],Raform[1], Raform[2]])
    pass

def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("Ranking", "Univesity", "Score"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))

def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2021"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    #print(uinfo)
    #printUnivList(uinfo, 20)

main()
