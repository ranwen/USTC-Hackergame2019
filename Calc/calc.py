import json
import requests
import math

host = "http://202.38.93.241:10024"


ln2=math.log(2)

def getc(num,dep):
    #print("GN",num)
    if dep==0:
        return "cos"
    ss="exp"
    while num>1.5:
        num/=2
        ss+=",x^2"
    ss+=",log"
    if num>0.9 and num<1.1 and dep<25:
        return "cos,"+ss
    if num>ln2+0.02:
        num-=ln2
        ss="exp,exp,x^2,log,log,"+ss
    ss="1/x,"+ss
    ss=getc(1/num,dep-1)+","+ss
    return ss

def solve(x):
    return getc(x,50)

def outc(x):
    gg=x.split(",")
    now=0
    for i in gg:
        if i=="cos":
            now=math.cos(now)
        elif i=="exp":
            now=math.exp(now)
        elif i=="log":
            now=math.log(now)
        elif i=="x^2":
            now=now*now
        elif i=="1/x":
            now=1/now
        print(i+" "+str(now))

def main():
    with requests.session() as sess:
        r = sess.get(host + '/challenges')
        X = json.loads(r.text)["msg"]
        print(X)
        data = {
            "a1": solve(X[0]),
            "a2": solve(X[1]),
            "a3": solve(X[2])
        }
        r = sess.post(host + "/submit", data=data)
        resp = json.loads(r.text)
        print(resp["msg"])

main()
print(solve(72.12422465141421))
xx=solve(1)
print(xx)
#outc(xx)