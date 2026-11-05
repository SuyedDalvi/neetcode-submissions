class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dictionary to store {number: index}
        
        for i, num in enumerate(nums):
            num_to_find = target - num  # What number do we need?
            
            # 1. Check if we've already seen the complement
            if num_to_find in seen:
                return [seen[num_to_find], i]  # Found it! Return previous index and current index
            
            # 2. Otherwise, store current number and its index in the dictionary
            seen[num] = i
            
        return []
