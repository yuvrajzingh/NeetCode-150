from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            if num-1 not in num_set:
                curr_num = num
                curr_count = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_count += 1
                max_count = max(max_count, curr_count)
        
        return max_count