import numpy as np

print("input coefficient")
c=input().split()

for i in range(len(c)):
    c[i]=float(c[i])

def f(x):
    return c[0]*x[0]**2+c[1]*x[1]**2+c[2]*x[0]*x[1]+c[3]*x[0]+c[4]*x[1]+c[5]

def koubai(f,x):
    h=1e-6
    g=np.zeros_like(x)
    for idx in range(0,2):
        tmp=x[idx]
        x[idx]=tmp+h
        fxh1=f(x)
        x[idx]=tmp-h
        fxh2=f(x)
        g[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp
    return g

#係数一定
x=np.array([0.0,0.0])
alpha=0.5
for i in range(1,1000):
    dx=koubai(f,x)
    norm=0.0
    for j in range(0,2):
        dx[j]*=alpha
        x[j]-=dx[j]
        norm+=dx[j]*dx[j]
    print("i=",i,"x=",x,"f(x)=",f(x))
    norm=np.sqrt(norm)
    if(norm<1e-6):
        break
print("解",x,"f(x)=",f(x))

#係数を漸減
x=np.array([0.0,0.0])
for i in range(1,1000):
    dx=koubai(f,x)
    norm=0.0
    for j in range(0,2):
        dx[j]/=i
        x[j]-=dx[j]
        norm+=dx[j]*dx[j]
    print("i=",i,"x=",x,"f(x)=",f(x))
    norm=np.sqrt(norm)
    if(norm<1e-6):
        break
print("解",x,"f(x)=",f(x))