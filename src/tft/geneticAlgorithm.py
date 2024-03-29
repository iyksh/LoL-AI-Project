import random
import matplotlib.pyplot as plt
import networkx as nx

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
        for i in championList:
            if i in championHash.keys():
                championHash[i].append(splitedTwice[0])
            else:
                championHash[i] = []
                championHash[i].append(splitedTwice[0])
                
            if i not in championListNoRepeat:
                championListNoRepeat.append(i)
        caracteristicsHash[splitedTwice[0]] = championList
    
    return  caracteristicsHash, championHash 


def create_chromosome(classes, numChamps):
    chromosome = []
    selected_genes = set()

    for i in range(numChamps):
        rand = random.randint(0, len(classes) - 10)
        gene = classes[rand]

        if gene not in selected_genes:
            selected_genes.add(gene)
            chromosome.append(gene)
    return chromosome


def create_population(rangePop, classes, rangeNumChampions):
   population = [create_chromosome(classes,rangeNumChampions) for i in range(rangePop)]
   return population


def fitness_chromosome(chromosome, championHash):
   fitness = 0
   classesList = []
   for i in range(len(chromosome)):
       classesList.extend(championHash.get(chromosome[i]))
    
   for j in range(len(classesList)-1):
       for k in range(len(classesList)-1):
        if classesList[j] == classesList[k] and j != k :
            fitness += 10
       
   
   #print(chromosome, fitness)
   return fitness

def fitness_population(population, championHash):
   fitness = []
   for i in range(len(population)):
        fitness.append(fitness_chromosome(population[i], championHash))

   return fitness

def bestTeam(fitness_vec, population):
   best_fitness = fitness_vec[0]
   worst_fitness = best_fitness
   worst_chromosome = population[0]
   melhor_cromossomo = population[0]

   for i in range(len(fitness_vec)):
      if fitness_vec[i] > best_fitness:
          best_fitness = fitness_vec[i]
          melhor_cromossomo = population[i]

      if fitness_vec[i] < worst_fitness:
          worst_fitness = fitness_vec[i]
          worst_chromosome = population[i]

   return best_fitness, melhor_cromossomo, worst_fitness, worst_chromosome 

def torneio(populacao, tamanho_da_luta, championHash):
    populacao_final = []
    lutadores = []
    
    k = 0.6
    for i in range(len(populacao)):
      for j in range(tamanho_da_luta):
          lutadores.append(random.choice(populacao))
      r = random.random()
      fitness = fitness_population(lutadores,championHash)
      
      melhor_fitness, melhor_cromossomo, pior_fitness, pior_cromossomo = bestTeam(fitness,lutadores)

      if r < k:
          populacao_final.append(melhor_cromossomo)
      else:
          populacao_final.append(pior_cromossomo)

    return populacao_final
    
def create_graph(class_vector, characteristics_dict):
    # Create a directed graph
    graph = nx.DiGraph()

    # Add nodes to the graph based on the class_vector
    graph.add_nodes_from(class_vector)

    # Iterate through the class_vector
    for current_class in class_vector:
        if current_class in characteristics_dict:
            current_characteristics = characteristics_dict[current_class]

            for characteristic in current_characteristics:
                for other_class in class_vector:
                    if current_class != other_class and characteristics_dict.get(other_class) and characteristic in characteristics_dict[other_class]:
                        # Add a directed edge from the current class to the other class
                        graph.add_edge(current_class, other_class)

    # Visualize the graph
    nx.draw(graph, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_color='black')
    plt.show()

def algorithm(filePath, populationRange, teamSize, gerationsNum,tournamentRange, minimumFitness):
    print(f"Running Genetic Algorithm: Fitness: {minimumFitness}")
    x,championHash = read_and_convert_txt_file(filePath)
    championsList = list(championHash.keys())
    population = create_population(populationRange, championsList, teamSize)
    fitnessVec = fitness_population(population, championHash)
    best_fitness, melhor_cromossomo, worst_fitness, worst_chromosome  = bestTeam(fitnessVec, population)
    bestGlobal_vec = []
    bestGlobal_vec.append(best_fitness)

    for i in range(gerationsNum):
       population = torneio(population, tournamentRange,championHash)
       fitnessVec = fitness_population(population,championHash)

       best_fitness, melhor_cromossomo, worst_fitness, worst_chromosome  = bestTeam(fitnessVec, population)
       bestGlobal_vec.append(best_fitness)
       
    if best_fitness < minimumFitness:
        print(f"Fitness < {minimumFitness}")
        melhor_cromossomo, best_fitness, championHash = algorithm(filePath, populationRange, teamSize, gerationsNum,tournamentRange,minimumFitness)
        

    else:

        create_graph(melhor_cromossomo, championHash)
        return melhor_cromossomo, best_fitness, championHash