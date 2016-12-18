from .environment import array_test, array_test_sorted
from .gene_expression import express_test
import random


def evaluate_test(gene):  # 评估函数（测试）
    score = 1
    try:
        array = express_test(gene, array_test)  # 基因的表现是将array_test内容改变
    except:
        return (0.2,)
    else:
        for i, j in zip(array_test_sorted, array):
            if i == j:
                score += 1
        return (score,)


from .environment import input_data, commands_calculation
from .gene_expression import express_execute_func_list


def evaluate_calculate(gene):  # 求式子的评估函数
    score = 2
    for _ in range(4):
        input_data.a = random.randint(-20, 20)
        input_data.b = random.randint(-20, 20)
        input_data.c = random.randint(-20, 20)
        # input_data.a = 4
        # input_data.b = 5
        # input_data.c = 6
        d = input_data.a + input_data.b * input_data.c
        result = express_execute_func_list(gene, commands_calculation)
        if not result:
            return (2,)

        if len(result[1]) != 0 and result[1][0] == d:
            score += 2

    return (score,)
