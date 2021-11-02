from libs.roman import Roman


def main():
    r = Roman()
    s = 'III'
    print("{} roman to int: {}".format(s, r.romanToInt(s)))
    s = 'LVIII'
    print("{} roman to int: {}".format(s, r.romanToInt(s)))
    s = 'IX'
    print("{} roman to int: {}".format(s, r.romanToInt(s)))
    s = 'IV'
    print("{} roman to int: {}".format(s, r.romanToInt(s)))
    s = 'LIV'
    print("{} roman to int: {}".format(s, r.romanToInt(s)))
    s = 'XLV'
    print("{} roman to int: {}".format(s, r.romanToInt(s)))
    return 0


if __name__ == "__main__":
    main()
