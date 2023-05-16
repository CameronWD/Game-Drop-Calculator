class Boss:
    def __init__(self, name, kill_attempts=0, items_dropped=None):
        self.name = name
        self.kill_attempts = kill_attempts
        self.items_dropped = items_dropped if items_dropped is not None else {}

    def to_dict(self):
        return {
            'name': self.name,
            'kill_attempts': self.kill_attempts,
            'items_dropped': self.items_dropped
        }

    @staticmethod
    def from_dict(source):
        return Boss(
            source['name'],
            source.get('kill_attempts', 0),
            source.get('items_dropped', {})
        )
