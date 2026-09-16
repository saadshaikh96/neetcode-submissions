class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = {}
        for course in range(numCourses):
            dependencies[course] = []
        
        for course, dependency in prerequisites:
            dependencies[course].append(dependency)

        visited, visiting = set(), set()
        for course in range(numCourses):
            if course not in visited:
                hasCycle = self.dfs(course, dependencies, visited, visiting)
                if hasCycle:
                    return False
        
        return True

    def dfs(self, course, dependencies, visited, visiting):
        if course in visited:
            return False
        if course in visiting:
            return True
        
        visiting.add(course)
        for dependency in dependencies[course]:
            hasCycle = self.dfs(dependency, dependencies, visited, visiting)
            if hasCycle:
                return True
        
        visited.add(course)
        visiting.remove(course)
        return False
