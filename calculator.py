#Ddesconto não pode ser maior que 100%
#Desconto não pode ser menor que 0%
#Desconto não pode ser maior que 100 reais
#Qual o valor do desconto maximo 

price = float(input("Digite o preço: \n"))
desc = float(input("Qual o desconto a ser aplicado:\n"))


descporcentagem = (desc/100)
valordesc = descporcentagem * price
result = price - descporcentagem

if desc <= 10 and desc > 0 and valordesc<100:
  
    desc = (desc/100)*price
    result = price - desc
    print(f"O valor do desconto é {result}")
    
elif desc > 10:
    print("Desconto não pode ser maior que 10%!")

elif desc < 0:
    print("O desconto não pode ser menor que 0%!")

elif valordesc > 100:
    print("O desconto não pode ser maior que 100 reais!")

    if price < 1000:
        descmaximo = float(0.1*price)
        print(f"O desconto maximo será de: {descmaximo} reais")
    else:
        descmaximo = "99,99"
        print(f"O desconto maximo é de: {descmaximo} reais")

else:
    print("ERRO!")

