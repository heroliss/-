class GAConfig:
    @property
    def p_cross(self):
        # 交叉概率
        return self.p_cross

    @p_cross.setter
    def p_cross(self, value):
        # 设置交叉概率
        if 0 <= value <= 1:
            self.p_cross = value
        else:
            raise ValueError('交叉概率范围为[0,1]')

    @property
    def p_mutate(self):
        # 变异概率
        return self.p_mutate

    @p_mutate.setter
    def p_mutate(self, value):
        # 设置变异概率
        if 0 <= value <= 1:
            self.p_mutate = value
        else:
            raise ValueError('变异概率范围为[0,1]')

    @property
    def pop_size(self):
        # 种群规模
        return self.pop_size

    @pop_size.setter
    def pop_size(self, value):
        # 设置种群规模
        if isinstance(value, int) and value > 0:
            self.pop_size = value
        else:
            raise ValueError('种群规模必须为正整数')

    mutate = None  # 变异函数
    cross = None  # 交叉函数
    select =None  # 选择函数
