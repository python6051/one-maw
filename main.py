#条件設定
length = 100    #染色体の長さ
population = 100  #各世代の染色体の数
new_population = 50  #子孫の数
mutation_rate = 0.01  #突然変異する確率
generationcount = 100  #最大世代数

#初期個体群の生成
import random
def production(length,population):
    gene = [[random.randint(0,1) for i in range(length)] for j in range(population)]
    
    return gene

def sum_gene(gene):
    result = []
    for row in gene:
        result.append(sum(row))
    
    return result
#適応度の評価
def evaluation(gene):
    evaluate = []
    result = sum_gene(gene)
    for i in range(population):
        evaluate.append(result[i]/length)
    
    return evaluate

#最小値の探索
def find_min(evaluate):
    min = 5
    for i in range(population):
        if evaluate[i] < min:
            min = evaluate[i]
    return min

#最大値の探索
def find_max(evaluate):
    max = 0
    for i in range(population):
      if evaluate[i] > max:
        max = evaluate[i]
    return max

#親選択
def choice(gene,evaluate):
    father_index = random.randint(0,99)
    mother_index = random.randint(0,99)
    if evaluate[father_index] > evaluate[mother_index]:
        parent = gene[father_index]
    else:
        parent = gene[mother_index]
    return parent

#交叉
def crossover(father,mother):
    offspring = []
    for i in range(length):
        p = random.random()
        if p < 0.5:
            offspring.append(father[i])
        else:
            offspring.append(mother[i])
    return offspring

#突然変異
def mutation(offspring):
    for i in range(population):
        
        p = random.random()
        if p < mutation_rate:
            if offspring[i] == 0:
                offspring[i] = 1
            else:
                offspring[i] = 0
    return offspring
#エリート主義&世代交代
def elite(gene, evaluate, new_gene):
    sort_evaluate = sorted(evaluate, reverse=True)
    gen_tmp = []
    for i in range(int(population/2)):
        index = evaluate.index(sort_evaluate[i])
        gen_tmp.append(gene[index])
    gen_tmp.extend(new_gene)
    return gen_tmp

#いよいよ繁殖を行っていく
def main():
    generationcount = 1
    gene = production(length,population)
    new_gene = []

    while generationcount <= 100:
        new_gene.clear()

        evaluate = evaluation(gene)
        
        min = find_min(evaluate)
        max = find_max(evaluate)

        print("generation: "+ str(generationcount))
        print("MIN: " + str(min))
        print("MAX: " + str(max))
        if min == 100:
            break

        for i in range(new_population):
            father = choice(gene,evaluate)
            mother = choice(gene,evaluate)

            offspring = crossover(father,mother)
            
            offspring = mutation(offspring)
            
            new_gene.append(offspring)

        gene = elite(gene,evaluate,new_gene)
        print(len(gene))
        
        generationcount += 1
        print("---------------------------")

if __name__ == "__main__":
    main()
