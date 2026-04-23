#вводим списки материалов
mat1 = ['mel', 'klay', 'mjel']
mat2 = ['mel', 'chel', 'shmel']
mat3 = ['mel', 'klay', 'benbaloben']
mat_obsh = mat1 + mat2 + mat3
#находим уникальные материалы из всех списков
mat_unik = list(set(mat_obsh))
print(mat_unik)
#находим общие материалы из всех списков
for i in range(len(mat_unik)):
    if (mat_unik[i] in mat1) and (mat_unik[i] in mat2) and (mat_unik[i] in mat3):
        print(mat_unik[i])
#находим материалы которые есть только в первом списке
for i in range(len(mat_unik)):
    if (mat_unik[i] in mat1) and (not(mat_unik[i] in mat2)) and (not(mat_unik[i] in mat3)):
        print(mat_unik[i])
#находим общие материалы ровно из двух списков
sets = [set(mat1), set(mat2), set(mat3)]
print(sets)
result = [el for el in mat_unik if sum(el in s for s in sets) == 2]
print(result)
