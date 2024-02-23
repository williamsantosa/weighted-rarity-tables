import tableio

class WeightedRarityTable:
    def __init__(self, filelocation=None):
        self.table = self.load_table(filelocation)

    def load_table(self, filelocation):
        self.table = tableio.read_table(filelocation)

    def get_weight(self, rarity):
        return self.table[rarity]