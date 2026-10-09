class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r=set(nums)
        if len(nums)==len(r):
            return False
        else:
            return True