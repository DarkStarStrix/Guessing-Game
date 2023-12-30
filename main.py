class GuessNumber:
    def __init__(self, target):
        self.target = target
        self.lower_bound = 1
        self.upper_bound = 100
        self.guess = 0
        self.steps = 0

    def make_guess(self):
        self.guess = (self.lower_bound + self.upper_bound) // 2
        self.steps += 1
        if self.guess > self.target:
            self.upper_bound = self.guess - 1
        elif self.guess < self.target:
            self.lower_bound = self.guess + 1

    def guess_number(self):
        while self.guess != self.target:
            self.make_guess ()
        print (f"Target number: {self.target}")
        print (f"Number of steps: {self.steps}")


guess_game = GuessNumber (target=42)
guess_game.guess_number ()
