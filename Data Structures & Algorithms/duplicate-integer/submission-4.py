class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  bruth force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] :
        #             return True
        # return False

        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
        
        #set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False