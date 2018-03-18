import os
import bs4

from urllib.request import urlopen as  uReq
from bs4 import BeautifulSoup as soup

import subprocess


def runcpp(sid,cid):
    os.system('g++ '+sid+'.cpp -o '+sid+' -std=gnu++11 2>dump')
    os.system('./'+sid+' 0<'+cid+' 1>'+cid+'out'+sid+' 2>dump')
    print('Checking difference with Ans!!')
    #os.system('python Check_Result.py '+cid+' '+sid)
    subprocess.check_call('python Check_Result.py '+cid+' '+sid,shell=True)
    print('And Done!!\n')

def checkcppcodes():
    for container in cppcontainers:
        sid = container.get('acceptedsubmissionid')
        if sid!=None:
            print('Getting and Running submission:'+str(sid))
            url = 'http://codeforces.com/contest/'+str(con)+'/submission/'+sid
            try:
                uClient = uReq(url,timeout=10)
            except:
                print('Sorry!!! Timed OUT :( ')
                continue
            page_html = uClient.read()
            uClient.close()
            code_soup = soup(page_html,"html.parser")
            ccid = code_soup.findAll("td")
            cid = ccid[2].a.text
            codeclass = code_soup.findAll("pre",{"class":"prettyprint lang-cpp program-source"})
            fl = open(sid+'.cpp','w',newline='\n')
            s = str(codeclass)
            s = s.replace('[<pre class="prettyprint lang-cpp program-source" style="padding: 0.5em;">','')
            s = s.replace('</pre>]','')
            s = s.replace('&lt;','<')
            s = s.replace('&gt;','>')
            s = s.replace('&amp;','&')
            fl.write(s)
            fl.close()
            runcpp(sid,cid)


def getcppids():
    print('\n\n------------Checking Cpp Codes----------------------\n\n')
    global cppcontainers
    cppcontainers = page_soup.findAll("td",{"title":"GNU C++14"})
    checkcppcodes()

def runjava(sid,cid):

    os.system('javac '+javafilename+'.java 2>dump')
    os.system('java '+javafilename+' 0<'+cid+' 1>'+cid+'out'+sid+' 2>dump')
    print('Checking difference with Ans!!')
    #os.system('python Check_Result.py '+cid+' '+sid)
    subprocess.check_call('python Check_Result_forFuckingJava.py '+cid+' '+sid+' '+javafilename,shell=True)
    print('And Done!!\n')


def checkjavacodes():
    for container in javacontainers:
        sid = container.get('acceptedsubmissionid')
        if sid!=None:
            print('Getting and Running submission:'+str(sid))
            url = 'http://codeforces.com/contest/'+str(con)+'/submission/'+sid
            try:
                uClient = uReq(url,timeout=10)
            except:
                print('Sorry!!! Timed OUT :( ')
                continue
            page_html = uClient.read()
            uClient.close()
            code_soup = soup(page_html,"html.parser")
            ccid = code_soup.findAll("td")
            cid = ccid[2].a.text
            codeclass = code_soup.findAll("pre",{"class":"prettyprint lang-java program-source"})
            s = str(codeclass)
            startin = s.find('public class ')
            startin += 13
            endin = s.find(' ',startin)
            end1in = s.find('{',startin)
            if end1in < endin:
                endin = end1in
            global javafilename
            javafilename = s[startin:endin]
            fl = open(javafilename+'.java','w',newline='\n')
            s = s.replace('[<pre class="prettyprint lang-java program-source" style="padding: 0.5em;">','')
            s = s.replace('</pre>]','')
            s = s.replace('&lt;','<')
            s = s.replace('&gt;','>')
            s = s.replace('&amp;','&')
            s = "//Submission id = "+str(sid)+"\n"+ s
            fl.write(s)
            fl.close()
            runjava(sid,cid)


def getjavaids():
    print('\n\n------------Checking Java Codes----------------------\n\n')
    global javacontainers
    javacontainers = page_soup.findAll("td",{"title":"Java 8"})
    checkjavacodes()

def runpython(sid,cid):
    os.system('python '+sid+'.py 0<'+cid+' 1>'+cid+'out'+sid+' 2>dump')
    print('Checking difference with Ans!!')
    #os.system('python Check_Result.py '+cid+' '+sid)
    subprocess.check_call('python Check_Result.py '+cid+' '+sid,shell=True)
    print('And Done!!\n')


def checkpythoncodes():
    for container in pythoncontainers:
        sid = container.get('acceptedsubmissionid')
        if sid!=None:
            print('Getting and Running submission:'+str(sid))
            url = 'http://codeforces.com/contest/'+str(con)+'/submission/'+sid
            try:
                uClient = uReq(url,timeout=10)
            except:
                print('Sorry!!! Timed OUT :( ')
                continue
            page_html = uClient.read()
            uClient.close()
            code_soup = soup(page_html,"html.parser")
            ccid = code_soup.findAll("td")
            cid = ccid[2].a.text
            codeclass = code_soup.findAll("pre",{"class":"prettyprint lang-py program-source"})
            fl = open(sid+'.py','w',newline='\n')
            s = str(codeclass)
            s = s.replace('[<pre class="prettyprint lang-py program-source" style="padding: 0.5em;">','')
            s = s.replace('</pre>]','')
            s = s.replace('&lt;','<')
            s = s.replace('&gt;','>')
            s = s.replace('&amp;','&')
            fl.write(s)
            fl.close()
            runpython(sid,cid)


def getpythonids():
    print('\n\n------------Checking Phython Codes----------------------\n\n')
    global pythoncontainers
    pythoncontainers = page_soup.findAll("td",{"title":"Python 3"})
    checkpythoncodes()



def getdata():
    global con
    con = input('enter contest Number: ')
    global mx
    mx = int(input('enter number of pages you want to run: '))
    global pgn
    pgn = 1

def runpages():
    global pgn
    main_url = "http://codeforces.com/contest/"+str(con)+"/standings/page/"+str(pgn)
    uClient = uReq(main_url)
    page_html = uClient.read()
    uClient.close()
    global page_soup
    page_soup = soup(page_html,"html.parser")
    getcppids()
    getjavaids()
    getpythonids()
    print(str(pgn))
    pgn += 1
    if pgn<=mx:
        runpages()


#-------------------------------------------------------------

os.system('mkdir CodesofHacks 2>dump')
getdata()
runpages()
