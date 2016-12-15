def express_test(gene, array):
    # 基因表达测试
    array_new = array.copy()
    for a, b in zip(gene[::2], gene[1::2]):
        array_new[a], array_new[b] = array_new[b], array_new[a]
    return array_new

