from libs.lis import LIS


def main():
    r = LIS()
    print(r.findLis([2,3,1,-4]))
    print(r.findLis([1,2,3,2,-1]))
    print(r.findLis([1,3,2,10]))
    print(r.findLis([1,2,3,4,5]))
    print(r.findLis([4,3,2,1]))
    return 0


if __name__ == "__main__":
    main()