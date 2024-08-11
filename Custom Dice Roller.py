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

    def display_results(self, results):
        """Display the results of the dice roll."""
        print("Rolling the dice...")
        print("Results:", results)
        print("Total:", sum(results))  # Show the total of the rolled dice


def main():
    """Main function to run the Dice Roller program."""
    dice_roller = DiceRoller()  # Create an instance of DiceRoller


    while True:
        try:
            # User input for number of dice and sides
            num_dice = int(input("Enter the number of dice to roll (1-10): "))
            num_sides = int(input("Enter the number of sides on each die (4, 6, 8, 10, 12, 20): "))


            # Set the dice configuration
            dice_roller.set_dice(num_dice, num_sides)


            # Roll the dice and display results
            results = dice_roller.roll_dice()
            dice_roller.display_results(results)


        except ValueError:
            print("Invalid input. Please enter integers only.")
        except KeyboardInterrupt:
            print("\nExiting the Dice Roller. Goodbye!")
            break


if __name__ == "__main__":
    main()  # Run the main function
