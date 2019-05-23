cities = {"city": "Москва", "temperature": "20"}
print(cities["city"])
cities['temperature'] = int(cities['temperature'])-5
print(cities)

# if cities.get('country') == None:#Данный вариант Добавляет элемент в словарь
#     cities['country'] = "Россия"
#     print(cities['country'])

cities.get("country" , "Россия") # а этот не добавляет
#print(cities.get("country","Россия")) # выводит значение по умолчанию, но не добавляеьт его в словарь

cities["date"] = '27.05.2019'
print(cities)
print(len(cities))