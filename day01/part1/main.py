with open("day01/data/calories.txt") as file:
  lines = file.readlines()

highestValue = 0
currentValue = 0

for line in lines:
  if line.strip():
    currentValue += int(line)
  else:
    if currentValue > highestValue:
      highestValue = currentValue
    currentValue = 0

print("The elf with the most calories has", str(highestValue), "calories.")