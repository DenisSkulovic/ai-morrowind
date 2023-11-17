class Effect:
    def __init__(self, name, description, magnitude, duration=None, additional_effects=None):
        self.name = name  # e.g., "Healing", "Fire Damage"
        self.description = description  # A brief description of the effect
        self.magnitude = magnitude  # The strength or potency of the effect
        self.duration = duration  # How long the effect lasts, None for instant effects
        self.additional_effects = additional_effects or []  # List of additional or secondary effects

    def apply_effect(self, target):
        # Implement the logic to apply the effect to the target
        # e.g., increase health, deal damage, etc.
        pass

    def __str__(self):
        return f"{self.name} (Magnitude: {self.magnitude}, Duration: {self.duration})"
