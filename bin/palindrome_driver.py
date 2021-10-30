from libs.palindrome import Palindrome

def main():
        p=Palindrome()
        n=22222222
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        n=223
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        n=5
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        n=-55
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        n=55
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        n=121
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        n=10
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        n=11
        print("{} is palindrome: {}".format(n,p.is_palindrome(n)))
        return 0

if __name__ == "__main__":
        main()