class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        i = 2
        j = n
        sum1 = 1
        sum2 = 0
        while (i != j):
            if sum1 < sum2:
                sum1 += i
                i += 1
            elif sum1 > sum2:
                sum2 += j
                j -= 1
            else:
                sum1 += i
                sum2 += j
                if j-i == 1:
                    break
                i += 1
                j -= 1
        if sum1 == sum2:
            return i
        return -1