from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        array = sorted(nums)
        sum = 0
        i = 0
        while i < len(array):
            sum += min(array[i],array[i+1])
            i += 2
        return sum
    
if __name__=="__main__":
    arr = [1,4,3,2]
    print(Solution().arrayPairSum(arr))  # Output: 4
    arr = [6,2,6,5,1,2]
    print(Solution().arrayPairSum(arr))  # Output: 9