class GuessNumber:
    def __init__(self, target, lower_bound=1, upper_bound=100):
        self.target = target
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.guess = 0
        self.steps = 0
        self.previous_guesses = []

    def make_guess(self):
        # Binary search to find the midpoint
        self.guess = (self.lower_bound + self.upper_bound) // 2

        # Calculate the average of previous guesses
        average = self.guess if not self.previous_guesses else round(sum(self.previous_guesses) / len(self.previous_guesses))

        # Adjust the guess based on the average
        self.guess = (self.guess + average) // 2

        # Increment the step counter
        self.steps += 1

        # Add the current guess to the list of previous guesses
        self.previous_guesses.append(self.guess)

        # Update the bounds based on the comparison with the target
        if self.guess > self.target:
            self.upper_bound = self.guess - 1
        elif self.guess < self.target:
            self.lower_bound = self.guess + 1

    def guess_number(self):
        while self.guess != self.target:
            self.make_guess()

        # Output the results
        print(f"Target number: {self.target}")
        print(f"Number of steps: {self.steps}")


# Example usage with a target number (e.g., 42)
guess_game = GuessNumber(target=42)
guess_game.guess_number()
