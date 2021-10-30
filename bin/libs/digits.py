class Digits():
    def find_digits(self, x):
        s=1
        e=10
        for d in range(1,11):
            if(x>=s and x<e and x>=0):
                return d, s
            s*=10
            e*=10