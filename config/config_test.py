"""加载自定义函数"""
from GA_Algorithm import cross, select
from GA_Core.GA_config import GAConfig
from ecology import evaluate, create_individual, mutate

config = GAConfig()  # 建立一个配置对象

# 设置函数
config.func_cross = cross.cx_two_point  # 交叉函数
config.func_evaluate = evaluate.evaluate_test  # 估价函数
config.func_mutate = mutate.mutate_test  # 突变函数
config.func_select = select.select_roulette_algorithm  # 选择函数
config.func_create_individual_gene = \
    create_individual.create_individual_gene_test  # 创建个体函数

# 设置变量
config.p_mutate = 0.1 # 突变率
config.p_cross = 0.5  # 交叉率
config.pop_size = 100  # 种群大小
