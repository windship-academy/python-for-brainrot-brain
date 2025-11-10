# Paso 1: saldo inicial
saldo = int(input("Escribe tu saldo inicial en €: "))
print(f"Tu saldo inicial es: {saldo} €")
# Paso 2: ingreso extra
ingreso = int(input("Ingresa un ingreso extra: "))
saldo += ingreso
print(f"Después del ingreso extra: {saldo} €")
# Paso 3: gasto inesperado
gasto = int(input("Ingresa un gasto inesperado: "))
saldo -= gasto
print(f"Después de pagar el gasto: {saldo} €")
# Paso 4: inversión o ahorro
saldo *= 2
print(f"Después de ahorrar/invertir: {saldo} €")

# División con atajo
saldo /= 2
print(f"Después de dividir (atajo /=): {saldo} €")
# Paso 6: resto de pagos
resto = saldo % 7
# Paso 7: exponente simple
saldo **= 2
print(f"Saldo al cuadrado: {saldo} €")
