# calculadora python
num1 = float(input("Enter a number: "))
signo = input("introduce un signo de estos (+ - * / ** %): ")
num2 = float(input("Enter another number: "))

es_num1 = not (num1)
es_num2 = not (num2)


if signo == "+":
    solucion = num1 + num2
    print(f"{num1} + {num2} = {solucion}")

elif signo == "-":
    solucion = num1 - num2
    print(f"{num1} - {num2} = {solucion}")

elif signo == "*":
    solucion = num1 * num2
    print(f"{num1} * {num2} = {solucion}")

elif signo == "/":
    solucion = round(num1 / num2, 3)
    print(f"{num1} / {num2} = {solucion}")

elif signo == "**":
    solucion = num1 ** num2
    print(f"{num1} elevado a {num2} = {solucion}")

elif signo == "%":
    solucion = num1 % num2
    print(f"El resto de dividir {num1} entre {num2} es {solucion}")
else:
    print("signo no valido")