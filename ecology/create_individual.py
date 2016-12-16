import random
from .environment import array_test


def create_individual_gene_test():  # 产生个体基因
    gene = list()
    for i in range(len(array_test) * 2):  # 基因链长度
        gene.append(random.randint(0, len(array_test) - 1 + 5))  # 一个碱基对的内容
        # (此处的+5是故意产生越界索引来产生无法基因表达的个体)
    return gene
