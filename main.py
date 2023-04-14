import sys

a = int(input("Digite um número: "))

is_primo = True

if a <=0:
    print("Número inválido")
    sys.exit()
else:

  for i in range(2,a):

    
      if a % i == 0:
        is_primo = False
        break


if is_primo == True:
        print("Primo")
else:
        print("Não primo")
        
