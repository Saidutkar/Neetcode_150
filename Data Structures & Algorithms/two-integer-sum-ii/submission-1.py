class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmp = {}

        for i  in range(0,len(numbers)):
            res = target - numbers[i]
            if numbers[i] in hashmp:
                return [hashmp[numbers[i]]+1, i+1]
            else:
                hashmp[res] = i