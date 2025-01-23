# region imports
import Die.rollFairDie() as rfd

# endregion

# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0,0,0,0,0,0] #JES MISSING CODE  # create a list with 6 elements/items initialized to 0's
    n = 1000  # how many times to roll the die
    for i in range(1,7,1):  # each time through the loop, roll die and increment a score
        score = Die.rollFairDie()  # score = 1 to 6
        scores[1,2,3,4,5,6] += 1  # increment score-1 item b/c 0 indexing start
     print(score)
    #JES MISSING CODE


def main2():
    """
    This function rolls a fair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0,0,0,0,0,0]
    n = 10000
    for i in range(1,7,1):
        score = Die.rollFairDie()
        scores[] += 1
     print(score)
    pass


def main3():
    """
    This function rolls an unfair die 10000 times and tallys the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
   scores = [0,0,0,0,0,0]
   n = 10000
   for i in range(1,7,1):
       score = Die.rollUnfairDie()
       scores[] +- 1
    print(score)
    pass


# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()
    main3()
