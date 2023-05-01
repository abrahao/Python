 
alfabeto = {
"A": "A",
"E": "E",
"I": "I",
"O": "O",
"U": "U"
 }
 
entrada = [(i) for i in input().split()]

listEntrada = list(entrada)
saidaList = []

for i in listEntrada:
    saidaList += alfabeto[i]

print(listEntrada)