class Purchase:
    def __init__(self, street, city, zipcode, state, beds, baths,
                 sq__ft, home_type, sale_date, price, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.sale_date = sale_date

        self.type = home_type
        # we defined 'home_type' because 'type' (as it is in the csv header) is build-in name, but we still use
        # self.type because this ('type') is what will come as a key from transforming the file rows into dictionaries
        # (ex. {...., 'type': 'Residential', ....}) and if we use PyCharm to define it for us it will use
        # the name of the param (i.e. self.home_type) which will cause error in the create_from_dictionary method

        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zip = zipcode
        self.city = city
        self.street = street

    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            lookup['street'],
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude'])
        )
