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
            
