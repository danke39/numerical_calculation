import numpy as np
import matplotlib.pyplot as plt
#change below differential equation to yours
m=1.0
k=0.5+0.001*20*11
c=0.0025*(20+11)
g=9.8

y1_0=0.0
v1_0=0.0
y2_0=5.0
v2_0=0.0

def f(t,y1,v1,y2,v2):
    dy1_dt=v1
    dv1_dt=-k/m*y1-2*c*v1/m+g
    dy2_dt=v2
    dv2_dt=-k/m*(y2-y1)-2*c*v2/m+g
    return dy1_dt,dv1_dt,dy2_dt,dv2_dt

def rk4(f,y1_0,v1_0,y2_0,v2_0,t0,tn,n):
    h=(tn-t0)/n
    t=t0
    y1=y1_0
    v1=v1_0
    y2=y2_0
    v2=v2_0
    
    t_values=[t]
    y1_values=[y1]
    y2_values=[y2]
    
    for i in range(n):
        dy1_1,dv1_1,dy2_1,dv2_1=f(t,y1,v1,y2,v2)
        dy1_2,dv1_2,dy2_2,dv2_2=f(t+h/2,y1+h/2*dy1_1,v1+h/2*dv1_1,y2+h/2*dy2_1,v2+h/2*dv2_1)
        dy1_3,dv1_3,dy2_3,dv2_3=f(t+h/2,y1+h/2*dy1_2,v1+h/2*dv1_2,y2+h/2*dy2_2,v2+h/2*dv2_2)
        dy1_4,dv1_4,dy2_4,dv2_4=f(t+h,y1+h*dy1_3,v1+h*dv1_3,y2+h*dy2_3,v2+h*dv2_3)
        
        y1=y1+h/6*(dy1_1+2*dy1_2+2*dy1_3+dy1_4)
        v1=v1+h/6*(dv1_1+2*dv1_2+2*dv1_3+dv1_4)
        y2=y2+h/6*(dy2_1+2*dy2_2+2*dy2_3+dy2_4)
        v2=v2+h/6*(dv2_1+2*dv2_2+2*dv2_3+dv2_4)
        t=t+h
        
        t_values.append(t)
        y1_values.append(y1)
        y2_values.append(y2)
        
    return t_values,y1_values,y2_values

t0=0.0
tn=50.0
n=5000

t_values,y1_values,y2_values=rk4(f,y1_0,v1_0,y2_0,v2_0,t0,tn,n)
plt.figure(figsize=(18,6))
plt.subplot(1,2,1)
plt.plot(t_values,y1_values,label='y1(t)')
plt.plot(t_values,y2_values,label='y2(t)')
plt.xlabel('Time (s)')
plt.ylabel('y')
plt.title('y1(t),y2(t)')
plt.legend()
plt.show()