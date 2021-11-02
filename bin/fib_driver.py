from libs.fibonacci import Fibonacci


def main():
    r = Fibonacci()
    print(r.fibTab(0))
    print(r.fibTab(1))
    print(r.fibTab(2))
    print(r.fibTab(3))
    print(r.fibTab(4))
    print(r.fibTab(5))
    print(r.fibTab(6))
    print(r.fibTab(7))
    print(r.fibTab(8))
    print(r.fibLookUp(8))
    return 0


if __name__ == "__main__":
    main()
