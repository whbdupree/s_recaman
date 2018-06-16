from threading import Thread

class recaman(Thread): 
    def __init__(self,s,q):
        self.s = s # offset
        self.x = [0]*(q+1)  #allocate list at start
        self.x[0] = 1+s
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
        return b
    def run(self):
        for i in range(self.q):
            n = i+2 # start at n=2
            self.x[i+1]=self.eval(self.x[i],n)

if __name__=='__main__':
    rlist = [ recaman(n,20) for n in range(5) ]
    for r in rlist:
        r.start()
    for r in rlist:
        r.join()
        print(r.x)
