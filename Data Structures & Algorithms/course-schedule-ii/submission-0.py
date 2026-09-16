class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = {}
        for course in range(numCourses):
            dependencies[course] = []
        
        for course, dependency in prerequisites:
            dependencies[course].append(dependency)

        visited, visiting, result = set(), set(), []
        for course in range(numCourses):
            if course not in visited:
                hasCycle = self.dfs(course, dependencies, visited, visiting, result)
                if hasCycle:
                    return []
        
        return result

    def dfs(self, course, dependencies, visited, visiting, result):
        if course in visited:
            return False
        if course in visiting:
            return True
        
        visiting.add(course)
        for dependency in dependencies[course]:
            hasCycle = self.dfs(dependency, dependencies, visited, visiting, result)
            if hasCycle:
                return True
        
        visiting.remove(course)
        visited.add(course)
        result.append(course)
        return False