# =========================================
# IF / ELSE & CLAÚSULAS DE PROTECCIÓN - Curso Python for Brainrot Brains
# =========================================
# En este video aprenderás a usar condicionales en Python:
# - IF / ELSE permite que tu programa tome decisiones.
#   Ejecuta un bloque de código si una condición se cumple (IF),
#   y otro bloque si no se cumple (ELSE).
#

# ------------------------------

# Simple ejemplo
# age = 17
#
# if age >= 18:
#     print("eres mayor de edad")
# else:
#     print("eres menor de edad")

# age = int(input("Escribe tu edad: "))
#
# if age >= 18:
#     print(f"Tienes {age} años y eres mayor de edad ✅")
# else:
#     print(f"Tienes {age} años y eres menor de edad 🚫")
#

# respuesta = input("quieres continuar? (si/no)")
#
# if respuesta == "si":
#     print ("Perfecto, seguimos adelante")
# else:
#     print("Vale, nos detenemos")


# name = input("Escribe tu nombre: ")
#
# # Cláusula de protección
# if name == "":
#     print("No escribiste tu nombre 😭")
# else:
#     print(f"Hola {name}, bienvenido 👋")


# grade = int(input("¿Qué nota sacaste? "))
#
# if grade >= 7:
#     print ("sobresaliente")
# elif grade >= 5:
#     print ("aprobado")
# else:
#     print("suspendido")


# password = input("Escribe tu contraseña: ")
#
# if password == "":
#     print("No escribiste ninguna contraseña 😭")
# elif password == "python123":
#     print("Contraseña correcta ✅")
# else:
#     print("Contraseña incorrecta 🚫")

#
# is_student = False
#
# if is_student:
#     print("Puedes acceder a descuentos para estudiantes")
# else:
#     print("no tienes descuentos")

# =============================================
# MINI EJERCICIO — If/Else básico con cláusula de protección
# =============================================

# Paso 1 — Pedir nombre y edad
name = input("Escribe tu nombre: ")
age = input("Escribe tu edad: ")