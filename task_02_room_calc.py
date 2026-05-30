Задача 2: Параметры помещения
Размеры помещения (в метрах)
length = 3.5    # длина 
width = 2.5     # ширина
height = 3.3423231  # высота
Вычисление площадей и объёма 
pl_pola = length * width                       
pl_sten1 = height * length                      
pl_sten2 = height * width                       
obsch_pl_sten = (pl_sten1 + pl_sten2) * 2       
obem = length * width * height                 
Стоимость покраски 
st_pok_m = 125                                 
itog_stoim = st_pok_m * obsch_pl_sten           
Вывод результатов 
print('=== Параметры помещения ===')
print(f'Площадь пола:   {round(pl_pola, 2)} м²')
print(f'Площадь стен:   {round(obsch_pl_sten, 2)} м²')
print(f'Объём:          {round(obem, 2)} м³')
print(f'Стоимость покраски стен: {round(itog_stoim, 2)} руб.')
