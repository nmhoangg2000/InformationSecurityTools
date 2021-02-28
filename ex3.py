def powe(x, e, n):
    if(e==0):
        return 1
    if(e==1):
        return x%n
    tmp = powe(x,e//2,n)
    tmp = (tmp * tmp)%n
    if(e%2==1):
        tmp =(tmp * (x%n))%n
    return tmp

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def RSA(p,q,e):
    n = p*q
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    return (n,e,d)

def encry(e,n,M):
    return powe(M,e,n)

def decry(c,d,n):
    return powe(c,d,n)

test1 = RSA(5,11,3)
n = test1[0]
e = test1[1]
d = test1[2]
C = encry(e,n,9)
print(C)
m = decry(C,d,n)
print(m)

test2 = RSA(41,17,49)
n = test2[0]
e = test2[1]
d = test2[2]
C = encry(e,n,600)
print(C)
m = decry(C,d,n)
print(m)