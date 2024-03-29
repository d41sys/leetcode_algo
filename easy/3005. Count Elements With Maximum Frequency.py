
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        # define 
        fre = 1
        maxfre = -1
        # finding max frequency
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                fre += 1
            if fre > maxfre:
                maxfre = fre
            if nums[i] != nums[i-1]:
                fre = 1
            
        # check case [1,1,1,1]
        if maxfre == len(nums) or maxfre == 1:
            return len(nums)

        # check fre
        fre = 1
        sumfre = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                fre = 1
            if nums[i] == nums[i-1]:
                fre += 1
            if fre == maxfre:
                sumfre+=maxfre
        
        return sumfre