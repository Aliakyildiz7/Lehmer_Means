"""
In the first version, there was a bug such that when you enter two non_positive values consecutively,
the program added it into the list,
instead of prompting "All the numbers in the series must be greater than zero. \nPlease enter a number greater  than zero."

"""


from Lehmer_Means import lehmer_mean


def get_float_input(prompt: str):
    while True:
        try:
            ans = float(input(prompt))
            return ans
        except ValueError:
            return get_float_input("Please enter a valid number")


def get_float_greater_than_zero(prompt: str):

    x = get_float_input(prompt)

    if x <= 0:

        return get_float_greater_than_zero("All the numbers in the series must be greater than zero. \nPlease enter a number greater  than zero.")

    return x


def get_command(prompt: str):

    while True:
        command = input(prompt)

        if command.upper() == "No".upper() or command.upper() == "yes".upper():
            return command
        else:
            return get_command("Please enter a valid command(Yes or No)")





def main():

    print("This program calculates the lehmer means of a series, with the given p value.")
    print("All the numbers in the series must be greater than zero")
    print("For more information, please take a look at: https://en.wikipedia.org/wiki/Lehmer_mean")

    liste = []

    i = 1
    while True:

        k = get_float_greater_than_zero(f"\nPlease enter the {i}. number to add to the series.")

        if k.is_integer():
            liste.append(int(k))
        else:
            liste.append(k)

        print(f"\nThe series fo far is {liste}")

        if get_command("\nWill you enter another number to the series?(Yes or No)").upper() == "yes".upper():
            i += 1
            continue
        else:
            break
    print(liste)

    p = (get_float_input("\nPlease enter the p value. \nYou may enter 1 for arithemetic mean, 0.5 for geometric mean, and 0 for harmonic mean"))

    final_message = "\nThe Lehmer means of the series {} with the p value of {} is {}"

    if p.is_integer():
        print(final_message.format(liste, int(p), lehmer_mean(*liste, p=p)))
    else:
        print(final_message.format(liste, p, lehmer_mean(*liste, p=p)))


if __name__ == "__main__":
    main()


