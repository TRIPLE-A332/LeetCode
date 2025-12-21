class Solution:
    def reverseDegree(self, s: str) -> int:
        summation = 0
        for i,c in enumerate(s, start=1):
            prod = (123 - ord(c)) * i
            summation +=prod

        return summation