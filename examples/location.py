from geopy.geocoders import Nominatim
geolocator = Nominatim()

class Location():
    def __init__(self, address):
        self.address = geolocator.geocode(address)
        print(geolocator.geocode(address).raw)
        
    def city(self):
        return self.address.address.split(',')[0].strip()

    def town(self):
        return self.address.address.split(',')[3].strip()
    
    def region(self):
        return self.address.address.split(',')[4].strip()
    
    def country(self):
        return self.address.address.split(',')[-1].strip()

    def continent(self):
        return self.address.address.split(',')[-2].strip()
    
    def district(self):
        if self.address.address.split(',')[1].strip().count(' ') > 1:
            return self.address.address.split(',')[2].strip()
        else:
            return self.address.address.split(',')[1].strip()
