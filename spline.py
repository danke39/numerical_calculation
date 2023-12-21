import numpy as np

#xi=write data
#y=write data
h=[]
#M=number of data
#N=M-1
for i in range(N):
    h.append(xi[i+1]-xi[i])
#adjust H,v,tmp size
H=np.array([[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]])
v=np.array([0.0,0.0,0.0,0.0])
tmp=np.array([0.0,0.0,0.0,0.0])
for i in range(N-1):
    if i!=0:
        H[i][i-1]=h[i]
    H[i][i]=2*(h[i]+h[i+1])
    if i!=3:
        H[i][i+1]=h[i+1]
    v[i]=6*((y[i+2]-y[i+1])/h[i+1]-(y[i+1]-y[i])/h[i])
#adjust n
n = 4
A = H
b = v

r = b - A @ tmp
p=r
for k in range(1,1000):
    y1 = A @ p
    tmp1=np.dot(r, r)
    if np.abs(np.dot(p, y1))<1e-6:
        break
    alpha1 = tmp1 / np.dot(p, y1)
    tmp += alpha1 * p
    r -= alpha1 * y1
    print(k, tmp)
    if np.linalg.norm(r) < 1e-10:
        break
    beta = np.dot(r, r) / tmp1
    p = r + beta * p
print("tmp=",tmp)
ca=np.zeros(N,float)
cb=np.zeros(N,float)
cc=np.zeros(N,float)
cd=np.zeros(N,float) 
#adjust u size
u=np.array([0.0,0.0,0.0,0.0,0.0,0.0])
for i in range(N-1):
    u[i+1]=tmp[i]
for i in range(N):
    ca[i]=(u[i+1]-u[i])/(6.0*h[i])
    cb[i]=u[i]/2.0
    cc[i]=(y[i+1]-y[i])/h[i]-h[i]*(2*u[i]+u[i+1])/6.0
    cd[i]=y[i]
print(ca)
print(cb)
print(cc)
print(cd)
