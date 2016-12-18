import random


def mutate_test(gene):  # 个体突变
    gene[random.randint(0, len(gene) - 1)] = \
        random.randint(0, 8)


from .environment import commands_calculation


def mutate_calculation(gene):  # 求式子的突变函数
    gene[random.randint(0, len(gene) - 1)] = \
        random.randint(0, len(commands_calculation) - 1)
