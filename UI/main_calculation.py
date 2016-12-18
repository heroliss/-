from GA_Core.GA import GA
from config.config_calculation import config
from ecology.gene_expression import express_execute_func_list
from ecology.environment import input_data, commands_calculation
import random


def main():
    ga = GA(config)  # 这个是全部使用自定义函数的配置
    best_individual = None  # 每一代中的最佳个体

    print("下面显示进化每一代的最佳个体得分：\n")

    result = None
    for i in range(501):  # 进化代数
        ga.generate()  # 繁衍一代
        if i % 5 == 0:
            try:
                best_individual = \
                    max(ga.pop, key=lambda individual: individual.fitness)  # 找到最佳个体
                try:
                    result = [commands_calculation[func][0].__name__ for func in best_individual]  # 基因所表示的函数序列
                except:
                    print("第{0:3d}代: 分数{1:2g}   最佳个体表现：{2}".format(
                        i,
                        best_individual.fitness.values[0],
                        "<死翘翘>"))
                else:
                    print("第{0:3d}代: 分数{1:2g}   最佳个体表现：{2}".format(
                        i,
                        best_individual.fitness.values[0],
                        result if result else "<空>"))

                if best_individual and best_individual.fitness.valid and best_individual.fitness.values[0] >= 10:
                    break

            except ValueError:  # 此处捕获的是max函数中ga.pop为空的异常，说明种群为空
                print('种群为空！')
                return

    print("----------------------------------------")
    input_data.a = random.randint(-20, 20)
    input_data.b = random.randint(-20, 20)
    input_data.c = random.randint(-20, 20)
    d = input_data.a + input_data.b * input_data.c
    print("测试内容：{0}+{1}*{2}={3}".format(input_data.a, input_data.b, input_data.c, d))
    print("最佳个体表现：{0}\n"
          "最佳个体分数：{1}\n"
          "当前种群大小：{2}\n"
          "交叉率：{3}\n"
          "突变率：{4}\n"
          "基因成分：{5}\n"
          "函数序列：{6}".format(
        express_execute_func_list(best_individual, commands_calculation)[1],
        best_individual.fitness if best_individual else "空种群",
        len(ga.pop),
        ga.config.p_cross,
        ga.config.p_mutate,
        best_individual if best_individual else "空种群",
        [commands_calculation[func][0].__name__ for func in best_individual]))

    pass


if __name__ == '__main__':
    main()
