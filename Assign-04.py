#!/usr/bin/env python3
# Created By: Frankie Fox Wagoosh
# Date: Nov, 17, 2022
# This program tells you how much even and odd you have
# The program while also not crashing when entering a non integer


def main():
    # Tries to get the user's numbers as integers
    even_counter = 0
    odd_counter = 0
    # The while loop is created
    while True:
        user_num = input("Enter an integer or q to quit: ")
        # q us used to break out of the loop
        if user_num == "q":
            break

        try:
            # This casts the user_num to an int
            user_num = int(user_num)
        except:
            # This is the exception so the program doesn't crash
            print("This is not an integer. Enter an integer or q to quit")
        else:
            # This checks if the user_num is even
            if user_num % 2 == 0:
                even_counter = even_counter + 1
            # This checks if the user_num is odd
            if user_num % 2 != 0:
                odd_counter = odd_counter + 1
        # This tells you how much even and odd numbers you entered
    print(
        "you entered {} even numbers and {} odd numbers .".format(
            even_counter, odd_counter
        )
    )


if __name__ == "__main__":
    main()
