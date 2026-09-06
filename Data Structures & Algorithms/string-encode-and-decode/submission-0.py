class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            size = len(word)
            result += str(size) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while (i < len(s)):
            j = i
            while (s[j] != '#'):
                j += 1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            result.append(s[i:j])
            i=j

        return result