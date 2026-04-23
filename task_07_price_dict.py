mat = {'mel': 10, 'klay': 20, 'shmel': 23, 'jmel': 100, 'vasyan': 0}
mat['lak'] = 15
mat['cheremsha'] = 67
mat['klay'] = mat['klay'] * 1.1
mat.pop('jmel')
cen_sr = sum(mat.values()) / len(mat)
print(cen_sr)
print(mat)
