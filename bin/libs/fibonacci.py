class Fibonacci():
    def fibTab(self, n):
        if(n<1):
            return n
        tab = [0] * (n+1)
        tab[1] = 1
        for i in range(2, n+1):
            tab[i] = tab[i-1] + tab[i-2]
        
        return tab[n]

    def fibLookUp(self, n):
        if(n<1):
            return n
        l={}
        l[0]=0
        l[1]=1
        for i in range(2, n+1):
            l[i] = l[i-1] + l[i-2]
        
        return l[n]
