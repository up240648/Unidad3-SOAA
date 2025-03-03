
Age= 18
Height= 1.75
Complex= 4 + 6j

#Ejercicio 4

Base = int(input('Base: '))
height = int(input('height: '))
Area = int(0.5 * Base * height)
print('Area of a triangle:', Area)

# Ejercicio 5

side_a= int(input('side: '))
side_b= int(input('side: '))
side_c= int(input('side: '))
Perimeter = int(side_a + side_b + side_c)
print('Perimeter of a triangle:', Perimeter)

#Ejercicio 6

Lenght= int(input('Lenght: '))
Width= int(input('Width: '))
Area= int(Lenght * Width)
Perimeter= int(2 * (Lenght + Width))
print('Area of a rectangle:', Area)
print('Perimeter of a rectangle:', Perimeter)

#Ejercicio 7

Radius= int(input('Radius: '))
Area= int(3.14 * Radius ** 2)
Perimeter= int(2 * 3.14 * Radius)
print('Area of a circle:', Area)
print('Perimeter of a circle:', Perimeter)

#Ejercicio 8

x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
slope= int(y2-y1) / int(x2-x1)
print('slope:', slope)

#Ejercicio 9

Y1= int(input('y1: '))
Y2= int(input('y2: '))
X1= int(input('x1: '))
X2= int(input('x2: '))
Slope= int((Y2 - Y1) / int(X2 - X1))
print('slope:', Slope)

#Ejercicio 9

x1= int(X1)
y1= int(Y1)
x2= int(X2)
y2= int(Y2)
distance= int((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
print('distance:', distance)

#Ejercicio 10

print(Slope >= slope)
print(Slope <= slope)
print(Slope == slope)
print(Slope != slope)
print(Slope > slope)
print(Slope < slope)

#Ejercicio 11

x= int(input('x: '))
X= int(input('X: '))
y= int(x**2 + 6*X + 9)
print('y:', y)

#Ejercicio 12

print(len('python') == len('dragon'))
print(len('python') != len('dragon'))
print(len('python') < len('dragon'))
print(len('python') > len('dragon'))
print(len('python') >= len('dragon'))
print(len('python') <= len('dragon'))

#Ejercicio 13

python = 'python'
dragon = 'dragon'
print("on" in python and "on" in dragon)

#Ejercicio 14

Frase= 'I hope this course is not full of jargon'
print(Frase)
print("jargon" in Frase)

#Ejercicio 15

print("no" in python and "no" in dragon)

#Excersise 16

len('python')
print(float(len('python')))
print(str(len('python')))

#Ejercicio 17

Valor_1 = (input('Enter a number: ')) 
Remainder = float(Valor_1) % 2
if Remainder == 0:
    print('el valor es par:', Remainder)
else:
    print('el valor es impar:', Remainder)

#Ejercicio 18
    
Valor1 = (7)
Divisor = float(Valor1) / 3
if Divisor == int(2.7):
    print('True')
else:
    print('False')

#Ejercicio 19

if type(10) == '10':
    print('True')
else:
    print('False')

#Ejercicio 20

if int('9.8') == 10:
    print('True')
else:
    print('False')

#Ejercicio 21

Horaschambeadas= int(input('Horas trabajadas: '))
Pago= int(input('Pago por hora: '))
Salario= int(Horaschambeadas * Pago)
print('Salario:', Salario)

#Ejercicio 22

Years= int(input('Enter a number: '))
Valor_1= str(Years*365*24*60*60)
print('los segundos que has vivido son: ', Valor_1)

#Ejercicio 23

for i in range(1, 6):
   print (i, 1, i**2, i**3)

   