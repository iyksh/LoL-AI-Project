def read_and_convert_txt_file(filename):
    try:
        file = open(filename)
    except:
        print("Error Opening file")
    text = []
    for i in file:
        text.append(i)

    text = ''.join(text)
    splitedOnce = text.split('\n')

    championListNoRepeat = []

    caracteristicsHash = {} ## Chave é caracteristica, e os dados que serão guardados é uma lista de campeões

    championHash = {} ## Chave é o campeão, e os dados que serão guardados é uma lista de caracteristicas

    for i in splitedOnce:
        splitedTwice = i.split(':')
        
        championList = splitedTwice[1].split(',')
        print(championList)
        for i in championList:
            if i in championHash.keys():
                championHash[i].append(splitedTwice[0])
            else:
                championHash[i] = []
                championHash[i].append(splitedTwice[0])
                
            if i not in championListNoRepeat:
                championListNoRepeat.append(i)
        caracteristicsHash[splitedTwice[0]] = championList
        




