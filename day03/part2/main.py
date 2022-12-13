from get_alphabet_score import *
from get_shared_letter import *

with open("day03/data/rucksacks.txt") as file:
  lines = file.readlines()

totalPriority = 0
currentLine = 1
currentGroupRucksack = []

for line in lines:
  currentGroupRucksack.append(line.strip())

  if currentLine % 3 == 0:
    priority = getAlphabetScore(getSharedLetter(currentGroupRucksack[0],currentGroupRucksack[1],currentGroupRucksack[2]))
    totalPriority += priority
    currentGroupRucksack.clear()

  currentLine += 1

print("The total priority is",totalPriority)