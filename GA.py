from GA_config import GAConfig


class GA:
    def __init__(self, ga_config: GAConfig):
        self.config = ga_config
        self.population = self.create_population(self.config.pop_size)

    @staticmethod
    def create_population(pop_size):
        array = list()
        for i in range(pop_size):
            array.append(self.create_individual_call())

    def create_individual(self, fun):
        def decorator(f):
            def decorated_function(*args, **kwargs):
                return f(*args, **kwargs)
            return decorated_function
        return decorator