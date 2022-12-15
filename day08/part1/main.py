with open("day08/data/tree-grid.txt") as file:
  grid = file.readlines()

treeGrid = []

depth = len(grid)
length = len(grid[0].strip())

for cur_depth in range(depth):
  treeGrid.append([])
  for cur_length in range(length):
    treeGrid[cur_depth].append(0)

for cur_depth in range(depth):
  for cur_length in range(length):
    treeGrid[cur_depth][cur_length] = grid[cur_depth][cur_length]

treesVisible = 0

def isTreeVisible(treeDepth, treeLength, height):
  #Tree is on edge
  if treeDepth == 0 or treeDepth == depth - 1:
    return True
  if treeLength == 0 or treeLength == length -1:
    return True

  visibleFromLeft = True
  visibleFromRight = True
  visibleFromTop = True
  visibleFromBottom = True

  leftTreeHeights = []
  rightTreeHeights = []
  topTreeHeights = []
  bottomTreeHeights = []

  for cur_length in range(length):
    if cur_length == treeLength:
      continue
    if cur_length < treeLength:
      leftTreeHeights.append(treeGrid[treeDepth][cur_length])
    if cur_length > treeLength:
      rightTreeHeights.append(treeGrid[treeDepth][cur_length])

  for cur_depth in range(depth):
    if cur_depth == treeDepth:
      continue
    if cur_depth < treeDepth:
      bottomTreeHeights.append(treeGrid[cur_depth][treeLength])
    if cur_depth > treeDepth:
      topTreeHeights.append(treeGrid[cur_depth][treeLength])

  if height <= max(leftTreeHeights):
    visibleFromLeft = False
  if height <= max(rightTreeHeights):
    visibleFromRight = False
  if height <= max(bottomTreeHeights):
    visibleFromBottom = False
  if height <= max(topTreeHeights):
    visibleFromTop = False

  return visibleFromLeft | visibleFromBottom | visibleFromRight | visibleFromTop

for cur_depth in range(depth):
  for cur_length in range(length):
    if isTreeVisible(cur_depth, cur_length, treeGrid[cur_depth][cur_length]):
      treesVisible += 1

print("There are",treesVisible, "trees visible")