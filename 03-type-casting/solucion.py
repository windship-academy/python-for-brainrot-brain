print("===== MINI EJERCICIO =====")

# 🧠 Ejercicio:
# 1️⃣ Pide dos números (con input)
# 2️⃣ Convierte a int o float
# 3️⃣ Muestra:
#     - Suma
#     - Resta
#     - Multiplicación
#     - División
# 4️⃣ BONUS: muestra todos los resultados en una sola línea con f-string

# Tu código aquí 👇
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir entre cero"

print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# ------------------------------
print("\n===== EJERCICIO EXTRA =====")

# Pide al usuario su nombre y edad
# Convierte la edad a número
# Muestra:
# "Hola [nombre], el año que viene tendrás [edad + 1] años."

name = input("¿Cómo te llamas? ")
age = int(input("¿Cuántos años tienes? "))

print(f"Hola {name}, el año que viene tendrás {age + 1} años.")
