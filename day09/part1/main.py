with open("day09/data/motions.txt") as file:
  motions = file.readlines()

headX = 0
headY = 0

tailX = 0
tailY = 0

tailVisitedCoordinates = []
headVisitedCoordinates = []

def processCommand(command: str):
  global headX, headY, tailX, tailY
  direction = command.split(" ")[0]
  amount = int(command.split(" ")[1])

  for i in range(amount):
    headVisitedCoordinates.append([headX, headY])

    if direction == "R":
      headX += 1
    if direction == "L":
      headX -= 1
    if direction == "U":
      headY += 1
    if direction == "D":
      headY -= 1

    makeTailFollow()

  tailVisitedCoordinates.append([tailX, tailY])

def makeTailFollow():
  global headX, headY, tailX, tailY
  tailVisitedCoordinates.append([tailX, tailY])
  differenceX = abs(headX - tailX)
  differenceY = abs(headY - tailY)

  if differenceX > 1 or differenceY > 1:
    #Head and tails are on same X line
    if tailY == headY:
      if tailX < headX:
        tailX += 1
        return None
      elif tailX > headX:
        tailX -= 1
        return None
    #Head and tails are on same Y line
    if tailX == headX:
      if tailY < headY:
        tailY += 1
        return None
      elif tailY > headY:
        tailY -= 1
        return None
    #Head and tails are not equal, move diagonally
    if differenceX > differenceY:
      tailY = headY
      if tailX < headX:
        tailX += 1
        return None
      elif tailX > headX:
        tailX -= 1
        return None
    elif differenceY > differenceX:
      tailX = headX
      if tailY < headY:
        tailY += 1
        return None
      elif tailY > headY:
        tailY -= 1
        return None

def removeDuplicates(arr):
  result = []

  for i in arr:
    if i not in result:
      result.append(i)
  return result

for motion in motions:
  processCommand(motion)

tailVisitedCoordinates = removeDuplicates(tailVisitedCoordinates)

print("The tail of the rope has visited", len(tailVisitedCoordinates), "positions at least once")