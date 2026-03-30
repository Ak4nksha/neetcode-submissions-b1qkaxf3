class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        n = len(strs)
        d = {}

        for s in strs:

            t =  "".join(sorted(s))
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)


        return list(d.values())