class Individual:
    gene = None
    fitness = None

    def copy(self):
        new = Individual()
        new.gene = self.gene
        new.fitness = self.fitness
        return new
