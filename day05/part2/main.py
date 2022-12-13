import re

with open("day05/data/crate-arrangement.txt") as file:
  lines = file.readlines()

stacks = list()

for line in lines:
  stack = list()
  for i in range(len(line.strip())):
    stack.append(line[i])
  
  stacks.append(stack)

def moveCrates(amount, fromIndex, toIndex):
  fromIndex -= 1
  toIndex -= 1

  currentNumbers = []
  for i in range(amount):
    currentNumbers.append(stacks[fromIndex].pop())
  currentNumbers.reverse()
  print(currentNumbers)

  for number in currentNumbers:
    stacks[toIndex].append(number)

with open("day05/data/rearrangement-procedure.txt") as file:
  lines = file.readlines()

for line in lines:
  numbers = re.findall(r'\d+', line)
  moveCrates(int(numbers[0]), int(numbers[1]), int(numbers[2]))

for stack in stacks:
  print(stack[-1])