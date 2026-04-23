mat = ['titan', 'shlakobeton', 'glina', 'nenutonovskaya zhidkost', 'cement']
print(mat[:1])
a = len(mat) - 1
print(mat[a:])
print(mat[1:a])
mat.append("gudron")
mat.append('zhizha')
mat.pop(1)
print(mat, len(mat))
