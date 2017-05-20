from geopy.geocoders import Nominatim
geolocator = Nominatim()

class Location():
    def __init__(self, address):
        self.address = geolocator.geocode(address)
        print(geolocator.geocode(address).raw)
        

    def country(self):
        return self.address.address.split(',')[-1].strip()

    def city(self):
        return self.address.address.split(',')[0].strip()

    def district(self):
        if self.address.address.split(',')[1].strip().count(' ') > 1:
            return self.address.address.split(',')[2].strip()
        else:
            return self.address.address.split(',')[1].strip()
