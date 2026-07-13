class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution 1: for loop 2 vòng để get ra phần tử cần
        # (On^2)
        # n = len(numbers)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1] 
        
        # solution 2: hashmap
        seen = {}
        for i,num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff] + 1, i + 1]
            seen[num] = i
            
        # solution 3: using binary search
        
        # solution 4: 2 pointer
        
