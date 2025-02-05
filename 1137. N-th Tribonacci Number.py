class Solution:
    def tribonacci(self, n: int) -> int:
        # trib_list = [0,1,1]
        # i = 3
        # while i <= n:
        #     trib_list.append(trib_list[i-1] + trib_list[i-2] + trib_list[i-3])
        #     i += 1
        # return trib_list[n]
        if n < 3:
            return 0 if n == 0 else 1

        a, b, c = 0, 1, 1

        for i in range(2, n):
            a, b, c = b, c, a + b + c

        return c

if __name__ == "__main__":
    n = 25
    s = Solution()
    print(s.tribonacci(n))