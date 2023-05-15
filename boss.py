import item

class Boss:
    def __init__(self, name, kill_attempts=0, items=None):
        self.name = name
        self.kill_attempts = kill_attempts
        self.items = items if items is not None else []

    def add_item(self, item):
        self.items.append(item)

    def to_dict(self):
        return {
            'name': self.name,
            'kill_attempts': self.kill_attempts,
            'items': [item.to_dict() for item in self.items]
        }

    def from_dict(source):
        items = [item.from_dict(item_dict) for item_dict in source.get('items', [])]
        return Boss(
            source['name'],
            source.get('kill_attempts', 0),
            items
        )