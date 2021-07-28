import maze
import random

# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # TODO: Implement create_dfs
    cell_stack = []
    current_cell = random.randint(0, m.total_cells - 1)
    visited_cells = 1

    while visited_cells < m.total_cells:
        neighbors = m.cell_neighbors(current_cell)
        if neighbors:
            new_cell, dir = random.choice(neighbors)
            m.connect_cells(current_cell, new_cell, dir)
            cell_stack.append(current_cell)
            current_cell = new_cell
            visited_cells += 1
        else:
            current_cell = cell_stack.pop()
        m.refresh_maze_view()

    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
