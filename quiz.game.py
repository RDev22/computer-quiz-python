print("Bem-vindo ao meu Quiz")

playing = input("Você quer jogar? ")

if playing.lower() != "sim":
    quit()

print("Ok! Vamos jogar :)")
score = 0

answer = input("Qual é a letra que antecede a letra S no alfabeto brasileiro? ")
if answer.lower() == "R":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("O cantor britânico Fred Mercury pertenceu a qual banda de rock? ")
if answer.lower() == "queen":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("Qual cidade brasileira é conhecida como a terra da garoa? ")
if answer.lower() == "são paulo":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("Qual é a sigla do estado de Minas Gerais? ")
if answer.lower() == "mg":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("Qual o nome da capital da Inglaterra? ")
if answer.lower() == "londres":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

print("Você tem " + str(score) + "pontos!")
print("Você tem " + str((score / 4) * 100) + "%.")