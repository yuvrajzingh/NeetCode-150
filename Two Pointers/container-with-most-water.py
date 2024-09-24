from typing import List

class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxVol, vol = 0,0
        l = 0
        r = len(nums)-1

        while l<r:

            if nums[l] <= nums[r]:
                vol = nums[l] * abs(r-l)
                l+=1
            else:
                vol = nums[r] * abs(r-l)
                r-=1
            maxVol = max(vol, maxVol)
        return maxVol