class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #group all anagrams into sublists. return grouped list.
        newList = defaultdict(list)
        for s in strs:
            count = [0] * 26 #initialize a-z to be 0
            for c in s:
                count[ord(c) - ord('a')] += 1
            newList[tuple(count)].append(s)
        return list(newList.values())