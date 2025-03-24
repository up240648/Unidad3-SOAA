# Ejercicio 1
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ejercicio 2

edades.sort()
edad_minima = min(edades)
edad_maxima = max(edades)
print("Edades ordenadas:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

# Ejercicio 3

edades.append(edad_minima)
edades.append(edad_maxima)
print("Edades después de agregar mínima y máxima:", edades)

# Ejercicio 4

longitud_edades = len(edades)
if longitud_edades % 2 == 0:
    mediana = (edades[longitud_edades // 2 - 1] + edades[longitud_edades // 2]) / 2
else:
    mediana = edades[longitud_edades // 2]
print("Mediana de las edades:", mediana)

# Ejercicio 5

promedio_edades = sum(edades) / len(edades)
print("Edad promedio:", promedio_edades)

# Ejercicio 6

rango_edades = edad_maxima - edad_minima
print("Rango de las edades:", rango_edades)

# Ejercicio 7

diferencia_min = abs(edad_minima - promedio_edades)
diferencia_max = abs(edad_maxima - promedio_edades)
print("Diferencia entre mínima y promedio:", diferencia_min)
print("Diferencia entre máxima y promedio:", diferencia_max)

# Ejercicio 8

paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
longitud_paises = len(paises)
if longitud_paises % 2 == 0:
    paises_medios = paises[longitud_paises // 2 - 1:longitud_paises // 2 + 1]
else:
    paises_medios = [paises[longitud_paises // 2]]
print("País(es) del medio:", paises_medios)

# Ejercicio 9

mitad = (longitud_paises + 1) // 2 
primera_mitad = paises[:mitad]
segunda_mitad = paises[mitad:]
print("Primera mitad de países:", primera_mitad)
print("Segunda mitad de países:", segunda_mitad)

# Ejercicio 10

primeros_tres, *paises_escandinavos = paises
print("Primeros tres países:", primeros_tres)
print("Países escandinavos:", paises_escandinavos)
