"""
Main program file for this application.
"""
import os

import house_statistics
from csv_manager import CsvManager


def main():
    """
    Main program flow.
    """
    print_header()
    print("Loading CSV real estate data...")
    try:
        csv_abspath = os.path.join(
            os.path.dirname(__file__),
            "SacramentoRealEstateTransactions2008.csv"
        )
        csv_manager = CsvManager(csv_abspath)
        compute_statistics(csv_manager.houses)

    except FileNotFoundError:
        print("FileNotFoundError: {} is not a file.".format(csv_abspath))
    except OSError:
        print("OSError: {} couldn't be opened for reading.".format(csv_abspath))


def print_header():
    """
    Prints out the program header to stdout.
    """
    print()
    print("-------------------")
    print("  REAL ESTATE APP")
    print("-------------------")
    print()


def compute_statistics(houses: list):
    """
    Computes various statistics about real estate and prints it to stdout.

    :param houses: List of house sales.
    """
    most_expensive_house = house_statistics.most_expensive_house(houses)
    if most_expensive_house:
        print("Most expensive house: {}-bed, {}-bath house for ${:,} in {}"
              .format(most_expensive_house.beds, most_expensive_house.baths,
                      most_expensive_house.price, most_expensive_house.city))

    least_expensive_house = house_statistics.least_expensive_house(houses)
    if least_expensive_house:
        print("Least expensive house: {}-bed, {}-bath house for ${:,} in {}"
              .format(least_expensive_house.beds, least_expensive_house.baths,
                      least_expensive_house.price, least_expensive_house.city))

    average_house_mean = house_statistics.average_house_mean(houses)
    if average_house_mean:
        print("Average house (mean): ${:,}, {} bedrooms, {} bathrooms, "
              "{:,} ft\u00b2"
              .format(round(average_house_mean.price),
                      round(average_house_mean.beds),
                      round(average_house_mean.baths),
                      round(average_house_mean.sq__ft)))

    average_house_median = house_statistics.average_house_median(houses)
    if average_house_median:
        print(
            "Average house (median): ${:,}, {} bedrooms, {} bathrooms, "
            "{:,} ft\u00b2"
            .format(round(average_house_median.price),
                    round(average_house_median.beds),
                    round(average_house_median.baths),
                    round(average_house_median.sq__ft)))


    average_two_bed_house = house_statistics.average_two_bedroom_house(houses)
    if average_two_bed_house:
        print("Average two bedroom house: ${:,}, {} bathrooms, {:,} ft\u00b2"
              .format(round(average_two_bed_house.price),
                      round(average_two_bed_house.baths),
                      round(average_two_bed_house.sq__ft)))


if __name__ == '__main__':
    main()
