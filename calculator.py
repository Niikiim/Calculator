#Ddesconto não pode ser maior que 10%
#Desconto não pode ser menor que 0%
#Desconto não pode ser maior que 100 reais
#Qual o valor do desconto maximo ?

def desconto (desc,price):

    try:
        price = float(price)
        desc = float(desc)
        
    except(ValueError,TypeError):
        return "Erro!\n Insira os valores numéricos válidos!"

    desc = (desc/100)
    desc_amount = desc * price
    result = price - desc
        
    if  0 <= desc <= 10 and desc_amount <= 100:
  
        return(f"O valor do desconto é {result}")

    elif desc > 10:

        return("O desconto não pode ser maior que 10%")
    
    elif desc < 0: 
         
        return("O desconto não pode ser menor que 0!")
    
    elif result > 100:
        
        desc_max = (100/price)*100

        return("O desconto não pode ser maior que 100 reais!\n" f"O desconto máximo será de {desc_max}")


    

