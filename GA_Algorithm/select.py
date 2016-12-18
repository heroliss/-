import random
import copy
from operator import attrgetter


def select_roulette_algorithm(pop):  # 单权重的轮盘赌选择法
    inds = sorted(pop, key=attrgetter("fitness"), reverse=True)
    fitness_sum = sum(individual.fitness.values[0] for individual in inds)

    pop_new = list()
    for i in range(len(inds)):
        dice = random.random() * fitness_sum  # 骰子
        for individual in inds:
            dice -= individual.fitness.values[0]
            if dice < 0:
                pop_new.append(copy.deepcopy(individual))  # 此处需深度拷贝个体！！
                break
    return pop_new
