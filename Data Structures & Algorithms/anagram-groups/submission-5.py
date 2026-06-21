class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        if len(strs) <= 1:
            sol.append(strs)  
        else:    
            ana = []
            for s in strs:
                chars = {}
                for char in s:
                    chars[char] = chars.get(char, 0)+1
                if chars in ana:
                    ind = ana.index(chars)
                    sol[ind].append(s)
                else:
                    ana.append(chars)
                    sol.append([s])
        return sol