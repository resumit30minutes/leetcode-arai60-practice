from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        NUM_ROW = len(grid)
        NUM_COLUMN = len(grid[0])
        visited = [[False] * NUM_COLUMN for _ in range(NUM_ROW)]

        def is_explorable(row: int, column: int) -> bool:
            WATER = 0
            if not (0 <= row < NUM_ROW and 0 <= column < NUM_COLUMN):
                return False
            if grid[row][column] == WATER:
                return False
            if visited[row][column]:
                return False
            return True
        
        def count_area(row: int, column: int) -> int:
            area = 0
            next_positions = [(row, column)]
            while next_positions:
                row, column = next_positions.pop()
                if not is_explorable(row, column):
                    continue
                visited[row][column] = True
                area += 1
                next_positions.append((row + 1, column))
                next_positions.append((row - 1, column))
                next_positions.append((row, column + 1))
                next_positions.append((row, column - 1))
            return area

        max_area = 0
        for row in range(NUM_ROW):
            for column in range(NUM_COLUMN):
                if is_explorable(row, column):
                    area = count_area(row, column)
                    max_area = max(max_area, area)
        return max_area
