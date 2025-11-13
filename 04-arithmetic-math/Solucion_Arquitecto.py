import math

print("--- 🏗️ INICIO DEL PROYECTO PARQUE ---")

# 1. La Fuente Circular (pi, pow, round)
radio_fuente = 4.5
area_fuente = math.pi * pow(radio_fuente, 2)
print(f"Área de la fuente (exacta): {area_fuente}")
print(f"Área de la fuente (redondeada): {round(area_fuente, 2)} m²")

# 2. La Zona de Juegos (sqrt)
area_juegos = 100
lado_juegos = math.sqrt(area_juegos)
print(f"Cada lado de la zona de juegos debe medir: {lado_juegos} metros")

# 3. Vallado (ceil - redondeo hacia arriba)
perimetro_fuente = 28.27
paneles_necesarios = math.ceil(perimetro_fuente)
print(f"Necesitamos comprar {paneles_necesarios} paneles de valla.")

# 4. Presupuesto Árboles (floor - redondeo hacia abajo)
presupuesto = 350
precio_arbol = 40
num_arboles = math.floor(presupuesto / precio_arbol)
print(f"Con {presupuesto}€ podemos comprar {num_arboles} árboles.")

# 5. Análisis del Clima (max, min, abs)
temp1, temp2, temp3, temp4, temp5 = -3, 12, 8, 25, -5

temp_max = max(temp1, temp2, temp3, temp4, temp5)
temp_min = min(temp1, temp2, temp3, temp4, temp5)
print(f"La temperatura más alta será: {temp_max}°C")
print(f"La temperatura más baja será: {temp_min}°C")

temp_actual = -3
temp_ideal = 20
diferencia = abs(temp_actual - temp_ideal)
print(f"La diferencia de temperatura con la ideal es de: {diferencia}°C")

print("\n--- ✅ PROYECTO TERMINADO ---")