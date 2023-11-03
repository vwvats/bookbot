def count_words(text):
  words = text.split()
  return len(words)

def count_letters(text):
  words = text.split()
  letters_dict = {}

  for word in words:
    l_word = word.lower()
    for char in l_word:
      if char not in letters_dict:
        letters_dict[char] = 1
      else:
        letters_dict[char] += 1

  return letters_dict

def make_report(text):
  word_count = count_words(text)
  print(f"---- Book Report:")
  print(f"{word_count} words found in the document\n")
  letter_count = count_letters(text)
  for letter in letter_count:
    if letter.isalpha():
      print(f"The '{letter}' was found {letter_count[letter]} times")

with open("./books/frankenstein.txt") as f:
  file_contents = f.read()
  make_report(file_contents)
