
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




    
    