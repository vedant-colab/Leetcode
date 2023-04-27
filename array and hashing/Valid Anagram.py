class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht,yt = {},{}
        for char in s:
            if char in ht:
                ht[char] +=1

            else:
                ht[char] = 1

        for char in t:
            if char in yt:
                yt[char] +=1

            else:
                yt[char] = 1

        return ht == yt
