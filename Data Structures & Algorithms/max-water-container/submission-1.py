class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        sol = (r-l)*min(heights[r], heights[l])
        for i in range(len(heights)):
            if heights[l] < heights[r]:
                l+=1
            else: 
                r-=1
            curr = (r-l)*min(heights[r], heights[l])
            if (curr > sol):
                sol = curr
        return sol