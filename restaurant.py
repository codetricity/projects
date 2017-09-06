import random


breakfastlist = [
    "Avenue Cafe",
    "The Sand Bar",
    "Zelda's",
    "Cook House",
    "Sunrise Cafe"
]

lunchlist = [
    "Sushi Garden",
    "Erik's Deli Cafe",
    "Betty's Burger",
    "Chipotle",
    "Togos",
    "Dharma's",
    "Thai Basil"
]

snacklist = [
    "iCrave",
    "Yogurtland",
    "Penny Creamery",
    "Baskin Robbins",
    "Gayle's Bakery",
    "Jamba Juice",
    "Verve",
    "Mr. Toot's Coffeehouse",
    "Off the Block"
]
fulllist = [
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

meal = input("What meal do you want? Breakfast, lunch, snack, or dinner? ")
if meal == "breakfast":
    restaurants = breakfastlist
elif meal == "lunch":
    restaurants = lunchlist
elif meal == "snack":
    restaurants = snacklist

restaurantnum = len(restaurants)
restaurantran = random.randrange(0, restaurantnum)
restaurantstr = str(restaurantnum)
print("There are " + restaurantstr + " restaurants in the " + meal + " list")
print("How about " + restaurants[restaurantran] + "?")