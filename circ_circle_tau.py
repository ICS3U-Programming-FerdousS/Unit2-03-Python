#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: March 3rd, 2022
# This program asks the user for the radius of
# a circle in cm. It then calculates and displays
# the circumference using tau.


import Constant


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (cm): "))
    # calculate the circumference
    circumference = Constant.TAU * radius
    # display the circumference
    print("")
    print("Circumference = {:.2f} cm". format(circumference))


if __name__ == "__main__":
    main()
