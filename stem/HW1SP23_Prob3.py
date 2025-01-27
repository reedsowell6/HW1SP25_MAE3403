# region imports
import random
# endregion

# region functions
def between(num, low, high, inclusivelow=True, inclusivehigh=True):
    """
    I wrote this function to return a boolean to indicate if num is in a range
    :param num: the number to check
    :param low: the low end of the range
    :param high: the high end of the range
    :param inclusivelow: bool to include the low end
    :param inclusivehigh: bool to include the high end
    :return: bool indicating if between low and high limits
    """
    # check if number is greater than or equal to low
    if inclusivelow:
        lower_condition = num >= low
    else:
        lower_condition = num > low

    # check if number is less than or equal to high
    if inclusivehigh:
        upper_condition = num <= high
    else:
        upper_condition = num < high

    return lower_condition and upper_condition

    print(between(5, 1, 10))  # True (default inclusive range [1, 10])
    print(between(5, 1, 10, inclusivelow=False))  # True (exclusive low, range (1, 10])
    print(between(5, 1, 10, inclusivehigh=False))  # True (exclusive high, range [1, 10))
    print(between(5, 1, 10, inclusivelow=False, inclusivehigh=False))  # True (exclusive both ends, range (1, 10))
    print(between(1, 1, 10))  # True (1 is inclusive in [1, 10])
    print(between(10, 1, 10))  # True (10 is inclusive in [1, 10])
    print(between(10, 1, 10, inclusivehigh=False))  # False (10 is exclusive in (1, 10))

    pass


def main():

    """
    This function produces an array of numbers from a normally distributed population

    To check if the numbers generated are normally distributed, I can count
    the percentage within 1,2 and 3 standard deviations of the mean and see
    if they match the theoretical values.  I'll create 3 bins into which the
    numbers in my array will fit.  Note:  a number in bin 1 will also be in bins
    2 & 3.  A number in bin3 will not necessarily be in 1 or 2.
    :return: nothing
    """
    def generate_normal_dist(N, mean, stdev):

        arr = []  # array for storing the numbers


        bin1=0  # normal dist should contain 68% within +/-1stdev
        bin2=0  # normal dist should contain 95.5% within +/-2stdev
        bin3=0  # normal dist should contain 99.7% within +/-3stdev

        # define the edges of the limits for the various bins based on stdev
        bin1low = mean - stdev
        bin1high = mean + stdev

        bin2low = mean - 2 * stdev
        bin2high = mean + 2 * stdev

        bin3low = mean - 3 * stdev
        bin3high = mean + 3 * stdev

        for i in range(N):  # this loop generates the numbers
            num = random.gauss(mean, stdev)
            arr.append(num)
         # this checks which bin(s) the current number is in.

        # check which bin(s) the number belongs to
            if bin2low <= num <= bin2high:  # Check if it's within +/- 2 standard deviations
            bin2 += 1
            if bin3low <= num <= bin3high:  # Check if it's within +/- 3 standard deviations
            bin3 += 1
            if bin1low <= num <= bin1high:  # Check if it's within +/- 1 standard deviation
            bin1 += 1

        # Calculate the percentages for each bin
        bin1_percentage = (bin1 / N) * 100
        bin2_percentage = (bin2 / N) * 100
        bin3_percentage = (bin3 / N) * 100

        # Print the results
        print(f"Bin 1 (within 1 stdev): {bin1_percentage:.2f}%")
        print(f"Bin 2 (within 2 stdev): {bin2_percentage:.2f}%")
        print(f"Bin 3 (within 3 stdev): {bin3_percentage:.2f}%")

    # Example usage
    N = 10000  # Size of the array
    mean = 0  # Mean of the normal distribution
    stdev = 1  # Standard deviation of the normal distribution

# endregion

if __name__ == "__main__":
    main()  # calls the function main
