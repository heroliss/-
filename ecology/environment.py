from operator import *

# 测试环境变量 --------------------------------------
array_test = [1, 4, 7, 2, 5, 8, 3, 6, 9]
array_test_sorted = array_test.copy()
array_test_sorted.sort()


# 计算环境变量 --------------------------------------
class InputData:  # 输入类中需手动添加自定义函数和输入变量
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        # self.result = None

    def fa(self):
        return self.a

    def fb(self):
        return self.b

    def fc(self):
        return self.c
        # def set_result(self,value):
        #     self.result = value


input_data = InputData()

commands_calculation = ([input_data.fa, 0, 0], [input_data.fb, 0, 0], [input_data.fc, 0, 0],
                        [add, 2, 2], [mul, 2, 2])  # 命令列表
