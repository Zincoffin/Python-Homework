# num 1
l = "лфилыифнрнфыринфриннфннннннннр"
count = 1
max = 0
for i in range(len(l)-1):
  if l[i] == "н" and l[i+1] == "н":
    count += 1
  else:
    count = 1
  if count > max:
    max = count
print(f"Самая длинная последовательность: {max} \nПреобразованная строка: {l.replace("н" * max, "!" * max)}")
# num 2
l = 'ываыаыва(нннн)ыавыва'
print(((l.split("("))[1].split(")"))[0])
# num 3
l = "притмфьыао лфьлфмьдл акация фдэээдвыьжд адаптация"
list = l.split(" ")
for i in list:
  if (i[0] == "а" or i[0] == "А") and i[-1] == "я":
    if i == list[-1]:
      print(i, end=".")
    else:
      print(i, end=", ")