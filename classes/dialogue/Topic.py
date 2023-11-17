class Topic:
    def __init__(self, name, interest_level, importance, cooldown_rate):
        self.name = name
        self.interest_level = interest_level  # Scale of 0-10
        self.importance = importance  # Scale of 0-10
        self.cooldown_rate = cooldown_rate  # Points decreased per hour

        # Derive max_discussed from interest_level and importance
        self.max_discussed = self.calculate_max_discussed(interest_level, importance)
        self.discussed_score = 0

    def calculate_max_discussed(self, interest_level, importance):
        # Custom logic to calculate max_discussed based on interest and importance
        # Example: average of interest_level and importance, adjusted by a factor
        return (interest_level + importance) // 2  # Simple average as an example

    def discuss(self):
        if self.discussed_score < self.max_discussed:
            self.discussed_score += 1

    def cooldown(self, hours_passed):
        self.discussed_score -= self.cooldown_rate * hours_passed
        if self.discussed_score < 0:
            self.discussed_score = 0

    def is_still_interesting(self):
        return self.discussed_score < self.max_discussed

    def __str__(self):
        return f"Topic: {self.name}, Interest Level: {self.interest_level}, Importance: {self.importance}, Discussed Score: {self.discussed_score}/{self.max_discussed}"
