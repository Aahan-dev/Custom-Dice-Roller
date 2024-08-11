import random

class DiceRoller:
    def __init__(self):
        """Initialize the DiceRoller with default values."""
        self.num_dice = 1  # Default number of dice
        self.num_sides = 6  # Default number of sides on each die

    def set_dice(self, num_dice, num_sides):
        """
        Set the number of dice and the number of sides on each die.

        Args:
            num_dice (int): Number of dice to roll.
            num_sides (int): Number of sides on each die.
        """
        self.num_dice = num_dice
        self.num_sides = num_sides
        print(f"Dice set to {num_dice}d{num_sides}")

    def roll_dice(self):
        """Simulate rolling the dice and return the results."""
        results = [random.randint(1, self.num_sides) for _ in range(self.num_dice)]
        return results  # Return the list of results from rolling the dice

    