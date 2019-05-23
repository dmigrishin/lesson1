digits = [3, 5, 7, 9, 10.5]
print('Начальный список:',digits)
digits.append('Python') # Добавляем элемент к списку
print(digits) 
print('Длина списка = ',len(digits))
print('Первый элемент: ',digits[0])
print('Последний элемент:',digits[-1])
print('Элементы со второго по четвертый включительно: ',digits[1:4])
del digits[-1] #удаляем последний элемент
print('Итоговый список: ',digits)