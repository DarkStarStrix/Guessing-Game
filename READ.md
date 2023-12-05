# Guess Number Algorithm

## Algorithm Description

The Guess Number algorithm is a binary search approach for guessing a target number within a specified range. The algorithm utilizes a systematic process of refining guesses based on the average of previous guesses and updating the search bounds until the target is identified.

## Mathematical Representation

The algorithm can be expressed by the following equations:

1. **Binary Search and Adjustment:**
   ```python
   guess_{i+1} = floor((L_i + U_i) / 2)
   guess_{i+1} = floor((guess_{i+1} + round(sum(previousGuesses) / len(previousGuesses))) / 2)
   
if guess_{i+1} > T:
    U_{i+1} = guess_{i+1} - 1
elif guess_{i+1} < T:
    L_{i+1} = guess_{i+1} + 1

Proof of Correctness
Initialization:

The algorithm starts with appropriate initial values for the search space, guess, and step counter.
Binary Search and Adjustment:

The binary search ensures a logarithmic reduction in the search space.
The adjustment based on the average refines the guess towards the target.
Bounds Update:

The bounds are updated based on the comparison with the target, narrowing down the search space.
Convergence:

The algorithm converges when the guess matches the target, ensuring correctness.
Average Calculation:

The use of the average helps in refining the guess by considering historical performance.
Termination:

The algorithm terminates when the correct target is identified.
Bounding Values:

Bounds are updated correctly, preventing unnecessary searches.
Correctness of Formula:

The formula ensures that the guess is refined based on historical performance.
Overall Correctness:

The combination of binary search, guess adjustment, and bounds updating ensures convergence.

# Example usage with a target number (e.g., 42)
guess_game = GuessNumber(target=42)
guess_game.guess_number()

# this algorithm is a binary search algorithm and only with a 100 numbers range it will find the number in 5 guesses

GuessNumberWithAverage {
>>     param(
>>         [int]$target
>>     )
>>
>>     $lowerBound = 1
>>     $upperBound = 100
>>     $guess = 0
>>     $steps = 0
>>     $previousGuesses = @()
>>
>>     while ($guess -ne $target) {
>>         $guess = [math]::floor(($lowerBound + $upperBound) / 2)
>>
>>         # Calculate the average of previous guesses
>>         $average = if ($previousGuesses.Count -gt 0) {
>>             [math]::round(($previousGuesses | Measure-Object -Average).Average)
>>         } else {
>>             $guess
>>         }
>>
>>         # Adjust the guess based on the average
>>         $guess = [math]::floor(($guess + $average) / 2)
>>
>>         $steps++
>>         $previousGuesses += $guess
>>
>>         if ($guess -gt $target) {
>>             $upperBound = $guess - 1
>>         } elseif ($guess -lt $target) {
>>             $lowerBound = $guess + 1
>>         }
>>     }
>>
>>     Write-Output "Target number: $target"
>>     Write-Output "Number of steps: $steps"
>> }
# code in powershell

