class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        list_ans = [[] for n in range(len(nums) + 1)]
        
        for num in nums:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1
        
        for key, value in ans.items():
            list_ans[value].append(key)
        final = []
        for i in range(len(list_ans) -1, 0, -1):
            for n in list_ans[i]:
                final.append(n)
                if len(final) == k:
                    return final
        
        return final
