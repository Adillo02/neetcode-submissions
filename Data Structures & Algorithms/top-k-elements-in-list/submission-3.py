class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        list_ans = []
        
        for num in nums:
            if num in ans:
                ans[num] += 1
            else:
                ans[num] = 1
        
        for i in range(k):
            max_key = max(ans, key=ans.get)
            list_ans.append(max_key)
            ans.pop(max_key)

        return list_ans

