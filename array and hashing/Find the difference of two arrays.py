# typical approach using hash table 
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ht = {}
        yt = {}
        for num in nums1:
            if num not in nums2:
                if num in ht:
                    ht[num] +=1
                else:
                    ht[num] = 1

        for num in nums2:
            if num not in nums1:
                if num in yt:
                    yt[num] +=1
                else:
                    yt[num] = 1

        return [ht.keys(),yt.keys()]
    
# One liner using hashset 
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]