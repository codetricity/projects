import random
import pygame
pygame.init()

fonts = pygame.font.Font("heart.ttf", 17)
size = (800, 600)
screen = pygame.display.set_mode(size)
gameon = True

    
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

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
    pygame.display.update()
