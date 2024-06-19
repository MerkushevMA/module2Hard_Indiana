import random
choice = input('Рандому великому доверимся мы? (Да/нет): ')
if choice.lower() == 'да':
    number_indi = random.choice(range(3, 21))
else:
    number_indi = int(input('Тогда попрошу ввести число камня инди: '))
print('Число камня Инди:', number_indi)
if number_indi % 2 == 0:
    half_number_indi = number_indi // 2
else:
    half_number_indi = (number_indi // 2) + 1
result = ''
part_number = ''
for i in range(1, half_number_indi):
    for j in range(i, number_indi):
        if number_indi % (i + j) == 0 and i != j:
            part_number = str(i) + str(j)
            result = result + part_number
print('Код жизни:', int(result))
