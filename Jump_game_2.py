class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            print(nxt)
            l, r = r, nxt
        return times
        #Time limit Exceed
#         if len(nums) == 1:
#             return 0
#         number_of_jumps = [999999]*(len(nums))
#         number_of_jumps[0] = 0
#         # i = 1
#         for i in range(1,len(nums)):
#             for j in range(i):
#                 if (nums[j]+j) >= i:
#                     # print(j)
#                     number_of_jumps[i] = min(number_of_jumps[i],number_of_jumps[j]+1)
#                     # nums[i] = min(nums[i],nums[j]+1)
#             i += 1
#         # print(number_of_jumps)
#         return number_of_jumps[-1]
                
                
                
        
        