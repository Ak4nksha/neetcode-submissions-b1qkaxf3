class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(n)}
        heights = {}       
        ans = []

        def bfs_height(i):
            st = []
            visit = [0]*n
            visit[i] = 1
            st.append((i,0))
            h = 0

            while st:
                node, level = st.pop()
                h = max(h,level)
                for child in adj[node]:
                    if not visit[child]:
                        st.append((child,level+1))
                        visit[child] = 1
                        
            return h


        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for i in range(n):
            h = bfs_height(i)
            heights[i] = h

        #heights.sorted(key=lambda x: x[1])
        min_height = min(heights.values())
        for k,v in heights.items():
            if v == min_height:
                ans.append(k)

        return ans


