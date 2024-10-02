def is_adjacent_to_symbol(grid, i, j, symbols):
    # Define the 8 possible directions to check for adjacency
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if grid[ni][nj] in symbols:
                return True
    return False

def sum_part_numbers(grid):
    total_sum = 0
    symbols = {'*', '#', '+', '$'}
    
    # Loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].isdigit():
                # Check if the current number is adjacent to a symbol
                if is_adjacent_to_symbol(grid, i, j, symbols):
                    total_sum += int(grid[i][j])
    
    return total_sum

# Example engine schematic
grid = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# Convert the schematic to a list of lists (2D array)
grid = [list(row) for row in grid]

# Calculate the sum of the part numbers
result = sum_part_numbers(grid)
print("Sum of all part numbers:", result)
