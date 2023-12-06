import numpy as np

def forward(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(0,n):
        temp = b[i]
        for j in range(0,i):
            temp -= L[i][j] * y[j]
        y[i] = temp / L[i][i]
    return y

def backward(L_T, y):
    n = len(L_T)
    x = np.zeros(n)
    for i in reversed(range(0,n)):
        temp = y[i]
        for j in range(i+1, n):
            temp -= L_T[i][j] * x[j]
        x[i] = temp / L_T[i][i]
    return x

n = 4
A = np.array([[20.0, -1.0, 0.0, 0.0],
              [-1.0, 5.0, -2.0, 0.0],
              [0.0, -2.0, 11.0, -3.0],
              [0.0, 0.0, -3.0, 6.0]])
b = np.array([2.0, 0.0, 2.0, 3.0])

L = np.zeros((n, n))

L[0][0] = np.sqrt(A[0][0])

for i in range(1, n):
    for j in range(i):
        temp = A[i][j]
        for k in range(0,j):
            temp -= L[i][k] * L[j][k]
        L[i][j] = temp / L[j][j]
    L[i][i] = np.sqrt(A[i][i] - np.dot(L[i], L[i]))

L_T = L.T
x = np.zeros(n)
r = b - A @ x
y = forward(L, r)
z = backward(L_T, y)

for k in range(1,1000):
    Ap = A @ z
    alpha = np.dot(z, r) / np.dot(z, Ap)
    x += alpha * z
    r -= alpha * Ap
    print(k, x)
    if np.linalg.norm(r) < 1e-6:
        break
    beta = np.dot(r, r) / np.dot(y, y)
    y = forward(L, r)
    z = y - beta * z

print("解:", x)

#前処理無し
n = 4
A = np.array([[20.0, -1.0, 0.0, 0.0],
              [-1.0, 5.0, -2.0, 0.0],
              [0.0, -2.0, 11.0, -3.0],
              [0.0, 0.0, -3.0, 6.0]])
b = np.array([2.0, 0.0, 2.0, 3.0])

x = np.array([0.0,0.0,0.0,0.0])
r = b - A @ x
p=r
for k in range(1,1000):
    y = A @ p
    tmp=np.dot(r, r)
    if np.abs(np.dot(p, y))<1e-6:
        break
    alpha1 = tmp / np.dot(p, y)
    x += alpha1 * p
    r -= alpha1 * y
    print(k, x)
    if np.linalg.norm(r) < 1e-6:
        break
    beta = np.dot(r, r) / tmp
    p = r + beta * p

print("解:", x)