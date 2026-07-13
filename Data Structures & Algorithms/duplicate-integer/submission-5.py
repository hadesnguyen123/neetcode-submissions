class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap
        hasmap = {}
        for key in nums:
            if hasmap.get(key):
                hasmap[key] += 1
                if hasmap[key] == 2:
                    return True
            hasmap[key] = 1
        return False