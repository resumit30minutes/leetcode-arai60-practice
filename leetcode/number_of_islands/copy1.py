from typing import List
from collections import deque

class Solution:
    # memory limit over
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        WATER = '0'
        m, n = len(grid), len(grid[0])

        def remove_connected_lands(start_row, start_col):
            if grid[start_row][start_col] == WATER:
                return
                
            lands = deque([(start_row, start_col)])
            while lands:
                row, col = lands.popleft()
                grid[row][col] = WATER

                dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for dr, dc in dirs:
                    next_row, next_col = row + dr, col + dc
                    if not (0 <= next_row < m and 0 <= next_col < n):
                        continue
                    if grid[next_row][next_col] == WATER:
                        continue
                    lands.append((next_row, next_col))
        
        num_of_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == LAND:
                    num_of_islands += 1
                    remove_connected_lands(i, j)
        return num_of_islands
                    
    def numIslands2(self, grid: List[List[str]]) -> int:
        def mark_land_as_visited(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                mark_land_as_visited(row + dr, col + dc)

        m, n = len(grid), len(grid[0])
        num_of_islands = 0
        for i in range(m):
            for j in range(n):
                # find a new islands
                if grid[i][j] == '1':
                    num_of_islands += 1
                    mark_land_as_visited(i, j)
        return num_of_islands
