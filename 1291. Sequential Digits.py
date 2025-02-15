from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output = []
        num_list = ['1','2','3','4','5','6','7','8','9']
        low_length = len(str(low))
        high_length = len(str(high))
        def give_nums(x):
            temp = []
            i = 0
            while i < 10-x:
                s_num = ''.join(num_list[i:i+x])
                temp.append(int(s_num))
                i +=1
            return temp
        for i in range(low_length,high_length+1):
            current_arr = give_nums(i)
            # print(current_arr)
            for x in current_arr:
                if x < low:
                    continue
                if x > high:
                    break
                output.append(x)
        return output

if __name__ == "__main__":
    s = Solution()
    print(s.sequentialDigits(100,300))  # Output: [123,234]
    print(s.sequentialDigits(1000,13000))  # Output: [1234,2345,3456,4567,5678,6789,12345]