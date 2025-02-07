from typing import List
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        index = -1
        while i<n:
            first = sum(nums[:i])
            last = sum(nums[i+1:])
            if first == last:
                index = i
                break
            else:
                i += 1
        return index

if __name__ == "__main__":
    nums = [2,3,-1,8,4]
    s = Solution()
    print(s.findMiddleIndex(nums))