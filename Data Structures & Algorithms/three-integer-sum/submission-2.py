class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        results = []

        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l<r:
                tsum = num + nums[l] + nums[r]
                if tsum > 0 :
                    r -=1 
                elif tsum < 0:
                    l +=1 
                else:
                    results.append(sorted([num,nums[l],nums[r]]))
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        print(results)
        # return list(set(results))
        return results

        

        