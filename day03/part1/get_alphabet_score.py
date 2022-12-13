def getAlphabetScore(letter):
  ascii_value = ord(letter)

  # If the letter is lowercase
  if ascii_value >= 97 and ascii_value <= 122:
      alphabet_score = ascii_value - 96

  # If the letter is uppercase
  elif ascii_value >= 65 and ascii_value <= 90:
      alphabet_score = ascii_value - 38

  return alphabet_score