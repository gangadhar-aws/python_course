

country = input("Enter Country Name: ") # Add country name
visits = int(input("How Many times Visits")) # Number of visits
list_of_cities = input().split()# create list from formatted string


travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_newcity(country, visits, city):
    my_dict = {
        "country":country,
        "visists":visits,
        "cities": city
    }
    travel_log.append(my_dict)

add_newcity(country=country,  visits=visits, city=list_of_cities)

print(travel_log)