class Boss:
    def __init__(self, name, kill_attempts=0, items_dropped=None):
        self.name = name
        self.kill_attempts = kill_attempts
        self.items_dropped = items_dropped if items_dropped is not None else {}
