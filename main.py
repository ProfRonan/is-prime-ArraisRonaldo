

a = int(input("Digite um número: "))

is_primo = True

if a <=0:
    print("Número inválido")

else:

  for i in range(2,a):

    
      if a % i == 0:
        is_primo = False
        break


if is_primo == True and a != 2 and a != 1:
        print("Primo")
else:
        print("Não primo")
        
