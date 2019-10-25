import os
import json
import math
import time
import re
from shutil import copyfile
from flask import Flask,request
import queue
from flask.logging import default_handler
import logging
log=logging.getLogger("mid")
log.setLevel(logging.WARNING)



default_handler.setLevel(logging.WARNING)
# import pyecm as pce
# def factors(x):
#     print(x)
#     aa=pce.factors(x,False,False,7.97308847044, 1.0)
#     lis=[]
#     for i in aa:
#         print(i)
#         lis.append(int(i))
#     lis.sort()
#     return lis


app = Flask("mid")
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)

ans2={}
ans3={}
q2=[]
q3=[]

@app.route('/get2')
def get2():
    global q2
    if len(q2)==0:
        return "0"
    sx=q2[0]
    q2=q2[1:]
    return str(sx)

@app.route('/get3')
def get3():
    global q3
    if len(q3)==0:
        return "0"
    sx=q3[0]
    q3=q3[1:]
    return str(sx)

@app.route('/sub2',methods=["POST"])
def sub2():
    global ans2
    #num=int(request.form["num"])
    txt=request.form["res"]
    txt=re.sub("\\([0-9]* digits\\)","",txt)
    txt=txt.replace("²","")
    txt=txt.replace("³","")
    txt=txt.replace("(","")
    txt=txt.replace(")","")
    txt=txt.replace(" ","")
    txt=txt.replace(":","=")
    num=int(txt.split('=')[0])
    if txt.find("This")!=-1:
        ans2[num]="[\"0\",\"0\",\"0\",\"0\"]"
        return
    txt=txt.split('=')[1]
    txt=txt.split('+')
    while len(txt)<4:
        txt.append('0')
    ans2[num]=json.dumps(txt)
    return ""

@app.route('/sub3',methods=["POST"])
def sub3():
    global ans3
    #num=int(request.form["num"])
    txt=request.form["res"]
    txt=re.sub("\\([0-9]* digits\\)","",txt)
    txt=txt.replace("²","")
    txt=txt.replace("³","")
    txt=txt.replace("(","")
    txt=txt.replace(")","")
    txt=txt.replace(" ","")
    txt=txt.replace(":","=")
    num=int(txt.split('=')[0])
    if txt.find("This")!=-1:
        ans3[num]="[\"0\",\"0\",\"0\",\"0\"]"
        return ""
    txt=txt.split('=')[1]
    txt=txt.split('+')
    while len(txt)<4:
        txt.append('0')
    ans3[num]=json.dumps(txt)
    return ""

@app.route('/que2',methods=["POST"])
def que2():
    global q2
    num=int(request.form["num"])
    q2.append(num)
    while not num in ans2:
        time.sleep(0.1)
    return ans2[num]

@app.route('/que3',methods=["POST"])
def que3():
    global q3
    num=int(request.form["num"])
    q3.append(num)
    while not num in ans3:
        time.sleep(0.1)
    return ans3[num]

def mods(a, n):
    if n <= 0:
        return "negative modulus"
    a = a % n
    if (2 * a > n):
        a -= n
    return a

def powmods(a, r, n):
    out = 1
    while r > 0:
        if (r % 2) == 1:
            r -= 1
            out = mods(out * a, n)
        r //= 2
        a = mods(a * a, n)
    return out

def quos(a, n):
    if n <= 0:
        return "negative modulus"
    return (a - mods(a, n))//n

def grem(w, z):
    # remainder in Gaussian integers when dividing w by z
    (w0, w1) = w
    (z0, z1) = z
    n = z0 * z0 + z1 * z1
    if n == 0:
        return "division by zero"
    u0 = quos(w0 * z0 + w1 * z1, n)
    u1 = quos(w1 * z0 - w0 * z1, n)
    return(w0 - z0 * u0 + z1 * u1,
           w1 - z0 * u1 - z1 * u0)

def ggcd(w, z):
    while z != (0,0):
        w, z = z, grem(w, z)
    return w

def root4(p):
    # 4th root of 1 modulo p
    if p <= 1:
        return "too small"
    if (p % 4) != 1:
        return "not congruent to 1"
    k = p//4
    j = 2
    #print(j,k,p)
    while True:
        a = powmods(j, k, p)
        b = mods(a * a, p)
        #print(a,b)
        if b == -1:
            return a
        if b != 1:
            return "not prime"
        j += 1

def sq2(p):
    if p==1:
        return (1,0)
    if p==2:
        return (1,1)
    a = root4(p)
    #print(a,p)
    return ggcd((p,0),(a,1))


def merge(a,b):
    return (a[0]*b[0]+a[1]*b[1],a[0]*b[1]-a[1]*b[0])

@app.route('/que4',methods=["POST"])
def que4():
    #print(request.form)
    if request.form["num"]=="":
        return "[\"0\",\"0\"]"
    num=int(request.form["num"])
    bs=1
    ba=(1,0)
    #try:
    for i in range(2,10000000):
        while num%(i*i)==0:
            num=num//(i*i)
            bs*=i
        if num%i==0:
            print("HIT",i)
            num=num//i
            sax=sq2(i)
            print(ba,sax)
            ba=merge(ba,sax)
            print(ba)
    #ftl=factors(num)
    print("REM",num)
    #for i in ftl:
    #    print("FAC",i)
    #    sax=sq2(i)
    #    print(ba,sax)
    #    ba=merge(ba,sax)
    #    print(ba)
    sax=sq2(num)
    print(ba,sax)
    ba=merge(ba,sax)
    print(ba)
    return json.dumps([str(ba[0]*bs),str(ba[1]*bs)])
    #except:
    return "[\"0\",\"0\"]"

app.run(host="0.0.0.0",port=5000,debug=True,threaded=True)
