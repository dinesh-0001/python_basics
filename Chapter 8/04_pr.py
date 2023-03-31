def max(a, b, c):
    if(a>b):
        if(a>c):
            return a
        else : 
            return c
    else: 
        if(b>c):
            return b
        else: 
            return c

e = int(input("Number 1\n"))
f = int(input("Number 2\n"))
g = int(input("Number 3\n"))
m = max(e, f, g)
print('The Maximum Value is', str((m)))
