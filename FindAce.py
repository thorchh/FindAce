## write a for loop from 1 to 52 where you find the expected value of the number of cards until you see the first ace
## for each card, multiply the probability of seeing it by the number of cards taken to see it
## add that to the cumulative sum

def probabilityOfNotGettingAce(n):
    ## n is the number of cards drawn already
    if n == 1:
        return 48 / 52
    else:
        return ((49 - n) / (52 - n + 1)) * probabilityOfNotGettingAce(n - 1)

def probabilityOfGettingAce(n):
    ## n is the number of cards drawn already
    if n == 1:
        return 4 / 52
    else:
        return (4/(52 - n + 1)) * probabilityOfNotGettingAce(n - 1)

cumulativeSum = 0
for i in range(1, 49):
    cumulativeSum += (i) * probabilityOfGettingAce(i)

print(cumulativeSum)

