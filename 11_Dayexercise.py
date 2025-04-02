# Act 1

def add_two_numbers(a, b):
    return a + b

#Act 2

import math

def area_of_circle(radius):
    return math.pi * radius * radius

#Act 3

def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Todos los argumentos deben ser números."

#Act 4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Act 5

def check_season(month):
    if month in [12, 1, 2]:
        return "Invierno"
    elif month in [3, 4, 5]:
        return "Primavera"
    elif month in [6, 7, 8]:
        return "Verano"
    else:
        return "Otoño"

#Act 6

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1) if x2 != x1 else "La pendiente es indefinida"

#Act 7

import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No hay soluciones reales"

#Act 8
def print_list(lst):
    for item in lst:
        print(item)

#Act 9

def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

#Act 10 

def capitalize_list_items(lst):
    return [item.upper() for item in lst]

#Act 11

def add_item(lst, item):
    lst.append(item)
    return lst

#Act 12

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

#Act 13

def sum_of_numbers(n):
    return sum(range(n+1))

#Act 14

def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

#Act 15

def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"The number of evens are {evens}.")
    print(f"The number of odds are {odds}.")

# Nivel 2
    
#Act 1

def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"The number of evens are {evens}.")
    print(f"The number of odds are {odds}.")

#Act 2

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#Act 3

def is_empty(value):
    return len(value) == 0 if hasattr(value, '__len__') else value == ""

#Nivel 3

#Act 1

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

#Act 2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Act 3

def check_unique_elements(lst):
    return len(lst) == len(set(lst))

#Act 4

def check_same_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)

#Act 5

def is_valid_variable(variable):
    import keyword
    if not variable.isidentifier() or keyword.iskeyword(variable):
        return False
    return True

#Act 6

def most_spoken_languages():
    languages = {
        "Mandarin": 918000000,
        "Spanish": 460000000,
        "English": 377000000,
        "Hindi": 310000000,
        "Arabic": 310000000,
        "Bengali": 230000000,
        "Portuguese": 220000000,
        "Russian": 150000000,
        "Japanese": 125000000,
        "Punjabi": 120000000,
    }
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]

#Act 7

def most_populated_countries():
    countries = {
        "China": 1393409038,
        "India": 1366417754,
        "USA": 329500000,
        "Indonesia": 267670000,
        "Pakistan": 233500000,
        "Brazil": 211000000,
        "Nigeria": 206000000,
        "Bangladesh": 163000000,
        "Russia": 145900000,
        "Mexico": 127500000,
    }
    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
    return sorted_countries[:10]