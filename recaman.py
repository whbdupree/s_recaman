s = 0
x = [1+s]
def recaman(a,n):
    b = a - (n+s)
    if b > 0:
        try:
            x.index(b)
            b = a + (n+s)
        except ValueError:
            pass
    else:
        b = a + (n+s)
    x.append(b)

for i in range(20):
    recaman(x[-1],i+2)
print(x)
