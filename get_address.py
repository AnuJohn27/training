import sys
from geopy.geocoders import Nominatim


def address(latitude, longitude):
    ad = Nominatim(user_agent='locate_address')
    loc = ad.geocode(latitude + ',' + longitude)
    # print(str(loc))
    result = 'Address for the given coordinates is:' + str(loc)
    return result


def main():
    args = sys.argv[1:]
    print(args)
    latitude = args[0]
    longitude = args[1]
    print(latitude,longitude)
    if not (latitude or longitude):
        print('Please enter both latitude and longitude')
    else:
        output = address(latitude, longitude)
        print(output)

if __name__ == '__main__':
  main()
    
