class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        words = {}
        while len(strs) > 0:
            if len(words) == 0:
                words[strs[0]] = [strs[0]]
                strs.pop(0)
            else:
                self.isAnagram(words, strs[0])
                strs.pop(0)
        
        # words is now fully populated
        for key in words:
            result.append(words[key])
        
        # result is populated
        return result

    def isAnagram(self, strs: Dict, word: str):
        anagram = False
        for key in strs:
            if len(key) == len(word):
                # Create 2 dicts for letters and their frequencies
                dict1 = self.createDict(key)
                dict2 = self.createDict(word)
                if dict1 == dict2:
                    strs[key].append(word)
                    anagram = True
                    break
        if anagram == False:
            strs[word] = [word]

    def createDict(self, word: str) -> dict:
        letters = {}
        for letter in word:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        return letters