class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        num_list = list(number)
        max = 0
        print(num_list)
        for i,x in enumerate(num_list):
            # print(x)
            if x == digit:
                check_list = num_list.copy()
                check_list.pop(i)
                test_num = int(''.join(check_list))
                # print(test_num)
                if  test_num > max:
                    max = test_num
        return str(max)
        
if __name__=="__main__":
    number = "123"
    digit = "2"
    result = Solution().removeDigit(number, digit)
    print(result)
# Output: 13