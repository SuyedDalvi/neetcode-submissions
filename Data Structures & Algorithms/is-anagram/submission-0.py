class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.sortCharacters(s) == self.sortCharacters(t)

    def sortCharacters(self, s: str ) -> List:
        return sorted(s)