#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program will check if the year is a leap year

def main():
    year = print("Enter a year  ")
    year_string = input("Enter Here plz : ")

    try:
        year = int(year_string)
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("{0} is a leap year".format(year))
                else:
                    print("{0} is not a leap year".format(year))
            else:
                print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    except Exception:
        print("This was an invalid number ")


if __name__ == "__main__":
    main()
