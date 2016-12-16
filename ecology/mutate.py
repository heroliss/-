import random


def mutate_test(gene):  # 个体突变
    gene[random.randint(0, len(gene) - 1)] = \
        random.randint(0, 8)
