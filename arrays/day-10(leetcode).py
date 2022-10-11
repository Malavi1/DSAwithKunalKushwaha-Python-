#Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sample=[]
        for i in accounts:
            sample.append(sum(i))
        return max(sample)
      
#Increasing Triplet Subsequence      
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = third = float('inf')
        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            elif nums[i] <= third:
                third = nums[i]
        return float('inf') not in [first, second, third]
                    
