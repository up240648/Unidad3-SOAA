# Ejercicio 1
Perro = {}

# Ejercicio 2
Perro['Nombre'] = 'solovino',
Perro['Color'] = 'cafe'
Perro['Rasa'] = 'chihuahua',
Perro['Piernas'] = '4'
Perro['Edad'] = '2'

# Ejercicio 3
estudiante = {
    'nombre': 'Yahir',
    'apellido': 'Lopez',
    'género': 'Masculino',
    'edad': 18,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'Análisis de Datos'],
    'país': 'Mexico',
    'ciudad': 'aguascalientes',
    'dirección': 'ciudad gotica 123, ags'
}

# Ejercicio 4
longitud_estudiante = len(estudiante)
print(f"Longitud del diccionario estudiante: {longitud_estudiante}")

# Ejercicio 5
habilidades = estudiante['habilidades']
print(f"Habilidades: {habilidades}")
print(f"Tipo de dato de habilidades: {type(habilidades)}") 

# Ejercicio 6

estudiante['habilidades'].append('Aprendizaje Automático')
estudiante['habilidades'].append('Desarrollo Web')

# Ejercicio 7
claves_estudiante = list(estudiante.keys())
print(f"Claves del diccionario estudiante: {claves_estudiante}")

# Ejercicio 8
valores_estudiante = list(estudiante.values())
print(f"Valores del diccionario estudiante: {valores_estudiante}")

# Ejercicio 9
items_estudiante = list(estudiante.items())
print(f"Diccionario estudiante como lista de tuplas: {items_estudiante}")

# Ejercicio 10
del estudiante['dirección']
print(f"Diccionario estudiante después de eliminar dirección: {estudiante}")

# Ejercicio 11
del estudiante