class LongestCommonPrefix():
    def longestCommonPrefix(self, strs):
        for i in range(0, len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    return strs[0][:i]
        return strs[0]
