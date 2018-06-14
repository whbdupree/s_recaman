from threading import Thread

class recaman(Thread): 
    def __init__(self,s,q):
        self.s = s # offset
        self.x = [1+s] # list holds sequence starting at 1+s
        self.q = q # how may steps
        super(recaman, self).__init__()
    def eval(self,a,n):
        ns = n+self.s # might use it twice
        b = a - ns
        if b > 0:
            try:
                self.x.index(b)
                b = a + ns
            except ValueError:
                pass
        else:
            b = a + ns
        self.x.append(b)
    def run(self):
        for i in range(self.q):
            self.eval(self.x[-1],i+2)

if __name__=='__main__':
    rlist = [ recaman(n,20) for n in range(5) ]
    for r in rlist:
        r.start()
    for r in rlist:
        r.join()
        print(r.x)
