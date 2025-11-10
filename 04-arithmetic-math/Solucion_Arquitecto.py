# Aquí tienes un ejercicio completo que combina todas las herramientas matemáticas avanzadas que hemos visto. 🏗️
# Ejercicio: El Arquitecto Matemático

# Escenario:
# Eres un arquitecto diseñando un parque. Necesitas realizar varios cálculos precisos para comprar materiales y analizar el clima del lugar.

# Tu misión (Instrucciones):
# Crea un script de Python llamado proyecto_parque.py y realiza los siguientes pasos en orden.
# ¡No olvides importar lo necesario!

# -----------------------------------------
# Preparación:
# Importa el módulo math.
import math

# -----------------------------------------
# La Fuente Circular (math.pi, pow, round):
# Diseñas una fuente con radio de 4.5 metros.
# Calcula su área usando la fórmula: Área = π × radio². (Usa math.pi y pow()).
# Muestra el resultado redondeado a 2 decimales usando round().
radio_fuente = 4.5
area_fuente = math.pi * pow(radio_fuente, 2)
print("Área de la fuente:", round(area_fuente, 2), "m²")

# -----------------------------------------
# La Zona de Juegos Cuadrada (math.sqrt):
# Tienes un terreno de 100 m² exactos para un parque cuadrado.
# Calcula cuánto debe medir cada lado usando la raíz cuadrada.
area_parque = 100
lado_parque = math.sqrt(area_parque)
print("Cada lado del parque mide:", round(lado_parque, 2), "m")

# -----------------------------------------
# Vallado de Seguridad (math.ceil):
# El perímetro de la fuente circular es de aproximadamente 28.27 metros.
# La valla se vende solo en paneles completos de 1 metro.
# Usa math.ceil() para saber cuántos paneles necesitas comprar.
perimetro_fuente = 28.27
paneles = math.ceil(perimetro_fuente)
print("Paneles de valla necesarios:", paneles)

# -----------------------------------------
# Plantando Árboles (math.floor):
# Tienes un presupuesto de 350€ para árboles.
# Cada árbol cuesta 40€.
# Usa math.floor() para calcular cuántos árboles puedes comprar como máximo (no te venden medio árbol).
presupuesto = 350
precio_arbol = 40
arboles = math.floor(presupuesto / precio_arbol)
print("Número máximo de árboles que puedes comprar:", arboles)

# -----------------------------------------
# Análisis del Clima (max, min, abs):
# Las temperaturas previstas para la inauguración son: -3, 12, 8, 25, -5.
# Encuentra la temperatura máxima y mínima esperada.
# Calcula la diferencia real (magnitud) entre la temperatura actual (-3) y la temperatura ideal (20) usando abs().
temperaturas = [-3, 12, 8, 25, -5]
max_temp = max(temperaturas)
min_temp = min(temperaturas)
diferencia = abs(-3 - 20)

print("Temperatura máxima:", max_temp, "°C")
print("Temperatura mínima:", min_temp, "°C")
print("Diferencia con la temperatura ideal:", diferencia, "°C")
