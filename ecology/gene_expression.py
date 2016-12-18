def express_test(gene, array):
    # 基因表达（置换法排序测试）
    array_new = array.copy()
    for a, b in zip(gene[::2], gene[1::2]):
        array_new[a], array_new[b] = array_new[b], array_new[a]
    return array_new


from copy import deepcopy


def express_execute_func_list(func_list, commands):
    # 求式子的基因表达，即执行函数序列
    ops = [['base', -1, -1]]
    variables = []
    i = 0
    while True:
        if ops[-1][2] == 0:
            args = [variables.pop() for _ in range(ops[-1][1])]
            # try:
            variables.append(ops.pop()[0](*reversed(args)))
            # except:
            #    return None
        else:
            if len(func_list) == i:
                break
            ops[-1][2] -= 1
            ops.append(deepcopy(commands[func_list[i]]))
            i += 1
    return ops, variables  # 操作符栈和变量栈，计算结果都保留在变量栈
