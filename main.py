
varilla = 600
medidas = []

with open('medidas.csv','r') as archivo:
    file = archivo.read().split('\n')
    for elm in file:
        read = elm.split(',')
        read[0] = float(read[0])
        read[1] = int(read[1])
        for i in range(read[1]):
            medidas.append(read[0])


medidas.sort(reverse=True)

actual = 0
cortes = []

corte = []
acum = 0

for var in range(len(medidas)):
    if acum + medidas[var] <= varilla:
        corte.append(medidas[var])
        acum += medidas[var]
    else:
        acum = 0
        print(corte)
        cortes.append(corte)
        corte = []

for i in cortes:
    suma=0
    for e in i:
        suma += e
    print('suma:', suma,'aprov:',str(round(suma*100/600,2))+'%', 'piezas:', i)
    
    