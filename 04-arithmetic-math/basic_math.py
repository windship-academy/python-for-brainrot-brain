# =========================================
# ARITHMETIC & MATH - Curso Python for Brainrot Brains
# =========================================
# En este video aprenderás las operaciones básicas de Python
# y cómo usar los atajos de asignación.

# ------------------------------
print("===== SUMA =====")
money = 100
print(f"Valor inicial: {money}")

# Suma normal
money = money + 20
print(f"Después de sumar 20: {money}")

# Suma con atajo
money += 20
print(f"Después de sumar 20 con '+=': {money}")
print(f"Tipo de variable: {type(money)}\n")

# ------------------------------
print("===== RESTA =====")
# Resta normal
money = money - 10
print(f"Después de restar 10: {money}")

# Resta con atajo
money -= 10
print(f"Después de restar 10 con '-=': {money}")
print(f"Tipo de variable: {type(money)}\n")

# ------------------------------
print("===== MULTIPLICACIÓN =====")
# Multiplicación normal
money = money * 2
print(f"Después de multiplicar por 2: {money}")

# Multiplicación con atajo
money *= 2
print(f"Después de multiplicar por 2 con '*=': {money}")
print(f"Tipo de variable: {type(money)}\n")

# ------------------------------
print("===== DIVISIÓN =====")
# División normal
money = money / 2
print(f"Después de dividir entre 2: {money}")

# División con atajo
money /= 2
print(f"Después de dividir entre 2 con '/=': {money}")
print(f"Tipo de variable: {type(money)}\n")

# ------------------------------
print("===== POTENCIA =====")
money = 10
money = money ** 2
print(f"10 al cuadrado: {money}")

# Potencia con atajo
money **= 2
print(f"Potencia con '**=': {money}")
print(f"Tipo de variable: {type(money)}\n")

# ------------------------------
print("===== MÓDULO / RESTO DE LA DIVISIÓN =====")
remainder = money % 2
print(f"Resto de dividir {money} entre 2: {remainder}")
print(f"Tipo de variable: {type(remainder)}\n")

# ------------------------------
print("¡Listo! Hemos cubierto suma, resta, multiplicación, división, potencia y módulo,")
print("tanto con operaciones normales como con atajos (+=, -=, *=, /=, **=).")
