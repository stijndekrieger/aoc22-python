def getSharedLetter(string1, string2):
  shared_letter = ''.join(set(string1).intersection(string2))
  return shared_letter