from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            afterSorting = ''.join(sorted(s)) 
            if afterSorting in answer.keys():
                answer[afterSorting].append(s)
            else:
                answer[afterSorting] = [s]

        result =[]
        for values in answer.values():
            partialResult = []
            for value in values:
                partialResult.append(value)
            
            result.append(partialResult)

        return result
        

if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print (result)