class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        
        for n in(nums):
            if (n-1) not in numSet:
                lenght = 0
                while (n + lenght) in numSet:
                    lenght += 1
                longest = max(lenght, longest)
        return longest
        