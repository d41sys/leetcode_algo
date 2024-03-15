
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 1 and len(nums2) == 1:
            return -1
        common = set(nums1) & set(nums2)
        if list(common) != []:
            return min(list(common))
        return -1
