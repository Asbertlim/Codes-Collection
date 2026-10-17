
def rescue_robot(grid, commands):
    final_row = 0
    final_col = 0
    failed_moves = 0
    total_score = 0
    collected = set()

    for i in range(len(grid)):
        if "S" in grid[i]:
            start = grid[i].index("S")
            starting_point = [i, start]

    for j in commands:
        new_row = starting_point[0]
        new_col = starting_point[1]

        if j == "U":
            new_row -= 1
        elif j == "D":
            new_row += 1
        elif j == "R":
            new_col += 1
        elif j == "L":
            new_col -= 1


        if (new_row < 0 or new_row >= len(grid)
                or new_col < 0 or new_col >= len(grid[0])):
            failed_moves += 1
            continue

        
        if grid[new_row][new_col] == "#":
            failed_moves += 1
            continue

    
        if grid[new_row][new_col] == "R":
            if (new_row, new_col) not in collected:
                total_score += 10
                collected.add((new_row, new_col))

        starting_point = [new_row, new_col]

        final_row = starting_point[0]
        final_col = starting_point[1]

    return (final_row, final_col, failed_moves, total_score)

grid = [
    "S.R.",
    ".#R.",
    "...."
]

commands = "RRDDLLUU"

print(rescue_robot(grid, commands))
