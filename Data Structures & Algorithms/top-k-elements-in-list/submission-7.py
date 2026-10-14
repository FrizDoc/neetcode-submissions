class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = 1
            else: 
                hashmap[num] += 1
        nums_count = [[] for _ in range(len(nums) + 1)]
        for key, value in hashmap.items():
            nums_count[value].append(key)
        res = []
        for i in reversed(range(len(nums_count))):
            for num in nums_count[i]:
                res.append(num)
                if len(res) == k:
                    return res