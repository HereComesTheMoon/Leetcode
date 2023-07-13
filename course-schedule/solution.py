class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [ [0, []] for _ in range(numCourses) ]
        for [course, prereq] in prerequisites:
            g[course][0] += 1
            g[prereq][1].append(course)
        border = { k for k, [x, _] in enumerate(g) if x == 0 }
        seen = 0
        while border:
            val = border.pop()
            seen += 1
            for x in g[val][1]:
                g[x][0] -= 1
                if g[x][0] == 0:
                    border.add(x)
        return seen == numCourses