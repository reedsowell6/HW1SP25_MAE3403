# region imports
from Die import #JES MISSING CODE
# endregion

# region functions
def rollDice(N=1):
    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
import random

    def roll_dice(N):
        total_score = 0
        for _ in range(N):
            total_score += random.randint(1, 6)  # Roll a single die (values between 1 and 6)
        return total_score
    pass

def rollUnFairDice(N=1):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
import random

def roll_unfair_die():
        # Define an example probability distribution (not uniform)
        # For example, face 1 has a higher chance of being rolled.
        faces = [1, 2, 3, 4, 5, 6]
        probabilities = [0.2, 0.1, 0.2, 0.1, 0.2, 0.2]  # These must sum to 1
        return random.choices(faces, probabilities)[0]

def roll_n_unfair_dice(N):
        total_score = 0
        for _ in range(N):
            total_score += roll_unfair_die()
        return total_score

# Example usage:
N = 5  # Number of dice to roll
print(f"Total score from rolling {N} unfair dice: {roll_n_unfair_dice(N)}")

pass

# endregion