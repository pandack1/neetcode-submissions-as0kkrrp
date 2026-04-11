class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sub_list in matrix:
            for ele in sub_list:
                if ele == target:
                    return True
        return False
        