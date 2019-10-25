import socket
import requests as rq
import json
import threading
import time
import re

cnt=0

def do1():
    global cnt
    s=socket.socket()

    s.connect(("202.38.93.241",10017))
    print(s.recv(4096))
    s.sendall(b"TOKEN\n")
    print(s.recv(4096))
    s.sendall(b"-80538738812075974\n80435758145817515\n12602123297335631\n")
    time.sleep(0.02)
    print(s.recv(4096))
    xx=s.recv(4096)
    print(xx)
    if xx.find(b'=')==-1:
        xx=s.recv(4096)
        print(xx)
    gg=xx.split(b'=')[3]
    gg=gg[:-3].decode()
    print(gg)

    r=rq.post("http://localhost:5000/que3",data={"num":gg})
    dt=json.loads(r.text)
    r=rq.post("http://localhost:5000/que2",data={"num":gg})
    dta=json.loads(r.text)
    dt=dt+dta
    print(dt)
    for i in dt:
        s.sendall((i+'\n').encode())
    time.sleep(0.2)
    #print(s.recv(4096))
    xx=s.recv(4096)
    print("HTN")
    print(xx)
    while True:
        gx=re.search(r'[0-9]{10,}',xx.decode())
        #gg=gg[1:-3].decode()
        if gx:
            print("RIT")
            break
        if len(xx)==0:
            break
        xx=s.recv(4096)
        print(xx)
    gg=re.search( r'[0-9]{10,}',xx.decode()).group()
    print("NUMBET")
    print(gg)
    cnt=cnt+1
    r=rq.post("http://localhost:5000/que4",data={"num":gg})
    print(r.text)
    dt=json.loads(r.text)
    print(dt)
    rdy=0
    if dt[0]!="0":
        rdy=1
    for i in dt:
        s.sendall((i+'\n').encode())
    print(s.recv(4096))
    print(s.recv(4096))
    print(s.recv(4096))
    if rdy==1:
        time.sleep(10000)
        exit(0)

while True:
    #do1()
    print("CNT",cnt)
    try:
        do1()
    except:
        pass