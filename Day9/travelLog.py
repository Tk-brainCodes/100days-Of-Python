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


def add_new_country(country_name, times_visited,cities):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = times_visited
    new_country["cities"] = cities

    travel_log.append(new_country)
 
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)