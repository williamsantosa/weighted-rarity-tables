import tableio
import json

class WeightedRarityTable:
    def __init__(self, file_location=None):
        self.tables = tableio.load_tables(file_location)

    def get_table(self, table):
        return self.tables[table]
    
    # Get variable values

    def get_tables(self):
        return self.tables.keys()
    
    def get_item_pairs(self, table):
        return self.get_table(table).items()
    
    def __str__(self):
        return json.dumps(self.tables, indent=2, sort_keys=True)