
#Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        ans=nums
        return nums + ans
#Running Sum of 1d Array
 class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        total=0
        for i in range(0,len(nums)):
            total+=nums[i]
            ans.append(total)
        return ans
                       
