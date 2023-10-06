def is_safe(maze, x, y, sol):
    # Check if (x, y) is a valid position and not blocked
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and sol[x][y] == 0:
        return True
    return False

def solve_maze(maze):
    if not maze:
        return []

    rows = len(maze)
    cols = len(maze[0])
    
    # Initialize a solution matrix with all zeros
    sol = [[0 for _ in range(cols)] for _ in range(rows)]
    
    if solve_util(maze, 0, 0, sol):
        return sol
    else:
        return []

def solve_util(maze, x, y, sol):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        sol[x][y] = 1
        return True

    if is_safe(maze, x, y, sol):
        sol[x][y] = 1

        # Move right
        if solve_util(maze, x, y + 1, sol):
            return True

        # Move down
        if solve_util(maze, x + 1, y, sol):
            return True

        # If no valid move is possible, backtrack
        sol[x][y] = 0
        return False

# Example usage:
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = solve_maze(maze)

if result:
    print("Solution exists. Path:")
    for row in result:
        print(row)
else:
    print("No solution exists.")
def is_safe(maze, x, y, sol):
    # Check if (x, y) is a valid position and not blocked
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and sol[x][y] == 0:
        return True
    return False

def solve_maze(maze):
    if not maze:
        return []

    rows = len(maze)
    cols = len(maze[0])
    
    # Initialize a solution matrix with all zeros
    sol = [[0 for _ in range(cols)] for _ in range(rows)]
    
    if solve_util(maze, 0, 0, sol):
        return sol
    else:
        return []

def solve_util(maze, x, y, sol):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        sol[x][y] = 1
        return True

    if is_safe(maze, x, y, sol):
        sol[x][y] = 1

        # Move right
        if solve_util(maze, x, y + 1, sol):
            return True

        # Move down
        if solve_util(maze, x + 1, y, sol):
            return True

        # If no valid move is possible, backtrack
        sol[x][y] = 0
        return False

# Example usage:
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = solve_maze(maze)

if result:
    print("Solution exists. Path:")
    for row in result:
        print(row)
else:
    print("No solution exists.")
