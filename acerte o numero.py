import random
#import numpy as np

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randint(1,20)
print (numero_secreto)

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo")
