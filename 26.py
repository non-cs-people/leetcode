class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        curr = nums[0]
        length = len(nums)
        
        for i in range(1, length):
            if nums[i] != curr:
                nums[index] = nums[i]
                curr = nums[i]
                index += 1
        return index