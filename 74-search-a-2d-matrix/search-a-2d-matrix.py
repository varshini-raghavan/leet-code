class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for i in row:
                if i==target:
                    return True
                if i>target:
                    return False