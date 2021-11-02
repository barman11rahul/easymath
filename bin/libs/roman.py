class Roman():
    def __init__(self):
        self.rm = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s):
        sum = 0
        prev = 1001
        for alphabet in s:
            current = self.rm[alphabet]
            if(current <= prev):
                sum += current
            else:
                sum = sum - prev + (current-prev)
            prev = current
        return sum
