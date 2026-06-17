class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # for i in range(len(nums)):
        #     res = abs(target - nums[i] )
        #     if res in nums:
        #         return [i,nums.index(res)]
        
        helper_dict = {}
        for ind,num in enumerate(nums):
            res = target-num
          
            if num in helper_dict:
                return [helper_dict.get(num),ind]
            else:
                helper_dict[res] = ind


        return None
        