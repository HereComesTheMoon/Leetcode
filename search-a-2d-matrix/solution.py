class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = bisect.bisect_left(matrix, target, key=lambda row: row[-1])
        if i == len(matrix):
            return False
        j = bisect.bisect_left(matrix[i], target)
        return matrix[i][j] == target