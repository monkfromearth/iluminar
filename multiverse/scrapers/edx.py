from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('https://www.edx.org/subjects')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
slist = soup.findAll('a',{'class':'subject-link'})
sublink = list(set(lk['href'] for lk in slist))
count = 0
for i in sublink:
    driver.get('https://www.edx.org ' + i)
    htm = driver.page_source
    soup = BeautifulSoup(htm,'html.parser')
    count = count+1
    print(count)
    if len(soup.findAll('div',{'class':'card-wrapper three-column-layout position-relative'}))>0:
        slist = soup.findAll('div',{'class':'row card-columns'})
        for crlk in slist:
            cont = soup.findAll('div',{'class':'card-body program'})
            for fr in cont:
                crlnk = soup.findAll('a',{'class':'card-link'})
                crlink = [lk['href'] for lk in crlnk]
                for lks in crlink:
                    driver.get('https://www.edx.org'+lks)
                    htm4 = driver.page_source
                    soup = BeautifulSoup(htm4,'html.parser')
                    clist = soup.findAll('a',{'class':'card-link'})
                    crname = slist[0].text
                    crlinks = [lkr['href'] for lkr in clist]
                    for nk in crlinks:
                        driver.implicitly_wait(10)
                        driver.get('https://www.edx.org'+nk)
                        htm5 = driver.page_source
                        soup = BeautifulSoup(htm5,'html.parser')
                        info = soup.findAll('div',{'class':'course-stat col-md'})
                        for infor in info:
                            cprice =(soup.findAll('div',{'class':'highlight'}))[0].text
                            efforts1 = (soup.findAll('div',{'class':'highlight'}))[1].findAll(text=True)
                            level = (soup.findAll('div',{'class':'stat-details'}))[1].text
                        print(cprice)
                        print(efforts1)
                        print(level)
                        inst = soup.findAll('div',{'class':'instructor-list no-gutters'})
                        for ins in inst:
                            imdet = soup.findAll('img',{'class':'rounded-circle w-100'})
                            imsrc = [isrc['src'] for isrc in imdet]
                            inname = soup.findAll('a',{'class':'name font-weight-bold'})
                            inname1 = []
                            indes1 = []
                            inorg1 = []
                            for inn in inname:
                                inname1.append(inn.text)
                            indes = soup.findAll('div',{'class':'title font-italic'})
                            for ind in indes:
                                indes1.append(ind.text)
                            inorg = soup.findAll('div',{'class':'org'})
                            for ino in inorg:
                                inorg1.append(ino.text)
                            print(imsrc)
                            print(inname1)
                            print(indes1)
                            print(inorg1)
                            sy = soup.findAll('div',{'class':'mb-4'})[0]
                            slb = sy.findChildren('li')
                            sylb = []
                            for txt in slb: sylb.append(txt.text)
                            print(sylb)
    elif len(soup.findAll('div',{'class':'discovery-card course-card shadow verified'}))>0:
        lk2 = soup.findAll('a',{'class':'course-link'})
        clink2 = [k['href'] for k in lk2]
        for z in clink2:
            driver.get(z)
            htm2 = driver.page_source
            soup = BeautifulSoup(htm2,'html.parser')
            slist = soup.findAll('div',{'class':'course-info-list wysiwyg-content'})
            for i in slist:
                det = i.findChildren('li')
                details = []
                for j in det:
                    details.append(j.text)
                print(details)
            ocont = soup.findAll('ul',{'class':'clear-list block-list content-block'})
            cn = soup.findAll('span',{'class':'text-size-heading'})
            cname = []
            for nm in cn:
                cname.append(nm.text)
            iname = soup.findAll('p',{'class':'instructor-name'})
            for con in ocont:
                clength = (soup.findAll('span',{'class':'block-list__desc'})[0]).text
                ehours = (soup.findAll('span',{'class':'block-list__desc'})[1]).text
                school = (soup.findAll('span',{'class':'block-list__desc'})[3]).text
                level = (soup.findAll('span',{'class':'block-list__desc'})[5]).text
                lang = (soup.findAll('span',{'class':'block-list__desc'})[6]).text
                print(clength, ehours, level, lang, school)
            ilist = soup.findAll('ul',{'class':'clear-list list-instructors clearfix'})
            for mf in enumerate(ilist):
                det1 =soup.findAll('img',{'class':'instructor-img'})
                imgsrc = [img['src'] for img in det1]
                print(imgsrc)
                det2 = soup.findAll('p',{'class':'instructor-name'})
                iname = []
                for inm in det2:
                    iname.append(inm.text)
                det3 = soup.findAll('p',{'class':'instructor-position'})
                inpos = []
                for inp in det3:
                    inpos.append(inp.findAll(text=True)[0].strip().strip('\n'))
                det4 = soup.findAll('span',{'class':'instructor-org'})
                inorg = []
                for inor in det4:
                    inorg.append(inor.text)
                print(iname)
                print(inpos)
                print(inorg)
                        
            
            

