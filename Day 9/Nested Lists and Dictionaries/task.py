travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "United Kingdom": ["London", "Manchester"],
    "Germany": ["Bern", "Stuttgart"],
}


# print(travel_log["France"][1])

travel_log = {
    "France": {
        "num_time_visited": 8,
        "cities_visited":["Paris", "Lille", "Dijon"]
    },
    "Germany":{
        "num_time_visited": 5,
        "cities_visited": ["Bern", "Stuttgart"],
    }
}


print(travel_log["Germany"]["cities_visited"][1])