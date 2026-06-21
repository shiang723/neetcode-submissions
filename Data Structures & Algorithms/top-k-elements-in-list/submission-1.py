class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        vals = list(count.values())
        for j in range(k):
            max_v = max(vals)
            vals.remove(max_v)
            key = [key for key, val in count.items() if val == max_v]
            del count[key[0]]
            ans.append(key[0])
        return ans
        