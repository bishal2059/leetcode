class Solution:
    def getLucky(self, s: str, k: int) -> int:
        str_num = [f'{(ord(x)-96)}' for x in s]
        list_digits = [int(x) for x in list(''.join(str_num))]
        num = sum(list_digits)
        # print(num)
        for _ in range(k-1):
            num = sum(int(digit) for digit in str(num))
        return num
    
if __name__ == '__main__':
    s = Solution()
    print(s.getLucky('iiii', 1))
    print(s.getLucky('leetcode', 2))
    print(s.getLucky('zbax', 2))
