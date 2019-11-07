matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def compara(a):
    if  a == "A": 
        return 0
    if  a == "B": 
        return 1  
    if  a == "C": 
        return 2
    if  a == "D": 
        return 3  
    if  a == "E": 
        return 4
    if  a == "F": 
        return 5  
    if  a == "G": 
        return 6
    if  a == "H": 
        return 7  
    if  a == "I": 
        return 8
    if  a == "J": 
        return 9 
    if  a == "K": 
        return 10 
    if  a == "L": 
        return 11 
    return -1   

def reverter(b):
    if  b == 0: 
        return "A"
    if  b == 1: 
        return "B"
    if  b == 2: 
        return "C"
    if  b == 3: 
        return "D"
    if  b == 4: 
        return "E"
    if  b == 5: 
        return "F"
    if  b == 6: 
        return "G"
    if  b == 7: 
        return "H"
    if  b == 8: 
        return "I"
    if  b == 9: 
        return "J"
    if  b == 10: 
        return "K"
    if  b == 11: 
        return "L"

#ler vetor
heu = open("heuristica.txt","r")

for linha in heu:
    heuristica = linha.split()
    #print('heu ', heuristica[0], heuristica[1])
    vetor[compara(heuristica[0])] = heuristica[1]     

heu.close()

#ler matriz
gra = open("grafo.txt","r")

for linha in gra:
    valores = linha.split()
    #print('grafo ', valores[0], valores[1], valores[2])
    matriz[compara(valores[0])][compara(valores[1])] = valores[2]
    matriz[compara(valores[1])][compara(valores[0])] = valores[2]

gra.close()

#######################################################################

#iniciar rotinas

caminho = []
custo = 0
trajeto = 0

def busca(k):

    i = 0
    uck = 0

    while i < len(caminho) :
        if k == caminho[i] :
            uck = uck+1
        i = i+1

    return uck

begin = str(input('Digite o estado inicial: '))
end = str(input('Digite o estado final: '))

caminho.append(begin)

while begin != end :

    temp = int(compara(begin))

    menor = 900

    op = 0

    while op < 12:

        guard = busca(reverter(op))

        if guard > 0 :
            op = op + 1
            continue

        if int(matriz[temp][op]) != 0 :

            teste = int(matriz[temp][op]) + int(vetor[op])
            
            if menor > teste :

                menor = teste

                trajeto = trajeto + int(matriz[temp][op])

                begin = str(reverter(op))

        op = op + 1

    temp = int(compara(begin))

    caminho.append(begin)
    custo = custo + int(vetor[temp])

    
print(caminho, "\ncusto: heuristica", custo, "\ncusto: trajeto", trajeto)