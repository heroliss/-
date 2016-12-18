import random
from .environment import array_test


def create_individual_gene_test():  # 产生个体基因
    gene = list()
    for i in range(len(array_test) * 2):  # 基因链长度
        gene.append(random.randint(0, len(array_test) - 1 + 5))  # 一个碱基对的内容
        # (此处的+5是故意产生越界索引来产生无法基因表达的个体)
    return gene


from .environment import commands_calculation


def create_individual_gene_calculation():  # 产生 求计算公式的基因
    return [random.randint(0, len(commands_calculation) - 1) for _ in range(6)]
