from GA_Core.GA import GA
from config import config_deap,config_test
from ecology.environment import array_test,array_test_sorted
from ecology.gene_expression import express_test


def main():
    ga = GA(config_test.config)  # 这个是全部函数为自定义函数的配置
    # ga = GA(config_deap.config)  # 这个是与deap工具箱无缝连接的配置
    best_individual = None  # 每一代中的最佳个体
    best_array = None  # 最佳个体的表现（基因表达结果）

    print("下面显示进化每一代的最佳个体得分：\n")

    for i in range(100):  # 进化代数
        ga.generate()  # 繁衍一代
        if i%5 == 0:
            try:
                best_individual = \
                    max(ga.pop, key=lambda individual: individual.fitness)  # 找到最佳个体
                try:
                    best_array = express_test(best_individual.gene, array_test)  # 基因表达
                except IndexError:
                    best_array = None  # 抛出异常，说明基因表达失败（为空）

                print("第{0:3d}代: 分数{1:2g}   最佳个体表现：{2}".format(
                    i,
                    best_individual.fitness,
                    best_array if best_array else "<完蛋了>"))

            except ValueError:  # 此处捕获的是max函数中ga.pop为空的异常，说明种群为空
                print('种群为空！')
                return

    print("----------------------------------------")
    print("正确答案：    {0}".format(array_test_sorted))
    print("最佳个体表现：{0}\n"
          "最佳个体分数：{1}\n"
          "当前种群大小：{2}\n"
          "交叉率：{3}\n"
          "突变率：{4}\n"
          "基因成分：{5}".format(
            best_array,
            best_individual.fitness if best_individual else "空种群",
            len(ga.pop),
            ga.config.p_cross,
            ga.config.p_mutate,
            best_individual.gene if best_individual else "空种群"))

if __name__ == '__main__':
    main()
