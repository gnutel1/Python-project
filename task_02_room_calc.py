#вводим переменные
lenght = 3.5
width = 2.5
height = 3.3423231
#выполняем расчет
pl_pola = lenght*width
pl_sten1 = height*lenght
pl_sten2 = height*width
obsch_pl_sten = (pl_sten1 + pl_sten2) * 2
obem = lenght*width*height
st_pok_m = 125
itog_stoim = st_pok_m*obsch_pl_sten
#округляем и выводим итог. значение
print(round(itog_stoim, 2))
