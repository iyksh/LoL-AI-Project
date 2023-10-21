from headerTFT import *
import random

def create_chromosome(classes, numChamps):
    chromosome = ()
    selected_genes = set()

    for i in range(numChamps):
        rand = random.randint(0, len(classes) - 10)
        gene = classes[rand][1]

        if gene not in selected_genes:
            selected_genes.add(gene)
            chromosome += (classes[rand],)

    return chromosome


def create_population(rangePop, classes, rangeNumChampions):
   population = [create_chromosome(classes,rangeNumChampions) for i in range(rangePop)]
   return population

def fitness_chromosome(chromosome):
   fitness = 0
   for i in range(len(chromosome)):
    for j in range(len(chromosome)):
       if chromosome[i][0] == chromosome[j][0] and chromosome[i][1] != chromosome[j][1]:
          #print(f" {chromosome[i][0]}: {chromosome[i][1]} is good with {chromosome[i][0]}: {chromosome[j][1]}")
          fitness += 10
    
    #if fitness > 10:
       #print(f"The array {chromosome}, maybe is a good team. fitness: {fitness}")

    return fitness
    

def fitness_population(population):
   fitness = [fitness_chromosome(population[i]) for i in range(len(population))] #repeat the process for n population
   return fitness


def pmx_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))
    offspring1 = [None] * len(parent1)
    offspring2 = [None] * len(parent2)
    offspring1[point1:point2 + 1] = parent1[point1:point2 + 1]
    offspring2[point1:point2 + 1] = parent2[point1:point2 + 1]

    for i in range(len(parent1)):
        if point1 <= i <= point2:
            continue 
        else:
            mapping = parent2[i]
            while mapping in offspring1[point1:point2 + 1]:
                index = parent1.index(mapping)
                mapping = parent2[index]
            offspring1[i] = mapping

            mapping = parent1[i]
            while mapping in offspring2[point1:point2 + 1]:
                index = parent2.index(mapping)
                mapping = parent1[index]
            offspring2[i] = mapping

    return offspring1, offspring2

def crossover(population):
   new_chromosomes = []
   for i in range(0, len(population)-1, 2):
        crossover_chance = random.randint(1,10) #repete o processo de pmx para todos os filhos-1
        if crossover_chance > 2:
            filho1, filho2 = pmx_crossover(population[i], population[i+1])
            new_chromosomes.append(filho1)
            new_chromosomes.append(filho2)
        else:
         filho1, filho2 = population[i], population[i+1]
         new_chromosomes.append(filho1)
         new_chromosomes.append(filho2)
   
   return new_chromosomes

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


def torneio(populacao, tamanho_da_luta):
    populacao_final = []
    lutadores = []
    
    k = 0.6
    for i in range(len(populacao)):
      for j in range(tamanho_da_luta):
          lutadores.append(random.choice(populacao))
      r = random.random()  # valor entre 0 e 1
      fitness = fitness_population(lutadores)
      
      melhor_fitness, melhor_cromossomo, pior_fitness, pior_cromossomo = bestTeam(fitness,lutadores)

      if r < k:
          populacao_final.append(melhor_cromossomo)
      else:
          populacao_final.append(pior_cromossomo)

    return populacao_final


def geneticAlgortimh(filePath, populationRange, teamSize, gerationsNum,tournamentRange):
    class_tuples = read_and_convert_txt_file(filePath)
    population = create_population(populationRange,class_tuples,teamSize)
    fitness = fitness_population(population)
    best_fitness_global, bestTeam_global, worst_fitness, worst_chromosome = bestTeam(fitness, population)

    


    bestGlobal_vec = []
    bestGlobal_vec.append(best_fitness_global)

    for i in range(gerationsNum):
       population = torneio(population, tournamentRange)
       fitness = fitness_population(population)

       best_fitness_global, bestTeam_global, worst_fitness, worst_chromosome = bestTeam(fitness, population)

    print(best_fitness_global, bestTeam_global)

filename = 'src/tft/champions.txt'
geneticAlgortimh(filename,100,4,30,5)



