# 用于生成m*n 大小迷宫
import random


class Maze:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def builtMaze(self):
        status = [[[False for _ in range(4)] for _ in range(
            self.col)]for _ in range(self.row)]
        visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        i, j = 0, 0
        stack = [(i, j)]
        while stack:
            visited[i][j] = True
            choosable = []
            if j > 0 and not visited[i][j-1]:
                choosable.append('L')
            if i > 0 and not visited[i-1][j]:
                choosable.append('U')
            if j < self.col-1 and not visited[i][j+1]:
                choosable.append('R')
            if i < self.row-1 and not visited[i+1][j]:
                choosable.append('D')
            if choosable:
                direct = random.choice(choosable)
                if direct == 'L':
                    status[i][j][0] = True
                    j -= 1
                    status[i][j][2] = True
                elif direct == 'U':
                    status[i][j][1] = True
                    i -= 1
                    status[i][j][3] = True
                elif direct == 'R':
                    status[i][j][2] = True
                    j += 1
                    status[i][j][0] = True
                elif direct == 'D':
                    status[i][j][3] = True
                    i += 1
                    status[i][j][1] = True
                stack.append((i, j))
            else:
                i, j = stack.pop()

        maze = [[1 for _ in range(self.col*2+1)] for _ in range(self.row*2+1)]
        for r in range(self.row):
            for c in range(self.col):
                cell = status[r][c]
                maze[r*2+1][c*2+1] = 0
                if cell[0]:
                    maze[r*2+1][c*2] = 0
                if cell[1]:
                    maze[r*2][c*2+1] = 0
                if cell[2]:
                    maze[r*2+1][c*2+2] = 0
                if cell[3]:
                    maze[r*2+2][c*2+1] = 0

        return maze


if __name__ == '__main__':
    s = Maze(8, 8)
    g = s.builtMaze()
    m, n = len(g), len(g[0])
    for i in range(m):
        for j in range(n):
            print(g[i][j], end='')
        print()
