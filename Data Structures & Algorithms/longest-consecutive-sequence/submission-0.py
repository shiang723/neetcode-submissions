class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        sol = 0

        for n in set_num:
            if (n - 1) not in set_num:
                length = 1
                while (n + length) in set_num:
                    length += 1
                sol = max(length, sol)
        return sol

            


        