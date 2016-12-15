import random
from GA_Core.GA_config import GAConfig
from GA_Core.GA_individual import Individual
from time import clock  # 测试用


class GA:
    def __init__(self, ga_config: GAConfig):
        self.config = ga_config
        self.pop = list()
        self.population_init()

    def create_individual(self):
        # 根据基因创建函数创建个体
        ind = Individual()
        ind.gene = self.config.create_individual_gene()
        return ind

    def population_init(self):
        # 初始化种群(灾变)
        self.pop.clear()
        self.population_expand(self.config.pop_size)

    def population_expand(self, count):
        # 扩张种群
        for i in range(count):
            individual = self.create_individual()
            individual.fitness = self.config.evaluate(individual.gene)
            self.pop.append(individual)

    def generate(self):
        # 产生后代

        offspring = self.config.select(self.pop)  # 选择优良个体后代

        for child1, child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < self.config.p_cross:
                # 基因交叉
                self.config.cross(child1.gene, child2.gene)
                # 删除旧的适应度
                child1.fitness = None
                child2.fitness = None

        for mutant in offspring:
            if random.random() < self.config.p_mutate:
                # 突变
                self.config.mutate(mutant.gene)
                mutant.fitness = None

        # 为交叉变异和突变后代重新估价
        for ind in offspring:
            if ind.fitness is None:
                ind.fitness = self.config.evaluate(ind.gene)

        # 后代种群替换当前种群
        self.pop[:] = offspring
