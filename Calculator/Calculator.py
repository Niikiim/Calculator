##CALCULATOR

exit = 0

while exit.lower != "sim":

    
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))

    operator = input("Qual operação deseja fazer?\n Multiplicação (*)\n Divisão (/)\n Soma (+)\n Subtração(-)\n Potência (^)\n Módulo (%)\n")


    if operator == "*":

        result = num1 * num2

        
    elif operator == "/":

        if num2 != 0:
        
            result = num1 / num2 

    
        else: 

            result = "Erro!\n Impossivel executar divisão por 0!"
            
        
    elif operator == "+":

        result = num1 + num2


    elif operator == "-":

        result = num1 - num2

    elif operator == "^":

        result = num1 - num2
    
    elif operator == "%":
        
        result = num1 % num2


    print(result)
    exit = input("Deseja sair?\n")
