from environment import express_test, array_test,array_test_sorted


def evaluate_test(gene):
    score = 0
    try:
        array = express_test(gene, array_test)  # 基因的表现是将array_test内容改变
    except:
        return 0
    else:
        for i, j in zip(array_test_sorted, array):
            if i == j:
                score += 1
        return score

