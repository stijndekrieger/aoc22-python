def getSharedLetter(string1, string2, string3):
  shared_letter = set(string1).intersection(set(string2), set(string3))
  return "".join(str(x) for x in shared_letter)