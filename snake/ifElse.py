idade = int(input("Insira sua idade: "))

if(idade >= 0 and idade <= 3):
    print("Você é recém-nascido.")
elif(idade > 3 and idade <= 12):
    print("Você é uma criança.")
elif(idade > 12 and idade <= 18):
    print("Você é adolescente.")
elif(idade > 18 and idade < 65):
    print("Você é adulto.")
elif(idade >= 65 and idade < 120):
    print("Você é idoso.")
else:
    print("Idade inválida.")