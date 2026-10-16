class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            count = [0]*26
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] +=1
            key = tuple(count)
            if key in hashmap:
                hashmap[key].append(word)
            else: 
                hashmap[key] = [word]
        res = []
        for key, value in hashmap.items():
            res.append(value)
        return res