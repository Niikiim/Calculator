
def soma (*numeros):
    return sum(numeros)

def subtracao (*numeros):
    
    total = 0

    for i in numeros:
        total += i
    
    return total

def multplicar (*numeros):

    total = 1

    for i in numeros:
        total *= i

    return total

def divisao (numero, divisor):

    return numero / divisor


operacao = input("Qual operação deseja executar:\n Multiplicar (1) \n Dividir(2) \n Somar(3) \n Subtrair(4) \n")

if operacao == "1":
    quantidade_numeros = int(input("Digite quantos numeros deseja multiplicar:"))
    lista_numeros = []
    for i in range(quantidade_numeros):
        numeros = int(input(f"Digite o {i+1}º numero:"))
        lista_numeros.append(numeros)

    print(multplicar(*lista_numeros))

elif operacao == "2":
    numero = int(input("Digite o numero que deseja dividir:"))
    divisor = int(input("Digite o divisor: "))
    
    print(divisao(numero,divisor))

elif operacao == "3":
    lista_numeros=[]
    contador = 0

    while True:
        numero = input(f"Digite o {contador+1}º numero (ou 'sair'): ")

        if numero.strip().lower() == "sair":
            break
        
        try:
            numero = float(numero)
            contador +=1
        except:
            print("Valor inválido, tente novamente.")
            continue
        
        lista_numeros.append(numero)

    print(soma(*lista_numeros))

elif operacao == "4":
    lista_numeros = []
    contador = 0

    while True:
        numero = input(f"Digite o {contador+1}º numero (ou sair): ")

        if numero.strip().lower() == "sair":
            break

        try:
            numero = float(numero)
            contador += 1
        except:
            print("Valor inválido, tente novamente.")

        lista_numeros.append(numero)

    print(subtracao(*lista_numeros))
