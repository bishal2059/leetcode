from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        prev = 0 
        result = True
        n = len(bits) - 1
        for idx, digit in enumerate(bits):
            if digit == 1 and prev == 0:
                prev = 1
            elif digit == 1 and prev == 1:
                prev = 0
                result = False
            elif digit == 0 and prev == 1:
                prev = 0
                result = False
            elif digit == 0 and prev == 0:
                prev = 0
                result = True
            else:
                continue
        return result

if __name__ == "__main__":
    s = Solution()
    bits = [1, 0, 0]
    print(s.isOneBitCharacter(bits))  # Output: True
    bits = [1, 1, 1, 0]
    print(s.isOneBitCharacter(bits))  # Output: False
    bits = [0]
    print(s.isOneBitCharacter(bits))  # Output: True

        