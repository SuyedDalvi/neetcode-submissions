#clue no 1: return value is array of objects -> hashmap 
# improving the solution to have TC O(m*n) instead of O(m*nlogn)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # set result with defaultdict to avoid errors when accessing non existing values
        result = defaultdict(list)
        # Step1: setup each string in the input to its numeric/ascii representation
        for word in strs:
            
            # initializing frequency measuring variable - frequency refers to the total count of each character in the word

            count = [0] * 26

            for c in word:
                count[ord(c)-ord('a')] += 1

            result[tuple(count)].append(word)


        return list(result.values())
