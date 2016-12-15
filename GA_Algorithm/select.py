import random


def select_roulette_algorithm(pop):  # 轮盘赌选择法
    fitness_sum = 0
    individual = None
    for individual in pop:
        fitness_sum += individual.fitness

    pop_new = list()
    for i in range(len(pop)):
        dice = random.random() * fitness_sum  # 骰子
        for individual in pop:
            dice -= individual.fitness
            if dice < 0:
                pop_new.append(individual.copy())
                break
    return pop_new
