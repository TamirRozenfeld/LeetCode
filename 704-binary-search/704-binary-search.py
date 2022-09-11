class Solution(object):
    def search(self, nums, target):
        
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = (left + right) //2
            if target > nums[mid]:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
        
        