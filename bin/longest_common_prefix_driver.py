from libs.longest_common_prefix import LongestCommonPrefix


def main():
    r = LongestCommonPrefix()
    print(r.longestCommonPrefix(["flower","flow","flight"]))
    print(r.longestCommonPrefix(["dog","racecar","car"]))
    print(r.longestCommonPrefix(["",""]))
    print(r.longestCommonPrefix(["abc","abcd", "ab"]))
    return 0


if __name__ == "__main__":
    main()