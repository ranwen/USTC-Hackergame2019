#!/usr/bin/env python3
import cipolla
from gmpy2 import *

x = 130095999494467643631574289251374479743427759332282644620931023932981730612064829262332840253969261363881910701276769455728130421459878658660627330362688856751252524519341435317968272275310598639991033512763704530123231772642623291899534454658707761230166809620539187116816778418242273580873637781313957589597
y = 116513882455567447431772208851676203256471727099349255694179213039239989833646726805040167642952589899809273716764673737423792812107737304956679717082391151505476360762847773608327055926832394948293052633869637754201186227370594688119795413400655007893009882742908697688490841023621108562593724732469462968731
c = 88688615046438957657148589794574470139777919686383514327296565433247300792803913489977671293854830459385807133302995575774658605472491904258624914486448276269854207404533062581134557448023142028865220726281791025833570337140263511960407206818858439353134327592503945131371190285416230131136007578355799517986306208039490339159501009668785839201465041101739825050371023956782364610889969860432267781626941824596468923354157981771773589236462813563647577651117020694251283103175874783965004467136515096081442018965974870665038880840823708377340101510978112755669470752689525778937276250835072011344062132449232775717960070624563850487919381138228636278647776184490240264110748648486121139328569423969642059474027527737521891542567351630545570488901368570734520954996585774666946913854038917494322793749823245652065062604226133920469926888309742466030087045251385865707151307850662127591419171619721200858496299127088429333831383287417361021420824398501423875648199373623572614151830871182111045650469239575676312393555191890749537174702485617397506191658938798937462708198240714491454507874141432982611857838173469612147092460359775924447976521509874765598726655964369735759375793871985156532139719500175158914354647101621378769238233
def chk(n):
    try:
        if 0 < n < c and pow(n,10 , (x * y * y * y)) == c:
            flag = bytes.fromhex(hex(n)[2:])
            if flag.startswith(b"flag"):
                print("Flag:", flag[:32])
                return 1
        return 0
    except:
        return 0

def cm(i,j):
    p=x
    q=y
    a=invert(p,q*q*q)*j%(q*q*q)
    b=invert(q*q*q,p)*i%p
    return (a*p+b*q*q*q)%(p*q*q*q) 

def doa(i):
    f=open("rot")
    x=f.read()
    f.close()
    x=x.split("\n")
    for kk in x:
        if len(kk)==0:
            continue
        j=int(kk)
        nn=cm(i,j)
        chk(nn)

ci=c%x
pi=invert(5,x-1)
ci=powmod(ci,pi,x)
syp=cipolla.modular_sqrt(ci,x)
doa(syp)
doa(x-syp)