import csv
import os

from house import House


class CsvManager:
    """
    This class is capable of reading a CSV file and export all data to a list
    of House objects.
    """
    def __init__(self, file_name: str, delimiter: str = ","):
        """
        Loads a CSV file and parses it into a list of House objects.

        :param file_name: Absolute path to CSV file.

        :raises FileNotFoundError: If the supplied file wasn't be found.
        :raises OSError: If the supplied file couldn't be opened for reading.
        """
        self.houses = []

        # Parse the CSV file and fill out the two preceding lists.
        self._parse_csv(file_name, delimiter)

    def _parse_csv(self, file_name: str, delimiter: str):
        """
        Parses a CSV file and fills out two lists with column headers and data
        respectively.

        :param file_name: Absolute path to a CSV file.
        :param delimiter: Which delimiter is used in the CSV file.

        :raises FileNotFoundError: If the supplied file wasn't found.
        :raises OSError: If the supplied file couldn't be opened for reading.
        """
        if not os.path.isfile(file_name):
            raise FileNotFoundError()

        with open(file_name, "r", encoding="utf-8") as fin:

            reader = csv.DictReader(fin)
            for row in reader:
                house = House.from_dictionary(row)
                self.houses.append(house)
