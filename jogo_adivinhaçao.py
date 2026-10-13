import random 

numero_secreto = random.randint(1,100)
palpite = int (input("adivinhe o numero de 1 a 100 (apenas uma chance)"))


if palpite == numero_secreto:
    print("Voce acertou!")
else:
    print(f"Errou! burro do caramba kkk O número era {numero_secreto}")    
