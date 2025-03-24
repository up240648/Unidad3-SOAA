# Ejercicio 1
tupla_vacia = ()

# Ejercicio 2
hermanas = ('Alexa', 'Cortez', 'Fernanda') 
hermanos = ('Saul', 'Obed')  

# Ejercicio 3
hermanos_y_hermanas = hermanas + hermanos
print(hermanos_y_hermanas) 

# Ejercicio 4
cantidad_siblings = len(hermanos_y_hermanas)
print(f"Tengo {cantidad_siblings} hermanos y hermanas.")  

# Ejercicio 5
padre = 'Pedro'
madre = 'Lily'
familia = hermanos_y_hermanas + (padre, madre)
print(familia)