from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dependCnt = [0] * numCourses
        taken = []
        adj = defaultdict(list)

        # for i in range(numCourses):
        #     adj[i] = []

        for i in range(len(prerequisites)):
            second,first = prerequisites[i]
            dependCnt[second] += 1
            adj[first].append(second)

        q = deque()

        for i in range(numCourses):
           if dependCnt[i] == 0:
                q.append(i)
        # print(adj)
        # print(dependCnt)
        while q:
            #print(q)
            course = q.popleft()
            taken.append(course)
            for c in adj[course]:
                dependCnt[c] -= 1
                if dependCnt[c] == 0:
                    q.append(c)
        
        #print(q)
        if len(taken) == numCourses:
            return True
        else:
            return False
            

            

