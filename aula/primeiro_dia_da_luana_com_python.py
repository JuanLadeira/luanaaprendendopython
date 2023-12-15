#Falamos sobre atribuição de variáveis
luana = "luana"
#O que é uma variável?
#É um espaço na memória do computador que armazena um valor, que pode ser alterado durante a execução do programa
variavel = "variavel"
print(variavel)
variavel = 10
print(variavel)
variavel = 10.5
print(variavel)
#O que é uma constante?
#É um espaço na memória do computador que armazena um valor, que não pode ser alterado durante a execução do programa
meuamor = ("luana",)
#Quais são os tipos de variáveis simples?
#String, int, float, boolean
nome:str = "luana"
idade:int = 25
altura:float = 1.60
casada:bool = False #Quase lá
#O que é uma string, um float e um int?
#String é um texto, float é um número com casas decimais, int é um número inteiro
nome = "luana"
#string tem metodos? quais?
#Sim, tem vários, como upper(), lower(), replace(), split(), etc
print(nome.upper())
print(nome.lower())
print(nome.replace("l", "L"))
print(nome.split("a"))
#O que é um boolean?
#É um tipo de variável que só pode ter dois valores: True ou False
boolean = True or False
#O que é uma lista?
#É um tipo de variável que pode armazenar vários valores, inclusive de tipos diferentes
lista = [1,2,3,4,5,6,7,8,9,10]
#O que é uma tupla?
#É um tipo de variável que pode armazenar vários valores, inclusive de tipos diferentes, mas não pode ser alterada
tupla = (1,2,3,4,5,6,7,8,9,10)

#O que é um dicionário?
dicionario = {
    "nome":"luana",
    "idade":25
    }

#O que é uma função?
def printcadaletra(nome):
    for letra in nome:
        print(letra.upper())
        
printcadaletra(luana)