#TESTE WHILE 

tries = 0

while tries < 3:

    try:
        
        x = int(input("Digite o valor inicial:"))
        max = int(input("Digite o máximo:"))

        
        while x < max+1:
            print(x)
            x += 1

        break
        
    except ValueError:

        print("Digite um valor válido:")
        tries += 1
    



    


