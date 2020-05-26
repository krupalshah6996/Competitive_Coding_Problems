class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = minprod = answer = nums[0]
        for i in range(1,len(nums)):
            x = max(nums[i], minprod*nums[i],maxprod*nums[i])
            y = min(nums[i], minprod*nums[i],maxprod*nums[i])
            maxprod, minprod = x,y
            answer = max(maxprod,answer)
        return answer
        