#!/usr/bin/env python
# coding: utf-8

# In[2]:


def move_tile(grid, empty_pos, new_pos):
    new_grid = [row[:] for row in grid] 
    x1, y1 = empty_pos
    x2, y2 = new_pos
    new_grid[x1][y1], new_grid[x2][y2] = new_grid[x2][y2], new_grid[x1][y1]
    return new_grid

def print_grid(grid): 
    for row in grid:
        for row in grid:
            print(" ".join(map(str, row)))
        print()

def print_solution(path):
    print("\nSolution Found in", len(path) - 1, "moves:\n")
    for state in path:
        print_grid(state)

def solve_puzzle_bfs(start, empty_pos, goal):
    queue = [(start, empty_pos, [])]  
    visited = set()
    moves = [(1, 0), (0, -1), (-1, 0), (0, 1)] 

    while queue:
        grid, empty_pos, path = queue.pop(0)

        if grid == goal:
            print_solution(path + [grid])
            return
        visited.add(tuple(map(tuple, grid)))
       
        for dx, dy in moves:
            new_x, new_y = empty_pos[0] + dx, empty_pos[1] + dy
           
            if 0 <= new_x< 3 and 0 <= new_y< 3:
                new_grid = move_tile(grid, empty_pos, (new_x, new_y))
               
                if tuple(map(tuple, new_grid)) not in visited:
                    queue.append((new_grid, (new_x, new_y), path + [grid]))
                    
def get_inversion_count(grid):
    flat_list= [num for row in grid for num in row if num != 0]  
    inv_count=0
    for i in range(len(flat_list)):
        for j in range(i+1,len(flat_list)):
            if flat_list[i]>flat_list[j]:
                inv_count += 1
    return inv_count

def check_reachability(start, goal, empty_start):
      
    start_inversions = get_inversion_count(start)
    goal_inversions = get_inversion_count(goal)

    print("Start state inversion count:", start_inversions)
    print("Goal state inversion count:", goal_inversions)

    if (start_inversions % 2) == (goal_inversions % 2):
        print("\nThe given states are in the same set and reachable.\n")
        solve_puzzle_bfs(start, empty_start, goal)
    else:
        print("\nThe given states belong to different disjoint sets and are NOT reachable from each other.\n")
                
            
start_grid=[[8,6,7],
            [3,4,0],
            [1,5,2]]

goal_grid=[[1,2,3],
           [4,5,6],
           [7,8,0]]

empty_start=(1,2)

check_reachability(start_grid, goal_grid, empty_start)


# In[ ]:




