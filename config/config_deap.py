"""加载deap中的函数"""
import random
from deap import base, tools, creator
from GA_Core.GA_config import GAConfig
from ecology import mutate
from ecology.evaluate import evaluate_test
from ecology.environment import array_test
from GA_Algorithm import select


# 初始化deap函数
toolbox = base.Toolbox()
creator.create("Individual",list)
toolbox.register("attribute", random.randint, 0, len(array_test)-1+5)
toolbox.register("individual", tools.initRepeat,
                 creator.Individual,
                 toolbox.attribute,
                 n = len(array_test)*2)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutate.mutate_test)
toolbox.register("select", tools.selTournament, k=100, tournsize=10)  # 此处k为种群大小
#toolbox.register("select", select.select_roulette_algorithm)
toolbox.register("evaluate", evaluate_test)

config = GAConfig()

#设置函数
config.func_cross = toolbox.mate
config.func_mutate = toolbox.mutate
config.func_select = toolbox.select
config.func_evaluate = toolbox.evaluate
config.func_create_individual_gene = toolbox.individual

#设置变量
config.p_mutate = 0.1 # 突变率
config.p_cross = 0.5  # 交叉率
config.pop_size = 100  # 种群大小



