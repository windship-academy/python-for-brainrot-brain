# ============================================================
# CLASE: Operadores lógicos en Python + uso con condicionales IF
# ============================================================
#
# En esta clase veremos:
#
# 1. Qué son los operadores lógicos:
#       - AND  → todas las condiciones deben ser True
#       - OR   → con una sola condición True basta
#       - NOT  → invierte un valor (True → False / False → True)
#
# 2. Cómo funcionan estos operadores con valores booleanos.
#
# 3. Cómo combinarlos dentro de estructuras IF.
#
# 4. Ejemplos prácticos: edad, login, descuentos, permisos, etc.
#
# El objetivo es aprender a construir condiciones claras y fáciles
# de entender sin usar temas avanzados todavía.


usuario_baneado = True
tiene_cuenta = True
if tiene_cuenta and not usuario_baneado:
    print("Acceso permitido")
else:
    print("Acceso denegado")