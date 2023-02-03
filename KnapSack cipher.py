import random

print("\nKnapSack Cipher\n")


def generatePublicKeyList(privList: list, n: int, m: int):
    pubList = []
    for i in privList:
        pubList.append((i*m) % n)
    return pubList


def getNandM(privList: list):
    m = 0
    n = getNumberBiggerThan(sum(privList))
    for i in range(1, n+1):
        if (n % i != 0):
            m = i
            break
    print("\nMultiplier(m):", m, "\nModulus(n):", n,)
    return n, m


def getNumberBiggerThan(currSum: int):
    return int(random.random()*100 + currSum + 1)


def encrypt(pubList: list, bits: int):
    arr = list(map(int, str(bits)))
    print("Binary Equivalent of the Message:", arr)
    num = 0
    l = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            num = num + pubList[i]
    return num


def decrypt(num: int, d: int, n: int):
    dec = num*d % n
    print("\nDecryption Key:", dec)
    return dec


def binary(message: int):
    bits = bin(message)[2:]
    return bits


def exteuclid(a, b):

    r1 = a
    r2 = b
    s1 = int(1)
    s2 = int(0)
    t1 = int(0)
    t2 = int(1)

    while r2 > 0:

        q = r1//r2
        r = r1-q * r2
        r1 = r2
        r2 = r
        s = s1-q * s2
        s1 = s2
        s2 = s
        t = t1-q * t2
        t1 = t2
        t2 = t

    if t1 < 0:
        t1 = t1 % a

    return (r1, t1)


privList = [1, 5, 9, 22, 42, 57, 120, 167]  # Super Increasing Knapsack
print("Private List: ", privList)
n, m = getNandM(privList)
r, d = exteuclid(n, m)
pubList = generatePublicKeyList(privList, n, m)
print("Public Key:", pubList)

if r == 1:
    d = int(d)
    print("Multiplicative inverse of", m, "is:", d)

message = int(input("Message: "))


C = encrypt(pubList, binary(message))
print("\nCipher Text:", C)
decrypt(C, d, n)
