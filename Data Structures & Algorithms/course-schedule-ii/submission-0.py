class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {}
        dependCnt = [0] * numCourses
        q = deque()
        taken = []

        for i in range(numCourses):
            adj[i] = []

        for second, first in prerequisites:

            adj[first].append(second)
            dependCnt[second] += 1

        for i in range(numCourses):

            if dependCnt[i] == 0:
                q.append(i)

        while q:

            course = q.popleft()
            taken.append(course)

            for c in adj[course]:
                dependCnt[c] -= 1
                if dependCnt[c] == 0:
                    q.append(c)

        if len(taken) == numCourses:
            return taken
        else:
            return []

