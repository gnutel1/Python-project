#вводим словарь материалов и их цены
mat = {'mel': 10, 'klay': 20, 'shmel': 23, 'jmel': 100, 'vasyan': 0}
#добавляем новые материалы 
mat['lak'] = 15
mat['cheremsha'] = 67
#повышаем цену одного из материалов на 10 процентов и удаляем один материал
mat['klay'] = mat['klay'] * 1.1
mat.pop('jmel')
#находим среднею цену всех материалов и выводим
cen_sr = sum(mat.values()) / len(mat)
print(cen_sr)
print(mat)
