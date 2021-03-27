word = input()

array = []

for i in range(len(word)):
  array.append(word[-(i+1):])

array = sorted(array)

for k in array:
  print(k)