alfabeto = {

#---------- 
#Maiusculas
#----------
"A": "A",
"E": "E",
"I": "I",
"O": "O",
"U": "U",

"B": "BAC",
"C": "CAD",
"D": "DEF",
"F": "FEG",
"G": "GIH",
"H": "HIJ",
"J": "JIK",
"K": "KIL",
"L": "LOM",
"M": "MON",
"N": "NOP",
"P": "POQ",
"Q": "QOR",
"R": "ROS",
"S": "SUT",
"T": "TUV",
"V": "VUW",
"W": "WUX",
"X": "XUY",
"Y": "YUZ",
"Z": "ZAB",

#------------- 
# Miniusculas
#-------------
"a": "a",
"e": "e",
"i": "i",
"o": "o",
"u": "u",

"b": "bac",
"c": "cad",
"d": "def",
"f": "feg",
"g": "gih",
"h": "hij",
"j": "jik",
"k": "kil",
"l": "lom",
"m": "mon",
"n": "nop",
"p": "poq",
"q": "qor",
"r": "ros",
"s": "sut",
"t": "tuv",
"v": "vuw",
"w": "wux",
"x": "xuy",
"y": "yuz",
"z": "zab",
" ": " "
}

entrada = input("Palavra: ")

entradaList = []


listEntrada = list(entrada)
saidaList = []

for i in listEntrada:
    saidaList += alfabeto[i]
    
saida = "".join(saidaList)
print("Encriptada: "+saida.lower())
