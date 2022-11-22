from gettext import find

def balance_check(x):
    bracket = ['()','[]','{}']
    while any(i in x for i in bracket):
        for br in bracket:
            x = x.replace(br, '')
    return not x

def precede_succeed(x):
    open = ['(','[','{']
    close = [')',']','}']
    for i in x:
        if i in open:
            i0 = x[x.find(i)+1]
            if i0 in close and open.index(i)!=close.index(i0):
                return False

p = True
x = str(input())
while len(x)<1 or len(x)>100:
    x = str(input())
x1 = x
p = balance_check(x)
if p:
    precede_succeed(x1)
print('TRUE' if p == True else 'FALSE')