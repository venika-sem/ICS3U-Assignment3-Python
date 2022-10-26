#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: oct 2022
# This program gives a bonus of 5% of yearly salary


import constants


def main():
    # this function gives a bonus of 5% of yearly salary

    # input
    salary = float(input("Please, enter your salary: "))
    print("")

    year_of_service = float(input("Please, enter year of service: "))
    print("")

    # output
    if year_of_service > constants.BONUS_YEARS:
        bonus = constants.BONUS_PERCENT * salary
        print("You are eligible for bonus! The net bonus is: {0} .".format(bonus))
    else:
        print("Sorry, you are not eligible for the 5 percent bonus.")

    print("\nDone.")


if __name__ == "__main__":
    main()
