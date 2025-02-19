from typing import List
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_num = [int(x) for x in nums]
        sorted_arr = sorted(int_num,reverse=True)
        print(sorted_arr)
        return str(sorted_arr[k-1])
    
if __name__ =="__main__":
    s = Solution()
    print(s.kthLargestNumber(["3","6","7","10"], 4)) # 3
    print(s.kthLargestNumber(["2","21","12","1"], 3)) # 2
    print(s.kthLargestNumber(["0","0"], 2)) # 0