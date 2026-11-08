# solution with T(O) = O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table={}
        
        for num in nums: # T(O) = O(n)
            # step 1 counting the frequency of each element
            
            if num in frequency_table: # this is giving O(1) lookup time avg.
                frequency_table[num] += 1
            else:
                frequency_table[num] = 1

        # sorting the keys in the frequency_table map based on the respective values
        sortedKeys = sorted(frequency_table.keys(), key=frequency_table.get, reverse=True) # T(O)=O(mlogm) based on m keys
        return sortedKeys[:k] # filtering the top k values from the left of the list.

# total T(O) = O(n + mlogm) => O(nlogn)




