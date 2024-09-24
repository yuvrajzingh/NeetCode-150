from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1

        while i<j:
            if(nums[i] + nums[j] == target):
                return [i+1, j+1]
            elif (nums[i] + nums[j] > target):
                j-=1
            else:
                i+=1