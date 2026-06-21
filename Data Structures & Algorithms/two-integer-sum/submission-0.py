class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use target - ind[i] = difference
        diffs = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diffs.get(diff) == None:
                diffs.update({nums[i]:i})
            else:
                return [diffs.get(diff), i]
        return [0]
        