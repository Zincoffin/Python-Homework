s = input("Введите строку: \n").split(' ')
count = 0
for i in s:
#   s.remove('(')
#   s.remove('"')
    if i[0] == 'е' or i[0] == 'Е':
        count += 1
print(count)

