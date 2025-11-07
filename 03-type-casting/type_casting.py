# =============================================
# TYPE CASTING - Curso Python for Brainrot Brains
# =============================================
# En este video aprenderás por qué necesitamos convertir tipos de datos en Python.
# Veremos qué pasa cuando intentamos hacer operaciones con texto
# y cómo solucionarlo con int(), float() y str().

# ------------------------------
print("===== OPERACIONES NORMALES =====")

# Operaciones matemáticas básicas con números
num1 = 10
num2 = 5

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")
print()

# ------------------------------
print("===== PROBLEMA CON INPUT() =====")

# Ahora pedimos los mismos valores al usuario
# Pero recuerda: todo lo que entra por input() es TEXTO (string)

num1 = input("Dame un número: ")
num2 = input("Dame otro número: ")

print()
print("Tipos actuales de num1 y num2:")
print(type(num1))  # <class 'str'>
print(type(num2))  # <class 'str'>

# Intentemos sumar directamente
print(f"Resultado sin convertir: {num1 + num2}")
# Esto concatena texto, no suma números. Ej: 5 + 5 = 55
print()

# ------------------------------
print("===== SOLUCIÓN: TYPE CASTING =====")

# Convertimos el texto a número entero con int()
num1 = int(num1)
num2 = int(num2)

# Ahora sí, podemos operar correctamente
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")
print()

# ------------------------------
print("===== CONVERTIR A FLOAT (DECIMALES) =====")

# Ejemplo con decimales
price1 = float(input("Precio del primer producto: "))
price2 = float(input("Precio del segundo producto: "))

total = price1 + price2
print(f"El precio total es: {total} €")
print()

# ------------------------------
print("===== CONVERTIR NÚMERO A TEXTO =====")

# A veces queremos pasar de número a texto
age = 20
age_text = str(age)

print("Edad como texto: " + age_text)
print(f"También puedes hacerlo así: {age_text}")
print()

# ------------------------------
print("===== ERROR TÍPICO =====")
print("Si intentas convertir algo que no es número, Python lanza un error 👇")
print("int('hola')  # ❌ ValueError")
print()

# ------------------------------

