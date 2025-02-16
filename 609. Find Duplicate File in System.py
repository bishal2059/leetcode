from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hm ={}
        for x in paths:
            path_file = x.split(' ')
            i = 1
            while i < len(path_file):
                s = path_file[i]
                start = s.index("(") + 1
                end = s.index(")")
                res = s[start:end]
                if res not in hm:
                    hm[res] = []
                hm[res].append(path_file[0] + "/" + s[:start-1])
                i +=1
        output = []
        for y in hm.values():
            if len(y) > 1:
                output.append(y)
        return output

if __name__ =="__main__":
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    s = Solution()
    print(s.findDuplicate(paths)) # [['root/a/1.txt', 'root/4.txt'], ['root/c/3.txt', 'root/c/d/4.txt']]
    paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)", "root/c 3.txt(abdfcd)", "root/c/d 4.txt(efggdfh)"]
    print(s.findDuplicate(paths)) # []