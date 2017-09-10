import random
import pygame
pygame.init()
pygame.display.set_caption("Restaurants")
iconsurface = pygame.image.load("cherry.png")
pygame.display.set_icon(iconsurface)

fonts = pygame.font.Font("heart.ttf", 50)
pink = (247, 96, 237)
blue = (96, 247, 222)
lightblue = (78, 186, 244)
silver = (213, 223, 229)
black = (0, 0, 0)
yellow = (248, 255, 130)
palegreen = (204, 255, 181)
white = (255, 255, 255)
orange = (255, 127, 48)
darkpink = (140, 30, 70)
purple = (126, 67, 140)


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

fullList = [
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

breakfastbutton = fonts.render("Breakfast", False, palegreen)
breakfastbuttonrect = breakfastbutton.get_rect()
breakfastbuttonrect.topleft = (130, 120)
breakfastbuttonrect.width = breakfastbuttonrect.width + 10

lunchbutton = fonts.render("Lunch", False, lightblue)
lunchbuttonrect = lunchbutton.get_rect()
lunchbuttonrect.topleft = (502, 120)
lunchbuttonrect.width = lunchbuttonrect.width + 10

dinnerbutton = fonts.render("Dinner", False, orange)
dinnerbuttonrect = dinnerbutton.get_rect()
dinnerbuttonrect.topleft = (502, 490)
dinnerbuttonrect.width = dinnerbuttonrect.width + 10

snackbutton = fonts.render("Snack", False, purple)
snackbuttonrect = snackbutton.get_rect()
snackbuttonrect.topleft = (130, 490)
snackbuttonrect.width = snackbuttonrect.width + 10

meal = "none"
restaurants = fullList
restaurantMessage = ""
messageColor = black

while gameon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameon = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if allbuttonrect.collidepoint(mousepos):
                restaurants = fullList
                restaurantnum = len(restaurants)
                restaurantran = random.randrange(0, restaurantnum)
                restaurantstr = restaurants[restaurantran]
                restaurantMessage = "Caitlyn recommends " + restaurantstr
                messageColor = pink
            if breakfastbuttonrect.collidepoint(mousepos):
                restaurants = breakfastlist
                restaurantnum = len(restaurants)
                restaurantran = random.randrange(0, restaurantnum)
                restaurantstr = restaurants[restaurantran]
                restaurantMessage = "Caitlyn recommends " + restaurantstr
                messageColor = palegreen
            if lunchbuttonrect.collidepoint(mousepos):
                restaurants = lunchlist
                restaurantnum = len(restaurants)
                restaurantran = random.randrange(0, restaurantnum)
                restaurantstr = restaurants[restaurantran]
                restaurantMessage = "Caitlyn recommends " + restaurantstr
                messageColor = lightblue
            if dinnerbuttonrect.collidepoint(mousepos):
                restaurants = dinnerlist
                restaurantnum = len(restaurants)
                restaurantran = random.randrange(0, restaurantnum)
                restaurantstr = restaurants[restaurantran]
                restaurantMessage = "Caitlyn recommends " + restaurantstr
                messageColor = orange
            if snackbuttonrect.collidepoint(mousepos):
                restaurants = snacklist
                restaurantnum = len(restaurants)
                restaurantran = random.randrange(0, restaurantnum)
                restaurantstr = restaurants[restaurantran]
                restaurantMessage = "Caitlyn recommends " + restaurantstr
                messageColor = purple

    screen.fill(black)
    messageSurface = fonts.render(restaurantMessage, False, messageColor)
    screen.blit(messageSurface, (100, 231))
    
    screen.blit(allbutton, (380, 304))
    pygame.draw.rect(screen, blue, allbuttonrect, 1)

    screen.blit(breakfastbutton, (130, 120))
    pygame.draw.rect(screen, white, breakfastbuttonrect, 1)

    screen.blit(lunchbutton, (502, 120))
    pygame.draw.rect(screen, yellow, lunchbuttonrect, 1)

    screen.blit(dinnerbutton, (502, 490))
    pygame.draw.rect(screen, darkpink, dinnerbuttonrect, 1)

    screen.blit(snackbutton, (130, 490))
    pygame.draw.rect(screen, yellow, snackbuttonrect, 1)

    pygame.display.update()

