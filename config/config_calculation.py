"""求算式"""
from GA_Core.GA_config import GAConfig
from ecology import create_individual, \
    environment, evaluate, gene_expression, mutate
from GA_Algorithm import cross, select

config = GAConfig()  # 求算式的配置文件

config.func_create_individual_gene = create_individual.create_individual_gene_calculation
config.func_cross = cross.cx_two_point
config.func_mutate = mutate.mutate_calculation
config.func_evaluate = evaluate.evaluate_calculate
config.func_select = select.select_roulette_algorithm

config.p_mutate = 0.1
config.p_cross = 0.5
config.pop_size = 100
