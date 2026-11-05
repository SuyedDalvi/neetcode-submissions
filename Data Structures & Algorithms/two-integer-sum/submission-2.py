# this solution uses .index() approach to find the position of the number. index() returns first index when it finds multiple values, to ensure this does not impact the solution provide explicit start index to the method.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=list()
        index=0
        
        while index < len(nums): # this is O(n)
            num_to_find = target - nums[index]
            if(num_to_find in nums[index+1:]): # this is not O(1), instead its O(n)
                result.append(index)
                result.append(nums.index(num_to_find, index+1))    # explicitly stating the start index to be from the next index instead of the whole nums list.
            index +=1
        
        return result

