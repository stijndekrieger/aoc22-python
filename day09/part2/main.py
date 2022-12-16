with open("day09/data/motions.txt") as file:
  motions = file.readlines()

knots = [{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0},{"X":0,"Y":0}]
tail9VisitedCoordinates = []
headVisitedCoordinates = []

def processCommand(command: str):
  direction = command.split(" ")[0]
  amount = int(command.split(" ")[1])

  for i in range(amount):
    headVisitedCoordinates.append([knots[0]["X"], knots[0]["Y"]])

    if direction == "R":
      knots[0]["X"] += 1
    if direction == "L":
      knots[0]["X"] -= 1
    if direction == "U":
      knots[0]["Y"] += 1
    if direction == "D":
      knots[0]["Y"] -= 1

    makeTailsFollow()

def makeTailsFollow():
  for index in range(1,len(knots)):
    makeTailFollow(index)

def makeTailFollow(index):
  tailX = knots[index]["X"]
  tailY = knots[index]["Y"]

  parentX = knots[index - 1]["X"]
  parentY = knots[index - 1]["Y"]

  differenceX = abs(parentX - tailX)
  differenceY = abs(parentY - tailY)

  if differenceX > 1 or differenceY > 1:
    if differenceX == 2 and differenceY == 2:
      return setTailPosition(index, tailX, tailY)
    #Head and tails are on same X line
    if tailY == parentY:
      if tailX < parentX:
        tailX += 1
        return setTailPosition(index, tailX, tailY)
      elif tailX > parentX:
        tailX -= 1
        return setTailPosition(index, tailX, tailY)
    #Head and tails are on same Y line
    if tailX == parentX:
      if tailY < parentY:
        tailY += 1
        return setTailPosition(index, tailX, tailY)
      elif tailY > parentY:
        tailY -= 1
        return setTailPosition(index, tailX, tailY)
    #Head and tails are not equal, move diagonally
    if differenceX > differenceY:
      tailY = parentY
      if tailX < parentX:
        tailX += 1
        return setTailPosition(index, tailX, tailY)
      elif tailX > parentX:
        tailX -= 1
        return setTailPosition(index, tailX, tailY)
    elif differenceY > differenceX:
      tailX = parentX
      if tailY < parentY:
        tailY += 1
        return setTailPosition(index, tailX, tailY)
      elif tailY > parentY:
        tailY -= 1
        return setTailPosition(index, tailX, tailY)

def setTailPosition(index, x, y):

  knots[index]["X"] = x
  knots[index]["Y"] = y

  if index == 9:
    tail9VisitedCoordinates.append([x, y])
  return None

def removeDuplicates(arr):
  result = []

  for i in arr:
    if i not in result:
      result.append(i)
  return result

for motion in motions:
  processCommand(motion)

tail9VisitedCoordinates.insert(0,[0,0])
tail9VisitedCoordinates = removeDuplicates(tail9VisitedCoordinates)

print("The ninth tail of the rope has visited", len(tail9VisitedCoordinates), "positions at least once")