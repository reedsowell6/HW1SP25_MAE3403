# region imports
from Die import rollFairDie as rfd
from Die import rollUnFairDie as rufd



# endregion

# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    def rfd_1(n): #defining the function rfd
        scores = [0] * 6 # create a list with 6 elements/items initialized to 0's
        for _ in range(n):  # each time through the loop, roll die and increment a score
            score = rfd()  # score = 1 to 6
            scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start

        for i in range(6):
            probability = scores[i] / n
            print(f"Probability of rolling a {i + 1}: {probability:.4f}")

    rfd_1(1000) # Call the function with 1000 rolls

    pass

def main2():
    """
    This function rolls a fair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    def rfd(n):
        scores = [0] * 6
        for _ in range(n): # N times loop (10000)
            score = Die.rollFairDie()
            scores[score - 1] += 1

        for i in range(6):
            probability = scores[i] / n
            print(f"Probability of rolling a {i + 1}: {probability:.4f}")

    rfd(10000)
    pass


def main3():
    """
    This function rolls an unfair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    def rufd(n): # Call unfair die roll function
        scores = [0] * 6
        for _ in range(n): # Loop n 10000 times
            score = Die.rollUnfairDie()
            scores[score - 1] +- 1
        print(scores)

        for i in range(6):
            probability = scores[i] / n
            print(f"Probability of rolling a {i + 1}: {probability:.4f}")

    rufd(10000)
    pass


# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()
    main3()

# ChatGPT was used to create/format this code