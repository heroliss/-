class GAConfig:
    def __init__(self):
        self.func_mutate = None  # 突变方法
        self.func_cross = None  # 交叉方法
        self.func_select = None  # 选择方法
        self.func_evaluate = None  # 估价函数
        self.func_create_individual_gene = None  # 创建个体基因方法

        self.__p_cross_var = None
        self.__p_mutate_var = None
        self.__pop_size_var = None

    @property
    def p_cross(self):
        # 交叉概率
        return self.__p_cross_var

    @p_cross.setter
    def p_cross(self, value):
        # 设置交叉概率
        if 0 <= value <= 1:
            self.__p_cross_var = value
        else:
            raise ValueError('交叉概率范围为[0,1]')

    @property
    def p_mutate(self):
        # 变异概率
        return self.__p_mutate_var

    @p_mutate.setter
    def p_mutate(self, value):
        # 设置变异概率
        if 0 <= value <= 1:
            self.__p_mutate_var = value
        else:
            raise ValueError('变异概率范围为[0,1]')

    @property
    def pop_size(self):
        # 种群规模
        return self.__pop_size_var

    @pop_size.setter
    def pop_size(self, value):
        # 设置种群规模
        if isinstance(value, int) and value > 0:
            self.__pop_size_var = value
        else:
            raise ValueError('种群规模必须为正整数')
