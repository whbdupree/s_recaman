s = 5
x = [1]
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

for i in range(10):
    recaman(x[-1],i+2)
print(x)
