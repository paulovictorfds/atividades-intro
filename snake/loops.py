frutas = ("banana", "maça", "uva", "mamão", "abacaxi", "pêra", "melão")

print("Iteração em lista:")
for x in frutas:
    print(x)

print("Iteração em lista usando continue:")
for x in frutas:
    if x == "uva":
        continue
    print(x)

print()
print("Iteração em intervalo numérico:")

for x in range(6):
    print(x)

print("Usando while...")

num = 0
while num < 6:
    print(num)
    num += 1

print("Usando while com break...")

num = 0
while num < 6:
    if num == 4:
        break
    print(num)
    num += 1