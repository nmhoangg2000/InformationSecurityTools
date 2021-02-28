from Cayley import cayley
from eulerphi import eulerphi
from sympy import *

p = int(input("p: "))
while isprime(p) == false:
    print("p must be prime")
    p = int(input("p: "))

q = int(input("q: "))
while isprime(q)==false:
    print("q must be prime")
    p = int(input("q: "))
N = p*q
table = cayley(eulerphi(N))
choice = input("e or d was given? ")
if choice == "e":
	e = int(input("e: "))
	for i in range(N):
	    if table[e][i] == 1:
	        d = i
	        break
elif choice == "d":
	d = int(input("d: "))
	for i in range(N):
	    if table[d][i] == 1:
	        e = i
	        break

print("Choose 1 option:")
print("1. Encryption")
print("2. Decryption")
choice = int(input())
if choice == 1:
    M = int(input("Input plaintext M: "))
    C = M
    expo = bin(e)[2:]
    for i in range(1, len(expo)):
        C = (C ** 2) % N
        if expo[i] == "1":
            C = (C * M) % N
    print('Key pair for encrytion: ({n},{e}) '.format(n=N, e=e))
    print('Secret key for decryption: {}'.format(d))
    print('Plaintext: {} '.format(M))
    print('Ciphertext: {}'.format(C))
elif choice == 2:
    C = int(input("Input ciphertext C: "))
    M = C
    expo = bin(d)[2:]
    for i in range(1, len(expo)):
        M = (M ** 2) % N
        if expo[i] == "1":
            M = (M * C) % N
    print('Key pair for encrytion: ({n},{e}) '.format(n=N, e=e))
    print('Secret key for decryption: {}'.format(d))
    print('Ciphertext: {}'.format(C))
    print('Plaintext: {}'.format(M))
