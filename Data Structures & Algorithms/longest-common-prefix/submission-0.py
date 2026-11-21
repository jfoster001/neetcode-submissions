class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        common = strs[0]
        for word in range(1, len(strs)):
            j=0
            while j < min(len(common), len(strs[word])):
                if common[j] != strs[word][j]:
                    break
                j += 1
            common = common[:j]
        return common