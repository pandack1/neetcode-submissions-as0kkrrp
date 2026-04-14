class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.path = set()
        self.visited = set()
        self.adjList = {i: [] for i in range(numCourses)}

        for dst, src in prerequisites:
            self.adjList[src].append(dst)
        
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, node):
        if node in self.path:
            return False
        
        if node in self.visited:
            return True
        
        self.path.add(node)
        for nei in self.adjList[node]:
            if not self.dfs(nei):
                return False
        self.path.remove(node)
        self.visited.add(node)
        return True