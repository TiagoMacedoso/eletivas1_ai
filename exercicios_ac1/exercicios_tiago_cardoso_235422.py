def somar_2_numeros():
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    print("\n\nA soma dos dois números é: ", str(num1+num2))
    
    return

def impar_ou_par():
    num = int(input("Insira um número inteiro: "))
    
    if (num%2 == 0): print("\n\nO número é PAR")
    else: print("\n\nO número é IMPAR")
    
    return       

def maior_de_3_numeros():
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    num3 = float(input("Insira o terceiro número: "))
    
    if (num1 > num2 and num1 > num3): print("\n\nO PRIMEIRO número é o MAIOR!")
    elif (num2 > num1 and num2 > num3): print("\n\nO SEGUNDO número é o MAIOR!")
    else: print("\n\nO TERCEIRO número é o MAIOR!")
    
    return
    
def contar_1_a_10():
    for i in range(11):
        if (i==0):
            pass
        else:
            print(i)
        
def tabuada():
    num = float(input("Insira o número inteiro para receber a tabuada do mesmo: "))
    
    for i in range(11):
        print(str(num) + " * " + str(i) + " = " + str(i*num))
        
def maior_idade():
    idade = int(input("Informe sua idade: "))
    
    if (idade >= 18): print("\nVocê é MAIOR de idade")
    else: print("\nVocê é MENOR de idade")

def somar_pares_de_0_a_X():
    num = int(input("Insira o número inteiro até o qual deseja somar os pares: "))
    
    soma = 0
    
    for i in range(num+1):
        if (i%2 == 0): soma += i
        
    print("\nA soma dos pares até o " + str(num) + " é " + str(soma))

parar = False

while parar == False:
    opcao = int(input("\n\n1 - Soma de dois números\n2 - Par ou ímpar\n3 - Maior entre 3 números\n4 - Contagem de 1 a 10\n5 - Tabuada de um número\n6 - Verificação de idade\n7 - Soma dos pares de 0 à algum número\n0 - para encerrar\nEscolha uma das opções com o número correspondente: "))
    
    if (opcao == 1): somar_2_numeros()
    elif (opcao == 2): impar_ou_par()
    elif (opcao == 3): maior_de_3_numeros()
    elif (opcao == 4): contar_1_a_10()
    elif (opcao == 5): tabuada()
    elif (opcao == 6): maior_idade()
    elif (opcao == 7): somar_pares_de_0_a_X()
    elif (opcao == 0): parar = True