import pygame
import random
FPS = 60

money = 1000

Profit = [10,20,30,40,50]
Profit_add = 0
All_price = 0

melon = 1
banana = 0
apple = 0
potato = 0
stawberry = 0



melon_img = pygame.image.load("img/goods/fr/melon.png")
banana_img = pygame.image.load("img/goods/fr/banana.png")
apple_img = pygame.image.load("img/goods/fr/apple.png")
potato_img = pygame.image.load("img/goods/fr/potato.png")
stawberry_img = pygame.image.load("img/goods/fr/strawberry.png")

Choi = []
run = True
while run :
    if melon > 0 :
        Choi.append(melon_img)
    if apple > 0 :
        Choi.append("apple_img")
    else:
        Choi.remove(melon_img)
    run = False
print(Choi)
print(len(Choi))