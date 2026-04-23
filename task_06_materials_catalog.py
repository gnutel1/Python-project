#вводим список материалов
mat = ['titan', 'shlakobeton', 'glina', 'nenutonovskaya zhidkost', 'cement']
#выводим первый последний и среднии материалы из списка
print(mat[:1])
a = len(mat) - 1
print(mat[a:])
print(mat[1:a])
#добавляем новые материалы и удаляем старый
mat.append("gudron")
mat.append('zhizha')
mat.pop(1)
#выводим конечный результат
print(mat, len(mat))
