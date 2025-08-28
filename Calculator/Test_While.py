#TESTE WHILE 

tries = 0

try:

    try:
        
        x = int(input("Digite o valor inicial:"))
        max = int(input("Digite o máximo:"))

        while x < max+1:
            print(x)
            x += 1
    
    
    except ValueError:

        print("Digite um valor válido:")

except tries !=3:

    tries += tries


    


