with open("day06/data/datastream.txt") as file:
  datastream = file.readline()

charactersProcessed = 0
recentCharacters = list()

def checkMessageMarker(characters: list):
  duplicateSet = set(characters)
  if len(duplicateSet) == len(characters):
    return True
  return False

for i in range(len(datastream)):
  charactersProcessed += 1
  recentCharacters.append(datastream[i])
  if len(recentCharacters) > 14:
    recentCharacters.pop(0)
    if(checkMessageMarker(recentCharacters)):
      print(recentCharacters)
      break

print("First start-of-packet marker is detected after", charactersProcessed, "characters")