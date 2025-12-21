class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        visited = {}

        for num in nums:
            if num in visited:
                visited[num] += 1 
            else:
                visited[num] = 1
    
        highest = max(visited.values())

        summation = sum(v for v in visited.values() if v==highest)

        return summation