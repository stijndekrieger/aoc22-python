with open("day02/data/rps-strategy.txt") as file:
  lines = file.readlines()

totalScore = 0

def playRound(enemyMove, myMove) :
  score = 0
  match myMove:
    case "X":
      score += 1
      match enemyMove:
        case "A":
          score += 3
        case "B":
          score += 0
        case "C":
          score += 6
    case "Y":
      score += 2
      match enemyMove:
        case "A":
          score += 6
        case "B":
          score += 3
        case "C":
          score += 0
    case "Z":
      score += 3
      match enemyMove:
        case "A":
          score += 0
        case "B":
          score += 6
        case "C":
          score += 3
  return score

for line in lines:
  enemyMove = line.split()[0]
  myMove = line.split()[1]
  totalScore += playRound(enemyMove, myMove)

print("Total score is", totalScore)