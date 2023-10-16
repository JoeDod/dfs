#dfs递归版本
from maze import Maze


class Solution:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.__visited = set()

    def __check(self, i, j):
        return i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0]) and self.grid[i][j] == 0

    def __isTarget(self, i, j):
        return i == len(self.grid) - 2 and j == len(self.grid[0]) - 2

    def __dfs(self, i, j, path):
        if not self.__check(i, j):
            return False
        if (i, j) in self.__visited:
            return False
        self.__visited.add((i, j))
        if self.__isTarget(i, j):
            path.append((i, j))
            return True
        path.append((i, j))
        if self.__dfs(i + 1, j, path) or self.__dfs(i, j + 1, path) or self.__dfs(i - 1, j, path) or self.__dfs(i, j - 1, path):
            return True
        path.pop()
        return False

    def getPath(self):
        path = []
        self.__dfs(1, 1, path)
        return path

    def v(self):
        print(self.__visited)


if __name__ == "__main__":
    g = Maze(10, 10).builtMaze()
    m, n = len(g), len(g[0])
    for r in range(m):
        for c in range(n):
            print(g[r][c], end=' ')
        print()
    s = Solution(g)
    for x, y in s.getPath():
        g[x][y] = "X"
    print("-----------------路线---------------------")
    for r in range(m):
        for c in range(n):
            print(g[r][c], end=' ')
        print()
