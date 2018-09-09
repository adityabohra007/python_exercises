class Transaction:
    def __init__(self, city, zipcode, state, beds, baths, sq__ft,
                 home_type, sale_date, price, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.sale_date = sale_date
        self.type = home_type
        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zip = zipcode
        self.city = city

    @staticmethod
    def create_from_dict(data):
        return Transaction(
            data['city'],
            data['zip'],
            data['state'],
            int(data['beds']),
            int(data['baths']),
            int(data['sq__ft']),
            data['type'],
            data['sale_date'],
            float(data['price']),
            float(data['latitude']),
            float(data['longitude']),
        )
