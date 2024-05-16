def calculadora():
    
    a = int(input("Valor de a: "))
    
    b = int(input("Valor de b: "))
    
    opcao = input(("Qual será a operação a ser realizada? (+, -, *, /): "))

    if opcao == "+":
        resultado = soma(a, b)
    else:
        if opcao == "-":
            resultado = subtracao(a, b)
        else:
            if opcao == "*":
                resultado = multiplicacao(a, b)
            else:
                if opcao == "/":
                    resultado = divisao(a, b)
                else:
                    print("Opção inválida")

    print("Resultado da operação é: " + str(resultado))

def divisao(x, y):
    ret = float(x) / y
    
    return ret

def multiplicacao(x, y):
    ret = x * y
    
    return ret

def soma(x, y):
    ret = x + y
    
    return ret

def subtracao(x, y):
    ret = x - y
    
    return ret

# Main
continuar = "s"
while continuar == "s":
    calculadora()
    print("Deseja continuar (S/N): ")
    continuar = input()
print("Ok")    
print("Até Mais!")
