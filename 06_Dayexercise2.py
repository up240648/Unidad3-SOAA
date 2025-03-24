# Ejercicio 1
familia = ('Alexa', 'Cortez', 'Fernanda', 'Saul', 'Obed', 'Pedro', 'Lily')

# Ejercicio 2 
hermanos_y_hermanas, padre, madre = familia[:-2], familia[-2], familia[-1]
print(f"Hermanos y hermanas: {hermanos_y_hermanas}") 
print(f"Padre: {padre}, Madre: {madre}")

# Ejercicio 3
frutas = ('Uva', 'Manzana', 'Plantano')
vegetales = ('Lechuga', 'Tomate', 'Cebolla')
productos_animales = ('Leche', 'Queso', 'Huevo')

# Ejercicio 4
food_stuff_tp = frutas + vegetales + productos_animales
print(food_stuff_tp) 

# Ejercicio 5
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt) 

# Ejercicio 6
if len(food_stuff_lt) % 2 != 0:
    middle_item = food_stuff_lt[len(food_stuff_lt) // 2]
    print(f"Elemento del medio: {middle_item}")
else:
    middle_items = food_stuff_lt[len(food_stuff_lt) // 2 - 1: len(food_stuff_lt) // 2 + 1]
    print(f"Elementos del medio: {middle_items}")

# Ejercicio 7
primeros_tres_ultimos_tres = food_stuff_lt[:3] + food_stuff_lt[-3:]
print(f"Primeros tres y últimos tres elementos: {primeros_tres_ultimos_tres}") 

# Ejercicio 8
del food_stuff_tp

# Ejercicio 9 
nordic_countries = ('Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland')
print('Estonia' in nordic_countries)  
print('Iceland' in nordic_countries) 