# Ejercicio 1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Ejercicio 2
c = B.union(A)
print(c)

# Ejercicio 3
print(A.intersection(B))

# Ejercicio 4
print(A.issubset(B))

# Ejercicio 5
print(A.isdisjoint(B))

# Ejercicio 6
print(B.union(A))
print(A.union(B))

# Ejercicio 7
print(A.symmetric_difference(B))

# Ejercicio 8
del A
del B