# =============================================
# USER INPUT - Curso Python for Brainrot Brains
# =============================================
# input() = pedir datos al usuario
# IMPORTANTE: Todo lo que entra por input SIEMPRE es texto (string)

print("===== EJEMPLO BÁSICO =====")

# Pedimos nombre y edad (ambos serán texto)
name = input("¿Cómo te llamas? ")
age = input("¿Cuántos años tienes? ")

print(f"Hola {name}, tienes {age} años.")
print()  # línea en blanco


# =============================================
print("===== OTRO EJEMPLO =====")

city = input("¿En qué ciudad vives? ")
hobby = input("¿Cuál es tu hobby favorito? ")

print(f"Vives en {city} y te gusta {hobby}.")
print()


# =============================================
print("===== INPUT CON CONTEXTO =====")

food = input("¿Comida favorita? ")
sport = input("¿Deporte favorito? ")

print(f"Wow, te encanta {food} y disfrutas hacer/seguir {sport}. Cool!")
print()


# =============================================
print("===== INPUT NUMÉRICO (SIN CASTEO) =====")

# Aunque parezca número, sigue siendo TEXTO
age2 = input("Dime tu edad nuevamente: ")

# Esto NO suma. Solo junta los textos
print(f"Dentro de 10 años tendrás: {age2}10")
print()


# =============================================
print("===== ERROR TÍPICO: SUMAR INPUTS =====")

num1 = input("Dame un número: ")
num2 = input("Dame otro número: ")

# Esto concatena texto, no suma
print(f"Resultado: {num1 + num2}")

print("En el próximo video aprenderás a convertir texto a número ✅")
print()


# =============================================
# 👇 EJERCICIO 1 (hazlo tú)
# Crea variables pidiendo al usuario:
# - Tu animal favorito
# - Tu color favorito
# - Tu videojuego o serie favorita
#
# Luego imprime una frase como:
# "Me encanta el animal ____, mi color favorito es ____ y mi serie favorita es ____"
# Usa f-strings ✅

animal_fav = input("dime tu animal favorito ")
color_fav = input("dime tu color favorito ")
videojuego_fav = input("dime tu videojuego favorito ")

f"Me encanta el animal {animal_fav}  , mi color favorito es {color_fav} y mi serie favorita es {videojuego_fav}"



# =============================================
# 👇 EJERCICIO 2 (hazlo tú)
# Pide:
# - Nombre de una película
# - Año de estreno
# - Actor o actriz principal


#
# Imprime algo como:
# "La película ____ se estrenó en ____ y el protagonista es ____"
# Usa input() y f-strings ✅

movie = input("dime una pelicula")
year = input("dime un anio")
main_actor = input("dime el actor principal")
print(f"La película {movie} se estrenó en {year} y el protagonista es {main_actor}")


# =============================================
# 🎯 NOTA
# Aún NO convertimos texto a número. Eso viene en el siguiente video:
# 👉 Type Casting
