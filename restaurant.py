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

dinnerlist = [
    "Asian Express",
    "Mayflower",
    "Roux Dat Cajun",
    "Sushi Garden",
    "Canton",
    "Paradise Beach Grille",
    "Taqueria Vallata",
    "East Side Eatery",
    "Aloha Island Grill",
    "Cafe Cruz"
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

meal = input("""
Are you looking for
a) breakfast
b) lunch
c) dinner
d) snack

type in a, b ,c, or d
 """)


if meal == "a":
    restaurants = breakfastlist
elif meal == "b":
    restaurants = lunchlist
elif meal == "d":
    restaurants = snacklist
elif meal == "c":
    restaurants = dinnerlist

restaurantnum = len(restaurants)
restaurantran = random.randrange(0, restaurantnum)
restaurantstr = str(restaurantnum)
print("There are " + restaurantstr + " restaurants in the " + meal + " list")
print("How about " + restaurants[restaurantran] + "?")