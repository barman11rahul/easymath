class LIS():
    def findLis(self, arr):
        sizeOfArr = len(arr)
        lis = [1] * sizeOfArr
        max_num = 1
        for i in range(1, sizeOfArr):
            for j in range(0, i):
                if(arr[j] < arr[i]):
                    lis[i] = max(lis[i], 1 + lis[j])
            if(max_num < lis[i]):
                max_num = lis[i]
        return max_num
