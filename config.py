import random
from GA_Core.GA_config import GAConfig
from GA_Algorithm import cross, evaluate, \
    create_individual, mutate, select

config = GAConfig  # 建立一个配置对象

# 设置函数
config.cross = cross.cxTwoPoint  # 交叉函数
config.evaluate = evaluate.evaluate_test  # 估价函数
config.mutate = mutate.mutate_test  # 突变函数
config.select = select.select_roulette_algorithm  # 选择函数
config.create_individual_gene = \
    create_individual.create_individual_gene_test  # 创建个体函数

# 设置变量
config.p_mutate = 0.01 # 突变率
config.p_cross = 0.7  # 交叉率
config.pop_size = 100  # 种群大小
