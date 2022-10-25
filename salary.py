#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: oct 2022
# This program gives a bonus of 5% of yearly salary

import math


def main():
    # this function gives a bonus of 5% of yearly salary

    # input
    salary = int(input("Please, enter your salary: "))
    print("")

    year_of_service = int(input("Please, enter year of service: "))
    print("")

    # process 
    5 / 100 * salary
    
    #output
    if year_of_service > 5:
        print("You are eligible for the 5 percent bonus!".format(5 / 100 * salary))
    else:
        print("Sorry, you are not eligible for the 5 percent bonus.")

    print("\nDone.")


if __name__ == "__main__":
    main()
