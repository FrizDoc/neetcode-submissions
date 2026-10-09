class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            count = [0]*26
            for ch in str:
                count[ord(ch) - ord('a')] +=1
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(str)
        return list(hashmap.values())