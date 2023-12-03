# Binary search on some range of values
def binarySearch(low, high):
    L, R = low, high

    while L <= R:
        mid = (L + R) // 2

        if isCorrect(mid) == 1:
            R = mid - 1
        elif isCorrect(mid) == -1:
            L = mid + 1
        else:
            return mid
    return -1


# Return 1 if the guess is too big, -1 if the guess is too small, and 0 if the guess is correct
def isCorrect(guess):
    if guess > 10:  # 10 is hardcoded here, but it could be any number
        return 1
    elif guess < 10:  # 10 is hardcoded here, but it could be any number
        return -1
    else:
        return 0
