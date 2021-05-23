## Declarando Variaveis 2

a = 5
b = "doodoo"
c = 1.3

print(type(a))
print(type(b))
print(type(c))
print(type(10 > 5))

## Declarando Variaveis 2.1

    #a) Lista

classe = ['healer', 'warrior', 'druid', 'assassin', 'mage']
print(type(classe))

    ##b) Conjunto

idades = {62,58,27,34,12}
print(type(idades))

    #c)  Dicionario

dicionario = {
   'hello':'ola',
   'food':'comida', 
   'hour':'hora', 
   'time':'tempo'}
print(type(dicionario))

    #d)  Tupla

comidas = ('pizza','lasanha','hamburguer', 'pepeka')
print(type(comidas))


## Fluxo de Controle

    #a)  if

a = 27
b = 12
c = 38
d = 20
    
if a > b:
    print('ta certo isso ae')

    #b)  elif


if a < b:
    print('ta errado isso aê')
elif a > b:
    print('ai ta certo.')


   #c)  else


if a > b:
    print('a é maior que b')
else:
    print('oxi')


## Loops e iterações

    #d)

palavras = ['ameba', 'snow cabeção', 'rafa careca', 'rodrigo smilinguido', 'portugues viado', 'breno gostosao']
for x in palavras:
    print(x)

    #e)

...

    #f)

a = 25
while a < 30:
    print(a)
    a += 25

    #g)

idades = [1,2,3,4,5,6,7,8,9,10]
for x in range(10):
    print(idades)

    #h)

for x in range(12):
  if x == 9: break
  print(x)
else:
  print("Parei")


## Funções

    #i)

def my_function(gays):
  print(gays + 'é gay')

my_function('Rodrigo')
my_function('Tiago')
my_function('Snow')
my_function('Snake')

    #j)

def my_function(x):
  return 30 * x

print(my_function(5))
print(my_function(2))
print(my_function(7))

    #k)

def my_function(e, deus):
  print(e + " " + deus)

my_function("Raul", "Não sabe programar")