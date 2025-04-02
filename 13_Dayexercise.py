#Act 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print("Filtrados negativos y cero:", filtered_numbers)

#Act 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for sublist2 in sublist for item in sublist2]
print("Lista aplanada:", flattened_list)

#Act 3
tuples_list = [(i, 1) + tuple(i**j for j in range(1, 7)) for i in range(11)]
print("Lista de tuplas:", tuples_list)

#Act 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
transformed_countries = [[country[0].upper(), country[0][:3].upper(), city.upper()] for country, city in [item[0] for item in countries]]
print("Lista transformada de países:", transformed_countries)

#Act 5
dict_countries = [{'country': country[0].upper(), 'city': city.upper()} for country, city in [item[0] for item in countries]]
print("Lista de diccionarios:", dict_countries)

#Act 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{name[0][0]} {name[0][1]}" for name in names]
print("Lista de nombres concatenados:", concatenated_names)

#Act 7
calculate_slope_intercept = lambda x1, y1, x2, y2: ( (y2 - y1) / (x2 - x1), y1 - ((y2 - y1) / (x2 - x1)) * x1)
slope, intercept = calculate_slope_intercept(1, 2, 3, 6)
print("Pendiente y intercepto de la recta:", slope, intercept)
