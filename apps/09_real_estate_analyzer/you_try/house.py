class House:
    """
    A house object maps directly to a row in the CSV file listing sold houses.
    """
    def __init__(self, street: str, city: str, zip_code: str, state: str,
                 beds: int, baths: int, sq__ft: float, house_type: str,
                 sale_date: str, price: int, latitude: float, longitude: float):
        """
        Creates a new house object.

        :param street: Street address.
        :param city: City.
        :param zip_code: Postal code.
        :param state: State.
        :param beds: Number of bedrooms.
        :param baths: Number of bathrooms.
        :param sq__ft: Size of house in sq.ft.
        :param house_type: House type (residential, commercial etc.)
        :param sale_date: The date and time of the sale.
        :param price: The sale price in USD.
        :param latitude: Location of the house (lat.)
        :param longitude: Location of the house (long.)
        """
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq__ft = sq__ft
        self.house_type = house_type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def from_dictionary(cls, house_dictionary: dict) -> 'House':
        """
        Creates a house object from a dictionary of the same format as this
        class.

        :param house_dictionary: Dictionary of a house with the same format as
                                 this class.

        :return: House object,
        """
        house = House(
            house_dictionary['street'],
            house_dictionary['city'],
            house_dictionary['zip'],
            house_dictionary['state'],
            int(house_dictionary['beds']),
            int(house_dictionary['baths']),
            float(house_dictionary['sq__ft']),
            house_dictionary['type'],
            house_dictionary['sale_date'],
            int(house_dictionary['price']),
            float(house_dictionary['latitude']),
            float(house_dictionary['longitude']),
        )

        return house

    def __str__(self):
        """
        A nicer representation of this object.
        """
        pretty = "{} bedroom, {} bathroom {} sq.ft. {} house in {}, {} {} {} " \
                 "[{}, {}] sold for ${:,} on {}"\
            .format(self.beds, self.baths, self.sq__ft, self.house_type,
                    self.street, self.city, self.zip_code, self.state,
                    self.longitude, self.latitude, self.price, self.sale_date)

        return pretty
