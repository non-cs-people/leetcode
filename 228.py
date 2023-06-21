class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        range_lst = []
        if not nums:
            return range_lst

        start = nums[0]
        end = nums[0]
        length = len(nums)

        for i in range(1, length):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    range_lst.append(str(start))
                else:
                    range_lst.append(str(start) + '->' + str(end))

                start = nums[i]
                end = nums[i]
        
        if start == end:
            range_lst.append(str(start))
        else:
            range_lst.append(str(start) + '->' + str(end))

        return range_lst