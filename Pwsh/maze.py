from pwn import *
import time


sh=process("pwsh.exe")
#time.sleep(1)
#print(sh.recv(4096))
sh.send("Import-Module -Name .\\PSMaze.dll\n")
sh.send("cd Maze:\n")
time.sleep(2)
print(sh.recv(4096))

fx={"Down":0,"Up":3,"Left":1,"Right":2}
fxa=["Down","Left","Right","Up"]
fxs=[[0,1],[-1,0],[1,0],[0,-1]] 

def ersp(x):
    while x.find('  ')!=-1:
        x=x.replace("  "," ")
    return x

def gls(dep):
    sh.send("ls\n")
    time.sleep(0.1+dep*0.0002)
    xx=sh.recv(4096)
    gg=xx.split('\n')
    gg=gg[4:-2]
    print(xx)
    res=[]
    for i in gg:
        st=ersp(i[:-1]).split(' ')
        xa=st[-4:]
        xb=[fx[xa[0]],int(xa[1]),int(xa[2]),xa[3]]
        print(xb)
        res.append(xb)
    return res

nx=0
ny=0

def cdl(ff,dep,btf=0):
    global nx,ny
    nx+=fxs[ff][0]
    ny+=fxs[ff][1]
    if btf:
        sh.send("cd ..\n")
    else:
        sh.send("cd "+fxa[ff]+"\n")
    time.sleep(0.05+dep*0.0002)
    xx=sh.recv(4096)
    #print(xx)


vis={}
cn=0
def dfs(fa,dep):
    global vis,cn
    if (nx,ny) in vis:
        return
    vis[(nx,ny)]=1
    cn+=1
    print(nx,ny,cn)
    sos=gls(dep)
    for i in sos:
        if i[0]==fa:
            continue
        if i[3]!='':
            time.sleep(10000)
        cdl(i[0],dep)
        dfs(3-i[0],dep+1)
        cdl(3-i[0],dep,1)

dfs(-1,0)