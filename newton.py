def f(x,a):
    return x**2-a
def dfdx(x,a):
    dx=1e-10
    dfdx=(f(x+dx,a)-f(x,a))/dx
    return dfdx

print("input number\n")
a=int(input())
print("input start num\n")
start=float(input())
x=start
de=1

i=0
print("i=",i,"x=",x,"de=",de)
while de >1e-6:
    i+=1
    xnew=(x*dfdx(x,a)-f(x,a))/dfdx(x,a)
    de=f(xnew,a)
    x=xnew
    print("i=",i,"x=",xnew,"de=",de)
print("x=",x,",i=",i)
