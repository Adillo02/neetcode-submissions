class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        freq = [[] for i in range(len(nums) + 1 ) ]
        for i in nums:
            if i in ans:
                ans[i] += 1 
            else:
                ans[i] = 1
        for i, value in ans.items():
            freq[value].append(i)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
