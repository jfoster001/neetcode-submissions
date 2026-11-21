class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams into sublists. return grouped list.
        newList = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            newList[sortedS].append(s)
        return list(newList.values())
