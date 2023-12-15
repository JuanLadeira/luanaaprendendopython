def script(nome=None, pergunta_2=None):
    if nome != None:
        nome = nome
    if pergunta_2 != None:
        pergunta_2 = pergunta_2
    else:
        nome = input("Qual o seu nome? ")
        pergunta_2 = input("Como você está se sentindo? ")
    try:
        pergunta_3 = int(input("De 0 a 10? "))
    except ValueError:
        print("Você não digitou um número, tente novamente")
        script(nome=nome, pergunta_2=pergunta_2)
script()