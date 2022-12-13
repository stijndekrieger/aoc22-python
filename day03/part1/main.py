from get_alphabet_score import *
from get_shared_letter import *

with open("day03/data/rucksacks.txt") as file:
  lines = file.readlines()

totalPriority = 0

for line in lines:
  lineLength = len(line.strip())
  compartment1 = line[:lineLength // 2]
  compartment2 = line[lineLength // 2:]

  priority = getAlphabetScore(getSharedLetter(compartment1, compartment2))

  totalPriority += priority

print("The total priority is",totalPriority)