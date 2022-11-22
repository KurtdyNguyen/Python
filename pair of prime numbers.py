def getRange(s, M):
    a = list(map(int,str(s).split(' ')))
    M.append(a)

def getPrime(a, x):
    prime = True
    for i in range(2, int(x/2)+1):
        if x % i == 0:
            prime = False
            break
    if prime == True:
        a.append(x)

def count(a):
    c = 0
    for i in a:
        if i+6 in a:
            c+=1
    return c

a = []
M = []
n = int(input())
for i in range(n):
    s = str(input())
    getRange(s, M)
    a.append([])
    for j in range(M[i][0], M[i][1]+1):
        getPrime(a[i], j)

for i in range(n):
    print(count(a[i]))