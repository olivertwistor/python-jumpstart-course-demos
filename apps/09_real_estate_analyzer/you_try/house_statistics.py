"""
Statistics functions for real estate.
"""
import statistics

from house import House


def most_expensive_house(houses: list) -> House:
    """
    Finds the most expensive house.

    :param houses: List of house sales.

    :return: House object.
    """
    sorted_list = sorted(houses, key=lambda h: h.price)

    return sorted_list[-1]


def least_expensive_house(houses: list) -> House:
    """
    Finds the least expensive house.

    :param houses: List of house sales.

    :return: House object.
    """
    sorted_list = sorted(houses, key=lambda h: h.price)

    return sorted_list[0]


def average_house_mean(houses: list) -> House:
    """
    Finds the average house, meaning the average number of bedrooms, number of
    bathrooms, sq.ft. and price.

    :param houses: List of house sales.

    :return: House object.
    """
    avg_bedrooms = statistics.mean((h.beds for h in houses))
    avg_bathrooms = statistics.mean((h.baths for h in houses))
    avg_sqft = statistics.mean((h.sq__ft for h in houses))
    avg_price = statistics.mean((h.price for h in houses))

    avg_house = House("", "", "", "", avg_bedrooms, avg_bathrooms, avg_sqft,
                      "", "", avg_price, 0.0, 0.0)

    return avg_house


def average_house_median(houses: list) -> House:
    """
    Finds the average house, meaning the average number of bedrooms, number of
    bathrooms, sq.ft. and price.

    :param houses: List of house sales.

    :return: House object.
    """
    avg_bedrooms = statistics.median((h.beds for h in houses))
    avg_bathrooms = statistics.median((h.baths for h in houses))
    avg_sqft = statistics.median((h.sq__ft for h in houses))
    avg_price = statistics.median((h.price for h in houses))

    avg_house = House("", "", "", "", avg_bedrooms, avg_bathrooms, avg_sqft,
                      "", "", avg_price, 0.0, 0.0)

    return avg_house


def average_two_bedroom_house(houses: list) -> House:
    """
    Finds the average two-bedroom house, meaning the average number of
    bathrooms, sq.ft. and price.

    :param houses: List of house sales.

    :return: House object.
    """

    # Filter out every house that hasn't got two bedrooms.
    two_bedrooms = [
        h
        for h in houses
        if h.beds == 2
    ]

    avg_bathrooms = statistics.mean((h.baths for h in two_bedrooms))
    avg_sqft = statistics.mean((h.sq__ft for h in two_bedrooms))
    avg_price = statistics.mean((h.price for h in two_bedrooms))

    avg_house = House("", "", "", "", 0, avg_bathrooms, avg_sqft, "", "",
                      avg_price, 0.0, 0.0)

    return avg_house
