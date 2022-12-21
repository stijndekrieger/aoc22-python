heightmap = []

def letter_to_number(letter: str):
  return ord(letter.lower()) - 97

currentCoordinates = []
endCoordinates = []

with open("day12/data/heightmap.txt") as file:
  map = file.readlines()

  currentVerticalLine = 0
  currentHorizontalPosition = 0

  for horizontalLine in map:
    heightmap.append([])
    horizontalLine = horizontalLine.strip()
    currentHorizontalPosition = 0
    for letter in horizontalLine:
      letter = letter.strip()
      if letter == "S":
        letter = "a"
        currentCoordinates.append(currentVerticalLine)
        currentCoordinates.append(currentHorizontalPosition)
      elif letter == "E":
        letter = "z"
        endCoordinates.append(currentVerticalLine)
        endCoordinates.append(currentHorizontalPosition)
      heightmap[currentVerticalLine].append(letter_to_number(letter))
      currentHorizontalPosition += 1
    currentVerticalLine += 1

# with open("day12/data/heightmap-test.txt", "w") as file:
#   for horizontalLine in heightmap:
#     for number in horizontalLine:
#       file.write(str(number) + " ")
#     file.write("\n")

def getPossibleMoves():
  possibleMoves = []
  currentHeight = heightmap[currentCoordinates[0]][currentCoordinates[1]]
  maxHorizontal = len(heightmap[0]) - 1
  maxVertical = len(heightmap) - 1

  #vertical options
  #check below
  if currentCoordinates[0] < maxVertical:
    if heightmap[currentCoordinates[0]+1][currentCoordinates[1]] <= currentHeight:
      possibleMoves.append([currentCoordinates[0]+1,currentCoordinates[1]])
  #check above
  if currentCoordinates[0] > 0:
    if heightmap[currentCoordinates[0]-1][currentCoordinates[1]] <= currentHeight:
      possibleMoves.append([currentCoordinates[0]-1,currentCoordinates[1]])
  #horizontal options
  #check left
  if currentCoordinates[1] > 0:
    if heightmap[currentCoordinates[0]][currentCoordinates[1]-1] <= currentHeight:
      possibleMoves.append([currentCoordinates[0],currentCoordinates[1]-1])
  #check right
  if currentCoordinates[1] < maxHorizontal:
    if heightmap[currentCoordinates[0]][currentCoordinates[1]+1] <= currentHeight:
      possibleMoves.append([currentCoordinates[0],currentCoordinates[1]+1])

  return possibleMoves

def getBestMove(possibleMoves):
  if endCoordinates in possibleMoves:
    return endCoordinates

  allDeltas = []
  for move in possibleMoves:
    deltaArray = []
    currentCoordinateIndex = 0
    for coordinate in move:
      delta = abs(coordinate - endCoordinates[currentCoordinateIndex])
      deltaArray.append(delta)
      currentCoordinateIndex += 1

    allDeltas.append(deltaArray)

  print(" All delta array",allDeltas)
  bestDelta = min(allDeltas, key=lambda x: x[0] + x[1])
  indexOfBest = allDeltas.index(bestDelta)
  return possibleMoves[indexOfBest]

stepsTaken = 0
# while currentCoordinates != endCoordinates:
#   possibleMoves = getPossibleMoves()
#   bestMove = getBestMove(possibleMoves)
#   print("Possible Moves",possibleMoves)
#   print("Best Move",bestMove)
#   currentCoordinates = bestMove
#   stepsTaken += 1
  # print(possibleMoves)
  # print(currentCoordinates)

print("Current position",currentCoordinates)
for i in range(10):
  possibleMoves = getPossibleMoves()
  bestMove = getBestMove(possibleMoves)
  print(" Possible Moves",possibleMoves)
  print(" Best Move",bestMove)
  currentCoordinates = bestMove
  stepsTaken += 1
  print("Current position",currentCoordinates)
  # print(possibleMoves)
  # print(currentCoordinates)