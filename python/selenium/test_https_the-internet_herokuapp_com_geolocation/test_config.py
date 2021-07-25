

# DEFINITIONS
pg = 'https://the-internet.herokuapp.com/geolocation'
button = '//button["Where am I?"]'
pq_lat = '//div[@id="lat-value"]'
pq_long = '//div[@id="long-value"]'
google_map_link = '//*[@id="map-link"]/a'

# INPUTS
class pos_struct:
    def __init__(self, latitude, longitude, accuracy):
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy


out_of_globe = pos_struct(100, 100, 100)
globe_boundary_cordinates = pos_struct(90, 180, 100)
negative_cordinates = pos_struct(-45, -45, 100)

KPT = pos_struct(50.021167999999996, 19.8861912, 100)   # KPT, czerwone maki, krakow, PL
Codahead = pos_struct(50.0349715, 19.9362586, 100)      # Codahead, rydlowka, krakow, PL


# EXPECTED
title = 'The Internet'
pg_backendPerformance_max = 10000
pg_frontendPerformance_max = 10000
expected_link_str = 'http://maps.google.com/?q='    # expected_link_str + str(x.latitude) + ',' + str(x.longitude)
