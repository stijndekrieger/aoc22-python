with open("day02/data/rps-strategy.txt") as file:
  lines = file.readlines()

totalScore = 0

def playRound(enemyMove, myMove) :
  score = 0
  match myMove:
    case "Rock":
      score += 1
      match enemyMove:
        case "A":
          score += 3
        case "B":
          score += 0
        case "C":
          score += 6
    case "Paper":
      score += 2
      match enemyMove:
        case "A":
          score += 6
        case "B":
          score += 3
        case "C":
          score += 0
    case "Scissors":
      score += 3
      match enemyMove:
        case "A":
          score += 0
        case "B":
          score += 6
        case "C":
          score += 3
  return score

def decideMove(enemyMove, strategy) :
  move = "Rock"
  match strategy:
    case "X":
      match enemyMove:
        case "A":
          move = "Scissors"
        case "B":
          move = "Rock"
        case "C":
          move = "Paper"
    case "Y":
      match enemyMove:
        case "A":
          move = "Rock"
        case "B":
          move = "Paper"
        case "C":
          move = "Scissors"
    case "Z":
      match enemyMove:
        case "A":
          move = "Paper"
        case "B":
          move = "Scissors"
        case "C":
          move = "Rock"
  return move


for line in lines:
  enemyMove = line.split()[0]
  strategy = line.split()[1]
  totalScore += playRound(enemyMove, decideMove(enemyMove, strategy))

print("Total score is", totalScore)