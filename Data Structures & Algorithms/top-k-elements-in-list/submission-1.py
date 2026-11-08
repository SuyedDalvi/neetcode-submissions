# solution with T(O) = O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return self.bySortingFrequencyArray(nums, k)
        return self.byBucketSort(nums, k)


    def byBucketSort(self, nums:List[int], k:int):
        frequency_table={}
        topk=[]

        for num in nums: # T(O) = O(n)
            # step 1 counting the frequency of each element
            
            if num in frequency_table: # this is giving O(1) lookup time avg.
                frequency_table[num] += 1
            else:
                frequency_table[num] = 1

        # define bucket using defaultdict(list) and add the keys at the freq index in the bucket.
        # bucket is expected to store multiple values at one index, hence list
        buckets=defaultdict(list) 

        for key, value in frequency_table.items():
            buckets[value].append(key)
        
        # considering possiblity of 1 number in the nums list implying max frequency
        for index in range(len(nums),0, -1):
            for el in buckets.get(index, []):
                topk.append(el)
                if(len(topk) == k):
                    return topk
            
        
        


    def bySortingFrequencyArray(self, nums: List[int], k:int):
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

        # total T(O) = O(n + mlogm) 




