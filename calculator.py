#Ddesconto não pode ser maior que 100%
#Desconto não pode ser menor que 0%
#Desconto não pode ser maior que 100 reais
#Qual o valor do desconto maximo ?

price = float(input("Digite o preço: \n"))
desc = float(input("Qual o desconto a ser aplicado:\n"))


def desconto (desc,price):
    for sair != "sair":
        

    if desc >= 10 or desc <0:
  
        desc = (desc/100)*price
        result = price - desc
        print(f"O valor do desconto é {result}")

    else:
        print("O desconto não pode ser maior que 100%")
