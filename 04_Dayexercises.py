# Ejercicio 1

No1 = 'Thirty'
No2 = ' Days'
No3 = 'Of'
No4 = 'Python'
space = ' '
full = No1 +space+ No2 +space+ No3 +space+ No4
print(full)
print(len(full))

# Ejercicio 2

no1 = 'Coding'
no2 = 'For'
no3 = 'All'
space = ' '
Full = no1 + space + no2 + space + no3 
print(Full)
print(len(Full))

# Ejercicio 3

company = 'Coding For All'

# Ejercicio 4

print(company)

# Ejercicio 5

print(len(company))

# Ejercicio 6

print(company.upper())
# Ejercicio 7

print(company.lower())

# Ejercicio 8

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Ejercicio 9

print(company[0:6])

# Ejercicio 10

print(company.index('Coding'))

# Ejercicio 11

print(company.replace('Coding','Pytohn'))

# Ejercicio 12

oracion = 'Pytohn For Everyone' 
print(oracion.replace('Everyone','All'))

#Ejercicio 13

print(company.split())

# Ejercicio 14

empresas = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(empresas.split())

# Ejercicion 15

print(company[0])

# Ejercicio 16

print(company[13])

# Ejercicio 17

print(company[10])

# Ejercicio 18

Frase = 'Python For Everyone'
acronimo = "".join(word[0] for word in Frase.split())
print(acronimo)

# Ejercicio 19 

Frase2 = 'Coding For All'
acronimo2 = "".join(word[0] for word in Frase2.split())
print(acronimo2)

# Ejercicio 20

print(company.index('C'))

# Ejercicio 21

print(company.index('F'))

# Ejercicio 22

print(company.rfind('l'))

# Ejercicio 23

O = 'You cannot end a sentence with because because because is a conjunction'
print(O.index('because'))

# Ejercicio 24

print(O.rindex('because'))

# Ejercicio 25

print(company.endswith('coding'))

# Ejercicio 26

print('   Coding For All      '.strip()) 

# Ejercicio 27

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Ejercicio 28

bibliotecas_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(bibliotecas_python))

# Ejercicio 29

print("I am enjoying this challenge.\nI just wonder what is next.")

# Ejercicio 30

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# Ejercicio 31

radio = 10
area = 3.14 * radio ** 2
print(f"The area of a circle with radius {radio} is {area} meters square.")  # Salida: 'The area of a circle with radius 10 is 314 meters square.'

# Ejercicio 32

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")



