class Solution:
    def sortSentence(self, s: str) -> str:
        final = ''
        hm = {}
        current = ''
        for x in s:
            if x == ' ':
                current = ''
            elif x.isnumeric():
                hm[x] = current
            else:
                current = current + x
        count = len(hm.keys())    
        for i in range(count):
            if i+1 >= count:
                final = final + hm[f'{i+1}'] 
            else:
                final = final + hm[f'{i+1}'] + ' '
        
        return final
            
if __name__=="__main__":
    s = "is2 sentence4 This1 a3"
    sorted_sentence = Solution().sortSentence(s)
    print(sorted_sentence)
