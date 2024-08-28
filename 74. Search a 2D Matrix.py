"""
https://leetcode.com/problems/search-a-2d-matrix/description/
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Usual binary search with the translation into a matrix
        """
        def translate(i, m):
            return (int(i / m), i % m)

        found = False
        m = len(matrix[0])
        n = len(matrix)
        max_i = m * n - 1
        min_i = 0

        while max_i >= min_i:
            print(max_i, min_i)
            if (max_i == min_i):
                translated = translate(max_i, m)
                return (matrix[translated[0]][translated[1]] == target)
            search_n = int((max_i + min_i) / 2)
            translated = translate(search_n, m)
            value = matrix[translated[0]][translated[1]]
            print(search_n, translated, value)
            if (value == target):
                return True
            elif (value > target):
                max_i = search_n - 1
            else:
                min_i = search_n + 1
        return False
