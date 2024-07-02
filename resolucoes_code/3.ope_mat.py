# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operation = input("Digite a operação matemática simples a ser realizada (soma, subtração, multiplicação ou divisão): ")

if operation == "soma":
    result = num1 + num2
elif operation == "subtração":
    result = num1 - num2
elif operation == "multiplicação":
    result = num1 * num2
elif operation == "divisão":
    result = num1 / num2
else:
    print("Operação inválida!")
    result = None

if result is not None:
    print("Resultado da operação:", result)
else:
    print("Operação inválida!")