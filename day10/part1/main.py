registerValue = 1
currentCycle = 1
currentCommandFinishOnCycle = 0
currentCommandIndex = 0
currentCommand = None
cycleAvailable = True
totalSignalStrength = 0

def startCommand():
  global currentCommand, currentCommandIndex, currentCommandFinishOnCycle, cycleAvailable
  with open("day10/data/signal.txt") as file:
    signals = file.readlines()
    if 0 <= currentCommandIndex < len(signals):
      currentCommand = signals[currentCommandIndex].strip()
      print("Starting command", currentCommand)
      if currentCommand == "noop":
        currentCommandFinishOnCycle = currentCycle
      else:
        currentCommandFinishOnCycle = currentCycle + 1
    else:
      print("No more commands")
    cycleAvailable = False

def finishCommand():
  global registerValue, currentCommand, currentCommandIndex
  print("Finishing command", currentCommand)
  if currentCommand != "noop":
    value = int(currentCommand.split(" ")[1])
    registerValue  += value
  currentCommand = None
  currentCommandIndex += 1

while currentCycle <= 220:
  print("Start of cycle", currentCycle, ", current value is", registerValue)
  if(currentCycle == 20 or (currentCycle - 20)% 40 == 0):
    signalStrength = currentCycle * registerValue
    totalSignalStrength += signalStrength
    print("SIGNAL STRENGTH CHECK:", signalStrength)
  if cycleAvailable:
    startCommand()

  if currentCommandFinishOnCycle == currentCycle:
    finishCommand()
    cycleAvailable = True

  print("End of cycle", currentCycle, ", current value is", registerValue)
  print("-----")
    
  currentCycle += 1
print(totalSignalStrength)