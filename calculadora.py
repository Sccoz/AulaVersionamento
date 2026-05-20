print("================================")
print("Bem vindo a super calculador !!")
 
print("================================")

while True:
    print("Você vai ter algumas escolhas a seguir:") 
    print("1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Exponenciacao\n6 - Calc Porcent \n0 - Sair")
    escolha = int(input("\nDigite a opção: "))

    if escolha == 0:
        print("Saindo... Até logo!")
        break

    n1 = float(input("Digite o número 1: "))
    n2 = float(input("Digite o número 2: "))

    match escolha:
        case 1:
            resultado = n1 + n2
        case 2:
            resultado = n1 - n2
        case 3:
            if n2 != 0 :
                resultado = n1 / n2
            else :
                print("Impossivel o denomiandor ser 0 !!!")
        case 4:
            resultado = n1 * n2
        case 5 :
            resultado = n1 ** n2
        case 6 :
            resultado = n1 * (n2 /100)
        case _:  
            resultado = "Operação inválida"

    print(f"\nA resposta para sua operação é: {resultado}")
    print("=======================================\n\n")