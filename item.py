class Item:
    def __init__(self, name, drop_rate, count =0):
        self.name = name
        self.drop_rate = drop_rate
        self.count = count

    def to_dict(self):
        return {
            'name': self.name,
            'drop_rate': self.drop_rate,
            'count': self.count
        }
    
    def from_dict(source):
        return Item(
            source['name'],
            source['drop_rate'],
            source['count', 0]
        )