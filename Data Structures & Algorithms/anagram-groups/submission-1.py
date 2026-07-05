class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        case = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for chr in word:
                count[ord(chr) - ord("a") ] += 1
            case[tuple(count)].append(word)
        
        return list(case.values())
        