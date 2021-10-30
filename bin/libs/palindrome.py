from libs.digits import Digits
class Palindrome():
    def is_palindrome(self,n):
        if(n==0):
            return True
        elif(n>0):
            digits = Digits()
            d,e=digits.find_digits(n)
            s=1
            for i in range(1, int(d/2)+1):
                leftd=int((n/e)%10)
                rightd=int((n/s)%10)
                if(leftd!=rightd):
                    return False
                e/=10
                s*=10
            return True
        else:
            return False
