monkeys = []

#place data into dictionary
with open("day11/data/monkeys.txt") as file:
  lines = file.readlines()

  currentMonkey = {"items": [], "operation": "", "test": "", "ifTrue": 0, "ifFalse": 0, "itemsInspected": 0}
  for line in lines:
    line = line.strip()
    if "Starting items:" in line:
      itemsArray = line.split(": ")[1].strip().split(",")
      itemsArray = [int(x) for x in itemsArray]
      currentMonkey["items"] = itemsArray
    if "Operation:" in line:
      operation = line.split(": ")[1].strip()
      currentMonkey["operation"] = operation
    if "Test:" in line:
      test = int(line.split("by ")[1].strip())
      currentMonkey["test"] = test
    if "If true:" in line:
      ifTrue = int(line.split("monkey")[1].strip())
      currentMonkey["ifTrue"] = ifTrue
    if "If false:" in line:
      ifFalse = int(line.split("monkey")[1].strip())
      currentMonkey["ifFalse"] = ifFalse
    if line == "":
      monkeys.append(currentMonkey)
      currentMonkey = {"items": [], "operation": "", "test": "", "ifTrue": 0, "ifFalse": 0, "itemsInspected": 0}

for monkey in monkeys:
  print(monkey)

def playRound():
  currentMonkey = 0
  for monkey in monkeys:
    operation = monkey["operation"].split("=")[1].strip()
    test = monkey["test"]
    ifTrue = monkey["ifTrue"]
    ifFalse = monkey["ifFalse"]
    print("Monkey", currentMonkey)

    itemsToBeRemoved = []
    for item in monkey["items"]:
      print(" Monkey inspects an item with a worry level of", item)
      monkeys[currentMonkey]["itemsInspected"] += 1
      worryValue = eval(operation.replace('old', str(item)))
      print("   Worry level is increased to", worryValue)
      newWorryValue = int(worryValue / 3)
      print("   Monkey gets bored with item. Worry level is reduced to", newWorryValue)
      if newWorryValue % test == 0:
        itemsToBeRemoved.append(item)
        monkeys[ifTrue]["items"].append(newWorryValue)
        print("   Current worry level IS divisible by", test)
        print("   Item with worry", newWorryValue, "is thrown to monkey", ifTrue)
      else:
        itemsToBeRemoved.append(item)
        monkeys[ifFalse]["items"].append(newWorryValue)
        print("   Current worry level is NOT divisible by", test)
        print("   Item with worry", newWorryValue, "is thrown to monkey", ifFalse)
    for item in itemsToBeRemoved:
      monkeys[currentMonkey]["items"].remove(item)
    print("")
    currentMonkey += 1

amountOfRounds = 20
for i in range(amountOfRounds):
  playRound()

itemsInspected = []
for monkey in monkeys:
  itemsInspected.append(monkey["itemsInspected"])

itemsInspected = sorted(itemsInspected, reverse=True)
print(itemsInspected[0] * itemsInspected[1])