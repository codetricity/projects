import random
meal = input("What meal do you want? Breakfast, lunch, or dinner? ")
if meal == "lunch":
    print("You are having lunch")

restaurants = [
    "Sushi Garden",
    "Asian Express",
    "Mayflower",
    "Betty's Burgers",
    "Erik's Deli Cafe",
    "Avenue Cafe",
    "Dharma's",
    "Wasabi Tapas",
    "Roux Dat Cajun",
    "Paradise Beach Grille",
    "Taqueria Vallata",
    "iCrave",
    "Chipotle",
    "East Side Eatery"
]

restaurantnum = len(restaurants)
restaurantran = random.randrange(0, restaurantnum)
restaurantstr = str(restaurantnum)
print("There are " + restaurantstr + " restaurants in the Capitola list")
print("How about " + restaurants[restaurantran] + "?")