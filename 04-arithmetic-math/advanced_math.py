
# Paso 1: Valor absoluto (magnitud)
deuda = -500
magnitud = abs(deuda)
print(f"La magnitud de la deuda es: {magnitud}€")

# Paso 2: Redondeo
resultado = 100 / 3
print(f"Resultado exacto: {resultado}")
print(f"Redondeado: {round(resultado, 3)}")

# Paso 3: Encontrar extremos
puntuaciones = [95, 40, 12, 88, 76]

mejor_nota = max(puntuaciones)
peor_nota = min(puntuaciones)

print(f"Tu mejor nota ha sido: {mejor_nota}")
print(f"Tu peor nota ha sido: {peor_nota}")


# Paso 4: Potencia con función

potencia = pow(2,10)
print(f"2 elevado a la 10 es: {potencia}")

# Paso 5: Módulo math y Pi
import math
# Mostrar el valor de Pi
print(f"El valor de Pi es: {math.pi}")

# Ejercicio: calcular el área de un círculo
# Fórmula: área = π × radio²
radio = 5
#area = math.pi * (radio ** 2)
area = math.pi * pow(radio,2)

print(f"Área del círculo con radio {radio} es: {round(area, 2)}")

# Raíz cuadrada
numero = 81
raiz = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz}")

# Redondeo hacia arriba (Techo)
print (math.ceil(4.3))

# Redondeo hacia abajo (suelo)
print (math.floor(4.3))