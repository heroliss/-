import random
from GA_Core.GA_config import GAConfig
from deap import base, creator
from time import clock  # 测试用
from ecology.gene_expression import express_test
from ecology.environment import array_test_sorted, array_test


class GA:
    def __init__(self, ga_config: GAConfig):
        self.config = ga_config
        creator.create("Fitness", base.Fitness, weights=self.config.weights)
        creator.create("Individual", list, fitness=creator.Fitness)
        self.pop = list()
        self.population_init()

    def create_individual(self):
        # 根据基因生成函数创建个体
        ind = creator.Individual(self.config.func_create_individual_gene())
        return ind

    def population_init(self):
        # 初始化种群(灾变)
        self.pop.clear()
        self.population_expand(self.config.pop_size)

    def population_expand(self, count):
        # 扩张种群
        for i in range(count):
            individual = self.create_individual()
            individual.fitness.values = self.config.func_evaluate(individual)
            self.pop.append(individual)

    def generate(self):
        # 产生后代

        offspring = self.config.func_select(self.pop)  # 选择优良个体后代

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < self.config.p_cross:
                # 基因交叉
                self.config.func_cross(child1, child2)
                # 删除旧的适应度
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < self.config.p_mutate:
                # 突变
                self.config.func_mutate(mutant)
                del mutant.fitness.values

        # 为交叉变异和突变后代重新估价
        for ind in offspring:
            if not ind.fitness.valid:
                ind.fitness.values = self.config.func_evaluate(ind)

        # 后代种群替换当前种群
        self.pop = offspring
