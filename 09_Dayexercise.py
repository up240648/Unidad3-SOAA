# Nivel 1

# Ejercicio 1
edad = int(input("Enter your age: "))
if edad >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - edad
    print(f"You need {years_left} more years to learn to drive.")
my_age = int(input("Enter your age: "))
your_age = int(input("Enter my age: "))

# Ejercicio 2
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
elif my_age < your_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
else:
    print("We are the same age.")

    # Ejercicio 3
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Nivel 2
    
# Ejercicio 1
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: F")
else:
    print("Invalid score entered!")

# Ejercicio 2
month = input("Enter a month (e.g., September): ").lower()
if month in ['september', 'october', 'november']:
    print("The season is Autumn.")
elif month in ['december', 'january', 'february']:
    print("The season is Winter.")
elif month in ['march', 'april', 'may']:
    print("The season is Spring.")
elif month in ['june', 'july', 'august']:
    print("The season is Summer.")
else:
    print("Invalid month entered!")

# Ejercicio 3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit name: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print(f"The modified fruit lis: {fruits}")

# Nivel 3

# Ejercicio 1
person = {
    'first_name': 'Saul',
    'last_name': 'Alonso',
    'age': 15,
    'country': 'Mexico',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Ejercicio 2
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2] 
    print(f"The middle skill is: {middle_skill}")

# Ejercicio 3
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person doesn't have Python skill.")

# Ejercicio 4
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer.")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer.")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer.")
    else:
        print("Unknown title")

# Ejercicio 5
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")