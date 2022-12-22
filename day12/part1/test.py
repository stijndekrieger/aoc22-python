def get_neighbors(grid, position):
  # get the row and column of the position
  row, col = position
  
  # create a list to hold the neighbors
  neighbors = []
  
  # if the row is greater than 0, the position has a neighbor above it
  if row > 0:
    # only include the neighbor if it is within one elevation of the current position
    if abs(get_elevation(grid, (row - 1, col)) - get_elevation(grid, position)) <= 1:
      neighbors.append((row - 1, col))
  
  # if the row is less than the number of rows in the grid - 1, the position has a neighbor below it
  if row < len(grid) - 1:
    # only include the neighbor if it is within one elevation of the current position
    if abs(get_elevation(grid, (row + 1, col)) - get_elevation(grid, position)) <= 1:
      neighbors.append((row + 1, col))
  
  # if the column is greater than 0, the position has a neighbor to the left of it
  if col > 0:
    # only include the neighbor if it is within one elevation of the current position
    if abs(get_elevation(grid, (row, col - 1)) - get_elevation(grid, position)) <= 1:
      neighbors.append((row, col - 1))
  
  # if the column is less than the number of columns in the grid - 1, the position has a neighbor to the right of it
  if col < len(grid[0]) - 1:
    # only include the neighbor if it is within one elevation of the current position
    if abs(get_elevation(grid, (row, col + 1)) - get_elevation(grid, position)) <= 1:
      neighbors.append((row, col + 1))
  
  # return the list of neighbors
  return neighbors

def get_elevation(grid, position):
  # get the row and column of the position
  row, col = position
  
  # get the elevation of the position by using the row and column as indices into the grid
  elevation = grid[row][col]
  
  # if the elevation is 'z', return 26
  if elevation == 'z':
    return 26
  
  # otherwise, convert the elevation to an integer by subtracting the ASCII value of 'a' from it
  elevation = ord(elevation) - ord('a')
  
  # return the elevation
  return elevation

def find_shortest_path(grid, start, end):
  # create a list to hold the shortest path
  shortest_path = []
  
  # create a queue to hold unexplored nodes
  queue = []
  
  # add the starting position to the queue
  queue.append(start)
  
  # create a dictionary to hold the distances from the starting position to each other position in the grid
  distances = {start: 0}
  
  # create a dictionary to hold the previous position for each position in the grid
  previous_positions = {start: None}
  
  # create a set to hold the positions that have already been explored
  explored = set()
  
  # create a boolean flag to indicate if the end position has been found
  found = False
  
  # while there are still unexplored nodes in the queue:
  while queue:
    # remove the next node from the queue
    current_position = queue.pop(0)
    
    # if the current position is the end position:
    if current_position == end:
      # set the found flag to true
      found = True
      # break out of the loop
      break
    
    # add the current position to the set of explored positions
    explored.add(current_position)
    
    # for each neighbor of the current position:
    for neighbor in get_neighbors(grid, current_position):
      # if the neighbor has not been explored and is within one elevation of the current position:
      if neighbor not in explored and abs(get_elevation(grid, neighbor) - get_elevation(grid, current_position)) <= 1:
        # add the neighbor to the queue
        queue.append(neighbor)
        # update the distance from the starting position to the neighbor
        distances[neighbor] = distances[current_position] + 1
        # update the previous position for the neighbor
        previous_positions[neighbor] = current_position
  
  # if the end position was found:
  if found:
    # set the current position to the end position
    current_position = end
    # while the current position is not the starting position:
    while current_position != start:
      # add the current position to the beginning of the shortest path
      shortest_path.insert(0, current_position)
      # set the current position to the previous position
      current_position = previous_positions[current_position]
    # add the starting position to the beginning of the shortest path
    shortest_path.insert(0, start)
  
  # return the shortest path and the distance from the starting position to the end position
  return shortest_path, distances.get(end, float('inf'))

grid = [
  "Sabqponm",
  "abcryxxl",
  "accszExk",
  "acctuvwj",
  "abdefghi"
]

start = (0, 0)  # starting position is the top-left corner
end = (2, 6)  # ending position is the square with the letter 'E'

print(find_shortest_path(grid, start, end))