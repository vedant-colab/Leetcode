class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashs = set()
        for num in nums:
            if num in hashs:
                return True

            hashs.add(num)

        return False
