with open("day04/data/section-assignments.txt") as file:
  lines = file.readlines()

totalCount = 0

def isInRange(section1, section2):
  start1, end1 = section1.split("-")
  start1 = int(start1)
  end1 = int(end1)

  start2, end2 = section2.split("-")
  start2 = int(start2)
  end2 = int(end2)

  if start1 >= start2 and end1 <= end2:
    return True
  if start2 >= start1 and end2 <= end1:
    return True
  return False

for line in lines:
  section1 = line.split(",")[0].strip()
  section2 = line.split(",")[1].strip()
  if isInRange(section1,section2):
    totalCount += 1

print("There are",totalCount,"pairs that fully contain the other")