#region imports
import math
import random

def roll_dice(nDice):
    return sum(random.randint(1, 6) for _ in range(nDice))
#endregion

#region functions
def main():  # main function to roll nDice fair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 2 # number of dice
    nMinScore = 2 # total score if each die scores 1
    nMaxScore = 12 # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1  # number of possible scores
    nTally = [0] * nNumScores  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000 # how many times to roll the dice

    for i in range(nRolls):
        roll_score = roll_dice()  # roll the dice and get the total score
        nTally[roll_score - nMinScore] += 1  # increment the corresponding score in nTally

    for i in range(nNumScores):  # print the probability of each score
        probability = nTally[i] / nRolls # calculate the probability of each score
        print(f"Score {i + nMinScore}: {probability:.4f}")

def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 2  # number of dice
    nMinScore = 2  # total score if each die scores 1
    nMaxScore = 12  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1   # number of possible scores

    nTally = [0] * nNumScores  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000  # how many times to roll the dice

    for _ in range(nRolls):  # each loop rolls dice and increments a score
        roll_score = roll_unfair_dice(nDice, bias) # total score for this roll
        nTally[roll_score - nMinScore] += 1

    print("After {} rolls of {} dice...".format(nRolls, nDice))

    for i in range(nNumScores):  # print the fraction of rolls for each score
        probability = nTally[i] / nRolls
        print(f"Score {i + nMinScore}: {probability:.4f}")

main2()
#endregion

#this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()

# ChatGPT was used to create/format this code