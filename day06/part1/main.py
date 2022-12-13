with open("day06/data/datastream.txt") as file:
  datastream = file.readline()

charactersProcessed = 0
recentCharacters = list()

def checkPacketMarker(characters: list):
  duplicateSet = set(characters)
  if len(duplicateSet) == len(characters):
    return True
  return False

for i in range(len(datastream)):
  charactersProcessed += 1
  recentCharacters.append(datastream[i])
  if len(recentCharacters) > 4:
    recentCharacters.pop(0)
    if(checkPacketMarker(recentCharacters)):
      print(recentCharacters)
      break

print("First start-of-packet marker is detected after", charactersProcessed, "characters")