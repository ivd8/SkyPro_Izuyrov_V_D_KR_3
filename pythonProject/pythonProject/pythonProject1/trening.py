def get_longest(words):
  longest_word = ""
  for word in words[]:
    if len(word) > len(longest_word):
      longest_word = word
      return longest_word
      continue

    else:
      return longest_word
      continue
# Не удаляйте код ниже, он нужен для проверки

words = input().split(" ")
result = get_longest(words)
print(result)