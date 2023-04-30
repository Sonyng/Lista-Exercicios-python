#EXERCICIO 1-------------------------------------------------------------------------------
print("Olá ETE PORTO DIGITAL!")


#EXERCICIO 2-------------------------------------------------------------------------------
numero = int 
numero = input('Digite um número: ')
print("O numero informado foi: ",numero)



#EXERCICIO 3-------------------------------------------------------------------------------
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma é", soma)



#EXERCICIO 4-------------------------------------------------------------------------------
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média final é", media)




#EXERCICIO 5-------------------------------------------------------------------------------
metros = float(input("Digite a medida em metros: "))
centimetros = metros * 100
print("A medida em centímetros é", centimetros)




#EXERCICIO 6-------------------------------------------------------------------------------
import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio**2
print("A área do círculo é", area)



#EXERCICIO 7-------------------------------------------------------------------------------
lado = float(input("Digite o valor do lado do quadrado: "))
area = lado**2
dobro_area = 2 * area
print("O dobro da área do quadrado é", dobro_area)



#EXERCICIO 8-------------------------------------------------------------------------------
valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
salario = valor_hora * horas_trabalhadas
print("Seu salário neste mês é de R$", salario)



#EXERCICIO 9-------------------------------------------------------------------------------
valor = float(input("Digite um valor: "))
if valor > 0:
    print("O valor é positivo")
elif valor < 0:
    print("O valor é negativo")
else:
    print("O valor é zero")


    

#EXERCICIO 10-------------------------------------------------------------------------------
sexo = input("Digite F para feminino ou M para masculino: ")
if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo inválido")
