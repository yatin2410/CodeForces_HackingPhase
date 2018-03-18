import sys
import filecmp
import os

cid = sys.argv[1]
sid = sys.argv[2]
javafile = sys.argv[3]

codeout = open(cid+'out'+sid)
ansout = open(cid+'ans')
difile = 'HackData'
diffile = open(difile,'a')
diffile.write(sid+"   ")

ans = True


linea = ansout.readline()
linea = linea.replace(' ','')
linea = linea.replace('\n','')
linec = codeout.readline()
linec = linec.replace(' ','')
linec = linec.replace('\n','')

if linea != linec:
    ans = False


while linea:
    linea = ansout.readline()
    linea = linea.replace(' ','')
    linea = linea.replace('\n','')
    linec = codeout.readline()
    if linec == None:
        ans = False
    linec = linec.replace(' ','')
    linec = linec.replace('\n','')
    if linea != linec:
        ans = False

if ans:
    diffile.write("Not\n")
    os.system('rm '+cid+'out'+sid)
else:
    diffile.write("Hacked\n")
    os.system('mv '+cid+'out'+sid+' CodesofHacks')

os.system('rm '+javafile+'.java 2>dump')
os.system('rm '+javafile+'.class 2>dump')


diffile.close()
