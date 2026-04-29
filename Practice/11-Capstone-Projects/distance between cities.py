from geopy.geocoders import Nominatim
from geopy.distance import vincenty

def distance(city1, city2):
    geolocator = Nominatim()
    city1_data = geolocator.geocode(city1)
    city2_data = geolocator.geocode(city2)
    print(vincenty((city1_data.latitude, city1_data.longitude), (city2_data.latitude, city2_data.longitude)).kilometers, 'km')
distance('Stellenbosch', 'Somerset West')
