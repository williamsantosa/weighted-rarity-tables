import tableio
import json
import random

class WeightedRarityTable:
    def __init__(self, file_location=None):
        self.tables = tableio.load_tables(file_location)
        self.luck_rate = 1
    
    # Simulate 

    def get_weighted_random(self, table):
        total_weight = self.table_total_weight(table)
        sorted_table = sorted(self.get_item_pairs(table), key=lambda x: x[1])
        n = random.randint(1, total_weight)
        for item, weight in sorted_table:
            if n <= weight:
                return item
            n -= weight * self.luck_rate
        return sorted_table[-1][0]

    def get_weighted_random(self, sorted_table, total_weight):
        n = random.randint(1, total_weight)
        for item, weight in sorted_table:
            if n <= weight:
                return item
            n -= weight * self.luck_rate
        return sorted_table[-1][0]
    
    def simulate(self, table, iterations=1):
        ret = {}
        total_weight = self.table_total_weight(table)
        sorted_table = sorted(self.get_item_pairs(table), key=lambda x: x[1])
        for _ in range(iterations):
            item = self.get_weighted_random(sorted_table, total_weight)
            ret[item] = ret.get(item, 0) + 1
        return ret

    # Set values

    def set_luck_rate(self, rate):
        self.luck_rate = rate

    # Get variable values
    
    def table_total_weight(self, table):
        return sum(self.tables[table].values())

    def get_item_pairs(self, table):
        return self.tables[table].items()
    
    def __str__(self):
        return json.dumps(self.tables, indent=2, sort_keys=True)