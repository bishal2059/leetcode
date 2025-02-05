from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = digits
        n = len(number) - 1
        carry = 0
        while n >= 0:
            if carry == 0:
                sum = number[n] + carry + 1
            else:
                sum = number[n] + carry
            if sum > 9:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            number[n] = sum
            if carry == 0:
                break
            n -= 1
            if n < 0 and carry == 1:
                number.insert(0,carry)
        return number
        

if __name__ == "__main__":
    digits = [9,9,9]
    obj = Solution().plusOne(digits)
    print(obj)
