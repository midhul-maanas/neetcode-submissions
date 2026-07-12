class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newList = {}
        for i in strs:
            key = "".join(sorted(i))
            print(key)
            if key not in newList:
                newList[key] = []
            newList[key].append(i)
            
        return list(newList.values())