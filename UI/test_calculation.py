from ecology.environment import commands_calculation, input_data
from ecology.gene_expression import express_execute_func_list
from ecology.evaluate import evaluate_calculate

# add(fa(),mul(fb(),fc()))
right_func_list = [3, 0, 4, 1, 2, 0]
wrong_fun_list = [4, 4, 4, 3, 3, 2]
input_data.a = 4
input_data.b = 5
input_data.c = 6

print(input_data.fa(), input_data.fb(), input_data.fc())

print(express_execute_func_list(right_func_list, commands_calculation))

print(evaluate_calculate(right_func_list))
