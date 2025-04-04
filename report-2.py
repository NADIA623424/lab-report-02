def depth_limited_search(grid, current, target, depth, max_depth, visited, path):
    row, col = current
    path.append(current)
    visited.add(current)

    if current == target:
        return True, path

    if depth == max_depth:
        path.pop()
        return False, None

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        next_pos = (new_row, new_col)

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0 and next_pos not in visited:
            found, found_path = depth_limited_search(grid, next_pos, target, depth + 1, max_depth, visited, path)
            if found:
                return True, found_path

    path.pop()
    return False, None

def iterative_deepening_dfs(grid, start, end, max_depth):
    for limit in range(max_depth + 1):
        visited_nodes = set()
        path_taken = []
        found, result_path = depth_limited_search(grid, start, end, 0, limit, visited_nodes, path_taken)

        if found:
            return True, len(result_path) - 1, result_path
    return False, max_depth, None

if __name__ == "__main__":
    try:
        rows, cols = map(int, input("Enter number of rows and columns: ").split())
        grid = []

        print("Enter the grid structure (0 for open, 1 for wall):")
        for _ in range(rows):
            grid.append(list(map(int, input().strip().split())))

        start_x, start_y = map(int, input("Enter start position (row col): ").split())
        end_x, end_y = map(int, input("Enter target position (row col): ").split())

        start = (start_x, start_y)
        end = (end_x, end_y)

        max_depth = rows * cols

        found, depth_found, path = iterative_deepening_dfs(grid, start, end, max_depth)

        if found:
            print(f"Path found at depth {depth_found} using IDDFS")
            print("Path:", path)
        else:
            print(f"No path found within depth limit {max_depth} using IDDFS")

    except ValueError:
        print("Invalid input format.")
