class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c: list() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        q = deque()
        n = len(words)
        ans = ""

        for i in range(n-1):

            str1 = words[i]
            str2 = words[i+1]

            m = min(len(str1),len(str2))
            if len(str1) > len(str2) and str1[:m] == str2[:m]: return ""
            
            for j in range(m):
                first = str1[j]
                sec = str2[j]

                if first == sec: continue
                adj[first].append(sec)
                indegree[sec] += 1
                break
            

        for k,v in indegree.items():
            if v == 0:
                q.append(k)

        #print(indegree)
        while q:

            node = q.popleft()
            ans += node

            
            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
            

        return ans if len(ans) == len(indegree) else ""




