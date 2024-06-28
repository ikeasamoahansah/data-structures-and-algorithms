import collections

def main(grid): 
    if not grid: return 0
    visit = set()
    rows, cols = len(grid), len(grid[0])
    nums = 0

    def bfs(grid, r, c):

        q = collections.deque()
        visit.add((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if(r in range(row) and c in range(col) and grid[r][c] == "1" and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(grid, r, c)
                nums += 1
    return nums
