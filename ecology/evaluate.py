from .environment import array_test, array_test_sorted
from .gene_expression import express_test


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
