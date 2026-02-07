class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums)//2]