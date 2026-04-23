#вводим переменные
cena = 67
kolvo = 52
itog = kolvo*cena
#цикл для проверки скидки и вывод
if itog < 1000:
    itog = itog * 1
elif 1000 <= itog <= 5000:
    itog = itog * 0.95
else:
    itog = itog * 0.9
print(round(itog, 1))
