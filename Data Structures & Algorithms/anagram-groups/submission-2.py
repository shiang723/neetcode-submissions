class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            ana = []
            sol = []
            for s in strs:
                chars = {}
                print(s)
                for char in s:
                    chars[char] = chars.get(char, 0)+1
                    print(chars)
                if chars in ana:
                    ind = ana.index(chars)
                    sol[ind].append(s)
                else:
                    ana.append(chars)
                    sol.append([s])
                    print(sol)   
            return sol