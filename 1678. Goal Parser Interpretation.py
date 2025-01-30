class Solution:
    def interpret(self, command: str) -> str:
        x = command
        final = ''
        for i in range(len(x)):
            if x[i] == '(' and x[i+1] == ')':
                final = final + 'o'
            elif x[i] == '(' and x[i+1] == 'a':
                final = final + 'al'
            elif x[i] == 'G':
                final = final + 'G'
            else:
                continue
        return final

if __name__ == "__main__":
    s = Solution()
    print(s.interpret("G()(al)"))
    print(s.interpret("G()()()()(al)"))
    print(s.interpret("(al)G(al)"))