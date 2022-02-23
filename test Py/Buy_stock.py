import pygame
import random
import sys

screen = pygame.display.set_mode((800,800))
money = 1000

melon = 0
banana = 0
apple = 0
potato = 0
stawberry = 0

sausage = 0
fish = 0
selmon = 0
bacon = 0
cow = 0

water = 0
cola = 0
oil = 0
milk = 0
wine = 0

class Button():
    def __init__(self, x, y, image, goods_type , add_type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.size = (30,30)
        if add_type == "Exit":
            self.size = (105,50)
        self.goods_type = goods_type
        self.add_type = add_type

    def _Show_(self):
        screen.blit(self.image, (self.rect.x ,self.rect.y))

    def _is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        button_width = self.size[0]  # button width ขนาดความกว้าง
        button_height = self.size[1]  # button height ขนาดความสูง
        button_x1 = self.rect.topleft[0]  # button x1 จุดกำหนดแกน x
        button_x2 = button_x1 + button_width  # button x2
        button_y1 = self.rect.topleft[1]  # button y1 จุดกำหนดแกน y
        button_y2 = button_y1 + button_height  # button y2

        in_x_bound = (button_x1 <= mouse_x <= button_x2)
        in_y_bound = (button_y1 <= mouse_y <= button_y2)

        return in_x_bound and in_y_bound

    def draw(self,event):
        global money
        global melon 
        global banana 
        global apple 
        global potato 
        global stawberry 

        global sausage 
        global fish 
        global selmon 
        global bacon 
        global cow 

        global water 
        global cola 
        global oil 
        global milk 
        global wine 

        if event.type == pygame.MOUSEBUTTONDOWN and self._is_hovered() :
            # ผลไม้
            if self.goods_type == "Exit":
                pygame.quit()
                run = False
                print("1")
            if self.goods_type == "Buy":
                print("1")

            if self.goods_type == "melon":
                if self.add_type == "add" and money >= 10:
                    melon += 1
                    money -= 10
                elif self.add_type == "del" and melon > 0:
                    melon -= 1
                    money += 10

            elif self.goods_type == "banana":
                if self.add_type == "add" and money >= 10:
                    banana += 1
                    money -= 10
                elif self.add_type == "del" and banana > 0:
                        banana -= 1
                        money += 10

            elif self.goods_type == "apple":
                if self.add_type == "add" and money >= 50:
                    apple += 1
                    money -= 50
                elif self.add_type == "del" and apple > 0:
                        apple -= 1
                        money += 50
            
            elif self.goods_type == "potato":
                if self.add_type == "add" and money >= 100:
                    potato += 1
                    money -= 100
                elif self.add_type == "del" and potato > 0:
                        potato -= 1
                        money += 100
        
            elif self.goods_type == "stawberry":
                if self.add_type == "add" and money >= 200:
                    stawberry += 1
                    money -= 200
                elif self.add_type == "del" and stawberry > 0:
                        stawberry -= 1
                        money += 200
            # เนื้อ
            elif self.goods_type == "sausage":
                if self.add_type == "add" and money >= 10:
                    sausage += 1
                    money -= 10
                elif self.add_type == "del" and sausage > 0:
                        sausage -= 1
                        money += 10

            elif self.goods_type == "fish":
                if self.add_type == "add" and money >= 30:
                    fish += 1
                    money -= 30
                elif self.add_type == "del" and fish > 0:
                        fish -= 1
                        money += 30

            elif self.goods_type == "selmon":
                if self.add_type == "add" and money >= 60:
                    selmon += 1
                    money -= 60
                elif self.add_type == "del" and selmon > 0:
                        selmon -= 1
                        money += 60
            
            elif self.goods_type == "bacon":
                if self.add_type == "add" and money >= 120:
                    bacon += 1
                    money -= 120
                elif self.add_type == "del" and bacon > 0:
                    if bacon > 0:
                        bacon -= 1
                        money += 120
        
            elif self.goods_type == "cow":
                if self.add_type == "add" and money >= 300:
                    cow += 1
                    money -= 300
                elif self.add_type == "del" and cow > 0:
                        cow -= 1
                        money += 300
            # น้ำ
            elif self.goods_type == "water":
                if self.add_type == "add" and money >= 5:
                    water += 1
                    money -= 5
                elif self.add_type == "del" and water > 0:
                        water -= 1
                        money += 5

            elif self.goods_type == "cola":
                if self.add_type == "add" and money >= 15:
                    cola += 1
                    money -= 15
                elif self.add_type == "del" and cola > 0:
                        cola -= 1
                        money += 15

            elif self.goods_type == "oil":
                if self.add_type == "add" and money >= 25:
                    oil += 1
                    money -= 25
                elif self.add_type == "del" and oil > 0:
                        oil -= 1
                        money += 25
            
            elif self.goods_type == "milk":
                if self.add_type == "add" and money >= 50:
                    milk += 1
                    money -= 50
                elif self.add_type == "del" and milk > 0:
                        milk -= 1
                        money += 50
        
            elif self.goods_type == "wine":
                if self.add_type == "add" and money >= 500:
                    wine += 1
                    money -= 500
                elif self.add_type == "del" and wine >0:
                    if wine > 0:
                        wine -= 1
                        money += 500