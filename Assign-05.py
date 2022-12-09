# !/user/bin/env.python3
# Created By:Frankie fox
# Date: Dec. 9, 2022
# This program does the surface area of a rectangular prism
# It is a break statement loop that breaks when the user enters hi

# This function calculates and returns surface area of a rectangular prism
def calc_sa(height, length, width):
    surface_area = 2 * (width * length + height * length + height * width)
    return surface_area


def main():
    # This gets the user input for entering in the width , length and height
    user_height_str = input("Please enter a number (cm):")
    user_length_str = input("please enter a number (cm):")
    user_width_str = input("please enter a number (cm):")

    try:
        user_height = float(user_height_str)
        user_length = float(user_length_str)
        user_width = float(user_width_str)

        if user_height < 0:
            print("This is not possible")
        elif user_length < 0:
            print("This is not possible")
        elif user_width < 0:
            print("This is not possible")
        elif user_height == 0:
            print("This is not possible")
        elif user_length == 0:
            print("This is not possible")
        elif user_width == 0:
            print("This is not possible")
        else:
            user_sa = calc_sa(user_height, user_length, user_width)
            print("The surface area is {} cm^2".format(user_sa))

    except Exception:
        print("Please enter a positive number")


if __name__ == "__main__":
    main()
