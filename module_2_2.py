first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')


if first == second == third:
    print(3)

elif first == second or second == third or first == third:
    print(2)

elif first != second != third:
    print(0)