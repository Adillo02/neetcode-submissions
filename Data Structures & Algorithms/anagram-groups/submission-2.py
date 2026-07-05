class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: list of strings 
        #output: list with sublist for each anagram
        #plan: Go through the string List
        #countt frequency for each word 
        #
        ans = defaultdict(list)

        for word in strs:
            count = [0] * 26 # a.... z

            for c in word:
                count[ord(c) - ord("a")] += 1 
            ans[tuple(count)].append(word)

        return list(ans.values())


        