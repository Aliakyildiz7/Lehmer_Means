
# Source: https://en.wikipedia.org/wiki/Lehmer_mean
#Defining  the Function and User Interactivity
#Good example for *args, ""kwargs
#p = 1
#1 for Arithmetic Mean
#1/2 for Geometric Mean
#0 for Harmonic Mean


def lehmer_mean(*args, **kwargs):
    """Calculates Lehmer means of a series with the given p value.
    If no p value is given, its default  value is 1, which gives arithmetic mean"""

    p = kwargs.get("p", 1) #Setting the default value to 1, which means arithmetic mean

    numerator = 0
    denumerator = 0

    for x in range(len(args)):
        if args[x] <= 0:
            raise AssertionError("All the values in the series should be greater than zero")
        #assert args[x] > 0, "All the values in the series should be greater than zero"
        #Yields the same result with the above snippet

        numerator += args[x] ** p
        denumerator += args[x] ** (p - 1)

    lehmer_mean = numerator / denumerator

    return lehmer_mean



if __name__ == "__main__":
    help(lehmer_mean)
    print(lehmer_mean(1,2,3, p=0.5))





