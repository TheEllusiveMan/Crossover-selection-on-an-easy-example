import random
population_size = int(input("Enter population size: "))
number_of_genes = int(input("Enter number of genes: "))


def random_ch_pull(population_size, number_of_genes):
    ch_pull = []

    for i in range(population_size):
        letters = '01'
        rand_ch = ''.join(random.choice(letters) for j in range(number_of_genes))
        ch_pull.append(rand_ch)

    print("Population ch pull", ch_pull)
    return ch_pull


def fitness(ch_pull):
    ch_pull_sum = []
    print("Cur ch pull", ch_pull)
    for ch in ch_pull:
        gene_sum = 0
        for gene in ch:
            gene_sum += int(gene)
        ch_pull_sum.append(gene_sum)

    # print("Ch sum", ch_pull_sum)
    ch_max = max(ch_pull_sum)
    print("Ch pull sum list {0}\nCh max: {1}".format(ch_pull_sum, ch_max))
    return ch_pull_sum


def fitness_check(ch_pull_sum):
    for ch in range(len(ch_pull_sum)):
        if ch_pull_sum[ch] == number_of_genes:
            best_ch = ch_pull_sum[ch]
            return best_ch
        # best_ch = 0
    else:
        print("There is no best ch")


def roulette_crossover(ch_pull, ch_pull_sum):
    fitness_sum = 0
    for ch in range(len(ch_pull_sum)):
        # print(ch, ch_pull_sum[ch])
        fitness_sum += ch_pull_sum[ch]

    print("\nch sum:", fitness_sum)

    p = 0
    wheel_sector_pull = []
    for ch in range(len(ch_pull_sum)):
        ch_p = (ch_pull_sum[ch] / fitness_sum)
        p += ch_p
        v = p.__round__(2) * 100
        wheel_sector_pull.append(v)

        # print("Ch genes sum", ch_pull_sum[ch])
        # print("Ch P", ch_p)
        # print("P", p)
        # print("V sector", v)

    print("Sectors", wheel_sector_pull)

    mating_pull_index = []
    while len(mating_pull_index) != 8:
        random_chance = random.randrange(0, 100)
        # print("random_chance", random_chance)
        for sector in range(len(wheel_sector_pull)):
            if wheel_sector_pull[sector] > random_chance > wheel_sector_pull[sector-1]:
                # print(wheel_sector_pull[sector])
                mating_pull_index.append(sector)

    print("\nMating pull indexes", mating_pull_index)

    mating_pull = []
    for mating_index in range(len(mating_pull_index)):
        index = mating_pull_index[mating_index]
        mating_pull.append(ch_pull[index])
        # print(mating_pull_index[mating_index])

    print("Mating pull", mating_pull)

    ch_pull.clear()
    for mate in range(0, len(mating_pull), 2):
        # print("Mate", mating_pull[mate])
        genes_1 = mating_pull[mate]
        genes_2 = mating_pull[mate+1]
        # print("Genes", genes_1, genes_2)
        crossover_point = random.randrange(1, number_of_genes - 1)
        # print("crossover_point", crossover_point)

        child_1 = genes_1[:crossover_point] + genes_2[crossover_point:]
        child_2 = genes_1[crossover_point:] + genes_2[:crossover_point]
        ch_pull.append(child_1)
        ch_pull.append(child_2)
        # print("Childs", child_1, child_2)
    print("New ch pull", ch_pull)
    return ch_pull


ch_pull = random_ch_pull(population_size, number_of_genes)
epoch = 1
best_ch = 0

while best_ch != number_of_genes:
    ch_pull_sum = fitness(ch_pull)
    best_ch = fitness_check(ch_pull_sum)
    if best_ch == number_of_genes:
        print("\nFound best chromosome.\nCh pull {0}\nEpoch: {1}".format(ch_pull, epoch))
        break
    # print("Best ch", best_ch)
    roulette_crossover(ch_pull, ch_pull_sum)
    print("Epoch:", epoch)
    epoch += 1
    print("\n-------------------------------------------------------------------------------------------------------\n")
