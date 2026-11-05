class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # return self.hasDuplicate_withTempList(nums)
       # return self.hasDuplicate_withPointers(nums)
       # return self.hasDuplicate_withSet(nums)
       # return self.hasDuplicate_bruteForce(nums)

       # final solution using set and loop
        return self.hasDuplicate_best(nums)

    


    # Time Complexity : O(n^2); Space Complexity : O(n)
    def hasDuplicate_withTempList(self, nums: List[int]) -> bool:
        seen = list()
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
             
        return False
    
    # Time Complexity = O(n) ; Space Complexity = O(n)
    def hasDuplicate_withSet(self, nums: List[int]) -> bool:
        seen = set(nums) # requires O(n) TC and SC
        return len(nums) != len(seen)

    # Time Complexity: O(nlogn) ; Space Complexity O(1)
    def hasDuplicate_withPointers(self, nums: List[int]) -> bool:
        nums.sort() # O(nlogn) default Python behavior
        left_ptr=0
        right_ptr=1

        while right_ptr < len(nums):
            if(nums[left_ptr] == nums[right_ptr]):
                return True
            
            left_ptr +=1
            right_ptr +=1

        return False

    # Time complexity = O(n^2), Space complexity = O(n) 
    def hasDuplicate_bruteForce(self, nums: List[int]) -> bool:
        index=0
        while index < len(nums):
            if nums[index] in nums[index+1:]:
                return True
            index +=1
        return False

    def hasDuplicate_best(self, nums: List[int]) -> bool:
        seen = set() # SC = O(n)
        for num in nums: # TC = O(n)
            if num in seen: # Best case TC=O(1) if duplicate is found in the first and second element of the input
                return True 
            seen.add(num)
        return False
