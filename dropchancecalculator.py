class DropChanceCalculator:
    def __init__ (self, item, attempts):
        self.item = item
        self.attempts = attempts
    
    def calculate_drop_chance(self):
        success_probability = 1 - (1 - self.item.drop_rate) ** self.attempts
        return success_probability