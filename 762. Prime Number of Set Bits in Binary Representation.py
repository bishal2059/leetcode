class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left,right+1):
            num = i 
            binary = []
            while num > 0:
                binary.append(num % 2)
                num = num // 2 
            count_one = binary.count(1)
            # print(count_one)
            if count_one > 1:
                for i in range(2, (count_one//2)+1):
                    if (count_one % i) == 0:
                        break
                else:
                    count += 1
            else:
                continue
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countPrimeSetBits(6,10))  # Output: 4
    print(s.countPrimeSetBits(10,15))  # Output: 5

