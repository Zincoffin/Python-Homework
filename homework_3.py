n = int(input("Введите число от 1 до 100: \n"))
sum = 0
for i in range(1, n+1):
    sum += i**3
print(sum)

num1 = []
for i in range(1, 10):
  for j in range(1, 10):
    if i*j < 10:
      num1.append(" " + str(i * j))
    else:
      num1.append(str(i * j))
  print(*num1)
  num1 = []
