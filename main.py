from config import config
from GA_Core.GA import GA
from environment import express_test, array_test,array_test_sorted


def main():
    ga = GA(config)
    print("下面显示进化每一代的最佳个体得分：\n")
    for i in range(300):  # 进化100代
        ga.generate()
        best_individual = \
            max(ga.pop, key=lambda individual: individual.fitness)
        print("第{0:3d}代:{1:5g}".format(i,best_individual.fitness))

    # 找出最佳个体
    best_individual = \
        max(ga.pop, key = lambda individual:individual.fitness)

    best_array = None
    try:
        best_array = express_test(best_individual.gene, array_test)
    except:
        best_array = [0]
    print("正确答案：    {0}".format(array_test_sorted))
    print("最佳个体表现：{0}\n"
          "最佳个体分数：{1}\n"
          "当前种群大小：{2}\n"
          "交叉率：{3}\n"
          "突变率：{4}\n"
          "基因成分：{5}".format(
            best_array,
            best_individual.fitness,
            len(ga.pop),
            ga.config.p_cross,
            ga.config.p_mutate,
            best_individual.gene))

if __name__ == '__main__':
    main()