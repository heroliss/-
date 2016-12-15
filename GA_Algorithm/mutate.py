import random


def mutate_test(gene):
    gene[random.randint(0,len(gene)-1)] = \
        random.randint(0,6)