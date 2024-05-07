while True:
    print("Olá, irei realizar cálculos de adição, Vamos Começar =)")

    a = int(input("Qual o primeiro valor: "))
    b = int(input("Qual o segundo valor: "))

    x = (a+b)

    print("O valor da soma é: ", x)

    if x >= 0:
        print("Vamos continuar!")
    else:
        print("Calculadora encerrada! Até a próxima!")
        break