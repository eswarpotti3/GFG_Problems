class Solution:
    def majorityElement(self, nums):
        nums.sort()
        
        if nums.count(nums[len(nums)//2])>len(nums)//2:
            return nums[(len(nums)//2)]
        return -1