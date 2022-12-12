with open("day01/data/calories.txt") as file:
  lines = file.readlines()

values = []
currentValue = 0

for line in lines:
  if line.strip():
    currentValue += int(line)
  else:
    values.append(currentValue)
    currentValue = 0

values.sort(reverse = True)
totalCalories = values[0] + values[1] + values[2]
print("The top three Elves are carrying", totalCalories, "total calories.")