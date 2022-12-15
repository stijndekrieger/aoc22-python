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

def calculateScore(treeDepth, treeLength, height):
  scenicScores = []

  #check left side
  cur_length = treeLength - 1
  score = 0
  while True:
    if cur_length < 0:
      if score == 0:
        score = 1
      scenicScores.append(score)
      break
    if treeGrid[treeDepth][cur_length] < height:
      score += 1
    else:
      score += 1
      scenicScores.append(score)
      break
    cur_length -= 1
  
  #check right side
  cur_length = treeLength + 1
  score = 0
  while True:
    if cur_length > length - 1:
      if score == 0:
        score = 1
      scenicScores.append(score)
      break
    if treeGrid[treeDepth][cur_length] < height:
      score += 1
    else:
      score += 1
      scenicScores.append(score)
      break
    cur_length += 1

  #check top side
  cur_depth = treeDepth - 1
  score = 0
  while True:
    if cur_depth < 0:
      if score == 0:
        score = 1
      scenicScores.append(score)
      break
    if treeGrid[cur_depth][treeLength] < height:
      score += 1
    else:
      score += 1
      scenicScores.append(score)
      break
    cur_depth -= 1

  #check bottom side
  cur_depth = treeDepth + 1
  score = 0
  while True:
    if cur_depth > depth - 1:
      if score == 0:
        score = 1
      scenicScores.append(score)
      break
    if treeGrid[cur_depth][treeLength] < height:
      score += 1
    else:
      score += 1
      scenicScores.append(score)
      break
    cur_depth += 1

  finalScore = 1
  for score in scenicScores:
    finalScore = finalScore * score

  return finalScore

highestScore = 0

for cur_depth in range(depth):
  for cur_length in range(length):
    score = calculateScore(cur_depth, cur_length, treeGrid[cur_depth][cur_length])
    if  score > highestScore:
      highestScore = score

print("The highest possible score is", highestScore)