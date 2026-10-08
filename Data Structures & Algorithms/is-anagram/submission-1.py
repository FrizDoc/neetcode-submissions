class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        dict_s = {}
    
        for ch in s:
            if ch in dict_s:
                dict_s[ch] += 1
            else: dict_s[ch] = 1
        dict_t = {}

        for ch in t:
            if ch in dict_t:
                dict_t[ch] += 1
            else: dict_t[ch] = 1
        for key in dict_t:
            if dict_t.get(key, None) != dict_s.get(key, None):
                return False
        return True