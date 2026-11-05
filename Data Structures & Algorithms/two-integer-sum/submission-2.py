class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=list()
        index=0
        
        while index < len(nums): # this is O(n)
            num_to_find = target - nums[index]
            if(num_to_find in nums[index+1:]): # this is not O(1), instead its O(n)
                result.append(index)
                result.append(nums.index(num_to_find, index+1))    
            index +=1
        
        return result

