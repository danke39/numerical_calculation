import numpy as np
import matplotlib.pyplot as plt

#change below differential equation to yours
m=1.0
k=0.5+0.001*20*11
c=0.0025*(20+11)
g=9.8

y0=0.0
v0=0.0

def f(t,y,v):
    dy_dt=v
    dv_dt=-k/m*y-2*c*v/m+g
    return dy_dt,dv_dt

def rk4(f,y0,v0,t0,tn,n):
    h=(tn-t0)/n
    t=t0
    y=y0
    v=v0
    
    t_values=[t]
    y_values=[y]
    v_values=[v]
    
    for i in range(n):
        dy1,dv1=f(t,y, v)
        dy2,dv2=f(t+h/2,y+h/2*dy1,v+h/2*dv1)
        dy3,dv3=f(t+h/2,y+h/2*dy2,v+h/2*dv2)
        dy4,dv4=f(t+h,y+h*dy3,v+h*dv3)
        
        y=y+h/6*(dy1+2*dy2+2*dy3+dy4)
        v=v+h/6*(dv1+2*dv2+2*dv3+dv4)
        t=t+h
        if i==1000:
            print(y)
        t_values.append(t)
        y_values.append(y)
        v_values.append(v)
        
    return t_values,y_values,v_values

t0=0.0
tn=50.0
n=5000
t_values,y_values,v_values=rk4(f,y0,v0,t0,tn,n)

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(t_values,y_values,label='y(t)')
plt.xlabel('Time (s)')
plt.ylabel('y')
plt.title('y(t)')
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(t_values,v_values,label='v(t)',color='orange')
plt.xlabel('Time (s)')
plt.ylabel('v')
plt.title('v(t)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()