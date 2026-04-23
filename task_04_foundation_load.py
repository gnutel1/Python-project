#вводим переменную и массив
numb = 5
dni = ['pon', 'vtor', 'sred', 'chet', 'pyat', 'sybo', 'vs']
#цикл для проверки дня недели и вывод
for i in range(1, 8):
    if numb == i:
        print(dni[i-1])
