import random


def create_individual_gene_test():
    gene = list()
    for i in range(16):  # 基因链长度
        gene.append(random.randint(0,6))  # 一个碱基对的内容
    return gene