class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.groupAnagrams_(strs)

    def groupAnagrams_(self, strs: List[str]):
        list_of_anagrams=list()

        temp={}

        # step 1: mapped all the anagrams
        for i, s in enumerate(strs):
            sortedChars = self.sortCharacters(s)
            # adding the first index
            if(temp.get(sortedChars) is None):
                temp[sortedChars]=[i]
            else:
                # appending index number
                temp[sortedChars].append(i)

        # step 2
        for i,j in enumerate(temp):
            anagrams_list=list()
            for index in temp[j]:
                anagrams_list.append(strs[index])
            list_of_anagrams.append(anagrams_list)

        return list_of_anagrams
        
    def sortCharacters(self, s: str):
        return "".join(sorted(s))


act = 0
opst = 1
opst = 2
act = 3
opst = 4
aht = 5


act: [0,3]
opst: [1,2,4]
aht: [5]
