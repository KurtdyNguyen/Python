def divisor(x, a):
    for i in range(1,x+1):
        if x % i == 0:
            a.append(i)

def digitsum(x):
    s = 0
    for i in range(0,len(str(x))):
        s += x // (10**i) % 10
    return s

def maxVal(a1, a2):
    a2.append(a1[0])
    for i in range(0, len(a1)-1):
        if digitsum(a1[i+1]) > digitsum(a1[i]):
            a2.pop()
            a2.append(a1[i+1])
        elif digitsum(a1[i+1]) == digitsum(a1[i]):
            a2.append(a1[i+1])
        else:
            break

a1 = []
a2 = []
x = int(input())
divisor(x, a1)
maxVal(a1, a2)
print(min(a2))