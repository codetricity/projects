import random
import pygame
pygame.init()

fonts = pygame.font.Font("heart.ttf", 50)
pink = (247, 96, 237)
blue = (96, 247, 222)
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

allbutton = fonts.render("All", False, pink)
allbuttonrect = allbutton.get_rect()
allbuttonrect.topleft = (380, 304)
allbuttonrect.width = allbuttonrect.width + 10
meal = "none"
restaurants = fulllist

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if allbuttonrect.collidepoint(mousepos):
                meal = "all"
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
    print(restaurantstr)
    
    screen.blit(allbutton, (380, 304))
    pygame.draw.rect(screen, blue, allbuttonrect, 1)
    pygame.display.update()

