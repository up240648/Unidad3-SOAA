
# Nivel 1

#Act 1
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
# Ejemplo de uso:
print(random_user_id())  


#Act 2 
def user_id_gen_by_user():
    num_chars = int(input("Ingresa el número de caracteres para el ID: "))
    num_ids = int(input("Ingresa el número de IDs a generar: "))
    ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        ids.append(user_id)
    return '\n'.join(ids)
print(user_id_gen_by_user()) 


#Act 3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

#Act 4
print(rgb_color_gen()) 

#Nivel 2

#Act 1
def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        hex_color = f'#{random.randint(0, 0xFFFFFF):06x}'
        hex_colors.append(hex_color)
    return hex_colors

# Act 2
print(list_of_hexa_colors(5)) 

#Act 3
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f'rgb({r},{g},{b})')
    return rgb_colors

#Act 4
print(list_of_rgb_colors(5)) 


#Act 5
def generate_colors(color_type, num_colors):
    colors = []
    if color_type == 'hexa':
        for _ in range(num_colors):
            hex_color = f'#{random.randint(0, 0xFFFFFF):06x}'
            colors.append(hex_color)
    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f'rgb({r},{g},{b})')
    return colors

#Act 6
print(generate_colors('hexa', 3)) 
print(generate_colors('rgb', 1))  

#Nivel 3

#Act 1
import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

#Act 2
print(shuffle_list([1, 2, 3, 4, 5])) 


#Act 3
def unique_random_numbers():
    return random.sample(range(10), 7)

#Act 4
print(unique_random_numbers())

