import pygame
import random
import sys
pygame.init()


# 
Cus =["img/Customer/standL.png",
      "img/Customer/standL1.png",
      "img/Customer/standL2.png"]


walkRight = [pygame.image.load("img/character/png/run/runR/runR1.png"),
            pygame.image.load("img/character/png/run/runR/runR2.png"),
            pygame.image.load("img/character/png/run/runR/runR3.png"),
            pygame.image.load("img/character/png/run/runR/runR4.png"),
            pygame.image.load("img/character/png/run/runR/runR5.png"),
            pygame.image.load("img/character/png/run/runR/runR6.png"),
            pygame.image.load("img/character/png/run/runR/runR7.png"),
            pygame.image.load("img/character/png/run/runR/runR8.png"),
            pygame.image.load("img/character/png/run/runR/runR9.png"),
            pygame.image.load("img/character/png/run/runR/runR10.png")]

walkLeft = [pygame.image.load("img/character/png/run/runL/runL1.png"),
            pygame.image.load("img/character/png/run/runL/runL2.png"),
            pygame.image.load("img/character/png/run/runL/runL3.png"),
            pygame.image.load("img/character/png/run/runL/runL4.png"),
            pygame.image.load("img/character/png/run/runL/runL5.png"),
            pygame.image.load("img/character/png/run/runL/runL6.png"),
            pygame.image.load("img/character/png/run/runL/runL7.png"),
            pygame.image.load("img/character/png/run/runL/runL8.png"),
            pygame.image.load("img/character/png/run/runL/runL9.png"),
            pygame.image.load("img/character/png/run/runL/runL10.png")]
# 
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Button')

But_top = pygame.image.load('img/RL/RLtop.png').convert_alpha()
But_down = pygame.image.load('img/RL/RLdown.png').convert_alpha()
But_Buy = pygame.image.load('img/RL/Buy.png').convert_alpha()
But_Exit = pygame.image.load('img/RL/Exit.png').convert_alpha()
# 
character  = pygame.image.load("img/character/png/stand/standR/standR1.png")
Monster    = pygame.image.load(random.choice(Cus))
# 
background = pygame.image.load("img/BG3.png")
botground  = pygame.image.load("img/botdown.png")
background1 = pygame.image.load("img/sell1.png")
# สี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#ตัวอักษร
font1 = pygame.font.Font("Font/Baskic8-Bold.otf", 24)
clock = pygame.time.Clock()

money = 1000
Number = "0"
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

# 

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            
        else:
            win.blit(character, (self.x, self.y))

class Customer (object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if self.left:
            win.blit(Monster, (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(Monster, (self.x, self.y))
            self.walkCount += 1
            
        else:
            win.blit(Monster, (self.x, self.y))
    #การเดินของ custommer
    def move(self):
        
        if stat == 1 :
            self.x -= self.velocity
        elif stat == 2:
            self.y -= self.velocity
        elif stat == 3:
            self.y += self.velocity
        elif stat == 4:
            self.x -= self.velocity
        elif stat == 5:
            self.y += self.velocity
# 

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

    def Show_B(self):
            screen.blit(self.image, (self.rect.x ,self.rect.y))

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
                if self.add_type == "add":
                    melon += 1
                    money -= 10
                elif self.add_type == "del" and melon > 0:
                    melon -= 1
                    money += 10

            elif self.goods_type == "banana":
                if self.add_type == "add":
                    banana += 1
                    money -= 10
                elif self.add_type == "del":
                    if banana > 0:
                        banana -= 1
                        money += 10

            elif self.goods_type == "apple":
                if self.add_type == "add":
                    apple += 1
                    money -= 50
                elif self.add_type == "del":
                    if apple > 0:
                        apple -= 1
                        money += 50
            
            elif self.goods_type == "potato":
                if self.add_type == "add":
                    potato += 1
                    money -= 100
                elif self.add_type == "del":
                    if potato > 0:
                        potato -= 1
                        money += 100
        
            elif self.goods_type == "stawberry":
                if self.add_type == "add":
                    stawberry += 1
                    money -= 200
                elif self.add_type == "del":
                    if stawberry > 0:
                        stawberry -= 1
                        money += 200
            # เนื้อ
            elif self.goods_type == "sausage":
                if self.add_type == "add":
                    sausage += 1
                    money -= 10
                elif self.add_type == "del":
                    if sausage > 0:
                        sausage -= 1
                        money += 10

            elif self.goods_type == "fish":
                if self.add_type == "add":
                    fish += 1
                    money -= 30
                elif self.add_type == "del":
                    if fish > 0:
                        fish -= 1
                        money += 30

            elif self.goods_type == "selmon":
                if self.add_type == "add":
                    selmon += 1
                    money -= 60
                elif self.add_type == "del":
                    if selmon > 0:
                        selmon -= 1
                        money += 60
            
            elif self.goods_type == "bacon":
                if self.add_type == "add":
                    bacon += 1
                    money -= 120
                elif self.add_type == "del":
                    if bacon > 0:
                        bacon -= 1
                        money += 120
        
            elif self.goods_type == "cow":
                if self.add_type == "add":
                    cow += 1
                    money -= 300
                elif self.add_type == "del":
                    if cow > 0:
                        cow -= 1
                        money += 300
            # น้ำ
            elif self.goods_type == "water":
                if self.add_type == "add":
                    water += 1
                    money -= 5
                elif self.add_type == "del":
                    if water > 0:
                        water -= 1
                        money += 5

            elif self.goods_type == "cola":
                if self.add_type == "add":
                    cola += 1
                    money -= 15
                elif self.add_type == "del":
                    if cola > 0:
                        cola -= 1
                        money += 15

            elif self.goods_type == "oil":
                if self.add_type == "add":
                    oil += 1
                    money -= 25
                elif self.add_type == "del":
                    if oil > 0:
                        oil -= 1
                        money += 25
            
            elif self.goods_type == "milk":
                if self.add_type == "add":
                    milk += 1
                    money -= 50
                elif self.add_type == "del":
                    if milk > 0:
                        milk -= 1
                        money += 50
        
            elif self.goods_type == "wine":
                if self.add_type == "add":
                    wine += 1
                    money -= 500
                elif self.add_type == "del":
                    if wine > 0:
                        wine -= 1
                        money += 500
            
        

def reload_s():
    # screen.blit(background, (0, 0))
    # screen.blit(background1, (0, 0))
    # ผลไม้
    screen.blit(botground, (0, 600))
    screen.blit(font1.render(str(melon), True, BLACK), (130,72))
    screen.blit(font1.render(str(banana), True, BLACK), (130,167))
    screen.blit(font1.render(str(apple), True, BLACK), (130,262))
    screen.blit(font1.render(str(potato), True, BLACK), (130,357))
    screen.blit(font1.render(str(stawberry), True, BLACK), (130,452))
    # เนื้อ
    screen.blit(font1.render(str(sausage), True, BLACK),  (370,72))
    screen.blit(font1.render(str(fish), True, BLACK), (370,167))
    screen.blit(font1.render(str(selmon), True, BLACK), (370,262))
    screen.blit(font1.render(str(bacon), True, BLACK), (370,357))
    screen.blit(font1.render(str(cow), True, BLACK), (370,452))
    # น้ำ
    screen.blit(font1.render(str(water), True, BLACK),  (610,72))
    screen.blit(font1.render(str(cola), True, BLACK), (610,167))
    screen.blit(font1.render(str(oil), True, BLACK), (610,262))
    screen.blit(font1.render(str(milk), True, BLACK), (610,357))
    screen.blit(font1.render(str(wine), True, BLACK), (610,452))
    
    screen.blit(font1.render(str(money), True, WHITE), (605,645))
    # 
    
    man.draw(screen)
    Cut.draw(screen)
    Show_add()
    # screen.blit(botground, (0, 600))
    text = font1.render(Number, True, WHITE)
    screen.blit(text, (300,640))
    # screen.blit(botground, (0, 600))
    # 
    pygame.display.flip()
    pygame.display.update()

def Bott():
    # ผลไม้

    Button_top_melon.draw(event)
    Button_down_melon.draw(event)

    Button_top_banana.draw(event)
    Button_down_banana.draw(event)

    Button_top_apple.draw(event)
    Button_down_apple.draw(event)

    Button_top_potato.draw(event)
    Button_down_potato.draw(event)

    Button_top_stawberry.draw(event)
    Button_down_stawberry.draw(event)

    # เนื้อ

    Button_top_sausage.draw(event)
    Button_down_sausage.draw(event)

    Button_top_fish.draw(event)
    Button_down_fish.draw(event)

    Button_top_selmon.draw(event)
    Button_down_selmon.draw(event)

    Button_top_bacon.draw(event)
    Button_down_bacon.draw(event)

    Button_top_cow.draw(event)
    Button_down_cow.draw(event)
    # น้ำ
    Button_top_water.draw(event)
    Button_down_water.draw(event)

    Button_top_cola.draw(event)
    Button_down_cola.draw(event)

    Button_top_oil.draw(event)
    Button_down_oil.draw(event)

    Button_top_milk.draw(event)
    Button_down_milk.draw(event)

    Button_top_wine.draw(event)
    Button_down_wine.draw(event)

    # screen.blit(botground, (0, 600))
    Button_Exit.draw(event)
    Button_Buy.draw(event)
    


def Show_add():
    # ผลไม้

    Button_top_melon.Show_B()
    Button_down_melon.Show_B()

    Button_top_banana.Show_B()
    Button_down_banana.Show_B()

    Button_top_apple.Show_B()
    Button_down_apple.Show_B()

    Button_top_potato.Show_B()
    Button_down_potato.Show_B()

    Button_top_stawberry.Show_B()
    Button_down_stawberry.Show_B()

    # เนื้อ

    Button_top_sausage.Show_B()
    Button_down_sausage.Show_B()

    Button_top_fish.Show_B()
    Button_down_fish.Show_B()

    Button_top_selmon.Show_B()
    Button_down_selmon.Show_B()

    Button_top_bacon.Show_B()
    Button_down_bacon.Show_B()

    Button_top_cow.Show_B()
    Button_down_cow.Show_B()
    # น้ำ
    Button_top_water.Show_B()
    Button_down_water.Show_B()

    Button_top_cola.Show_B()
    Button_down_cola.Show_B()

    Button_top_oil.Show_B()
    Button_down_oil.Show_B()

    Button_top_milk.Show_B()
    Button_down_milk.Show_B()

    Button_top_wine.Show_B()
    Button_down_wine.Show_B()

    # screen.blit(botground, (0, 600))
    Button_Exit.Show_B()
    Button_Buy.Show_B()

# ผลไม้

Button_top_melon = Button(220, 47, But_top,"melon","add")
Button_down_melon = Button(220, 83, But_down,"melon","del")

Button_top_banana = Button(220, 144, But_top,"banana","add")
Button_down_banana = Button(220, 178, But_down,"banana","del")

Button_top_apple = Button(220, 239, But_top,"apple","add")
Button_down_apple = Button(220, 273, But_down,"apple","del")

Button_top_potato = Button(220, 335, But_top,"potato","add")
Button_down_potato = Button(220, 368, But_down,"potato","del")

Button_top_stawberry = Button(220, 431, But_top,"stawberry","add")
Button_down_stawberry = Button(220, 463, But_down,"stawberry","del")

# เนื้อ
Button_top_sausage = Button(460, 47, But_top,"sausage","add")
Button_down_sausage = Button(460, 83, But_down,"sausage","del")

Button_top_fish = Button(460, 144, But_top,"fish","add")
Button_down_fish = Button(460, 178, But_down,"fish","del")

Button_top_selmon = Button(460, 239, But_top,"selmon","add")
Button_down_selmon = Button(460, 273, But_down,"selmon","del")

Button_top_bacon = Button(460, 335, But_top,"bacon","add")
Button_down_bacon = Button(460, 368, But_down,"bacon","del")

Button_top_cow = Button(460, 431, But_top,"cow","add")
Button_down_cow = Button(460, 463, But_down,"cow","del")

# น้ำ
Button_top_water = Button(700, 47, But_top,"water","add")
Button_down_water = Button(700, 83, But_down,"water","del")

Button_top_cola = Button(700, 144, But_top,"cola","add")
Button_down_cola = Button(700, 178, But_down,"cola","del")

Button_top_oil = Button(700, 239, But_top,"oil","add")
Button_down_oil = Button(700, 273, But_down,"oil","del")

Button_top_milk = Button(700, 335, But_top,"milk","add")
Button_down_milk = Button(700, 368, But_down,"milk","del")

Button_top_wine = Button(700, 431, But_top,"wine","add")
Button_down_wine = Button(700, 463, But_down,"wine","del")

Button_Exit = Button(225, 515, But_Exit, "Exit", "Exit")
Button_Buy = Button(470, 515, But_Buy, "Buy", "Exit")

man = Player(150, 111, 64, 64)
Cut = Customer(1000, 400, 64, 64)
stat = 1

run = True

while run:
    clock.tick(20)
    screen.blit(background, (0, 0))
    screen.blit(background1, (0, 0))
    
    for event in pygame.event.get():
        Bott()
        reload_s()
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                Number = Number[:-1]
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_0:
                    Number += event.unicode
                if event.key ==  pygame.K_1:
                    Number += event.unicode
                if event.key ==  pygame.K_2:
                    Number += event.unicode
                if event.key ==  pygame.K_3:
                    Number += event.unicode
                if event.key ==  pygame.K_4:
                    Number += event.unicode
                if event.key ==  pygame.K_5:
                    Number += event.unicode
                if event.key ==  pygame.K_6:
                    Number += event.unicode
                if event.key ==  pygame.K_7:
                    Number += event.unicode
                if event.key ==  pygame.K_8:
                    Number += event.unicode
                if event.key ==  pygame.K_9:
                    Number += event.unicode

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x > 100 - man.width - man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
        character  = pygame.image.load("img/character/png/stand/standL/standL1.png")
    elif keys[pygame.K_RIGHT] and man.x < 390 - man.width - man.velocity:
        man.x += man.velocity
        man.right = True
        man.left = False
        character  = pygame.image.load("img/character/png/stand/standR/standR1.png")
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if stat == 1:
        Cut.move()
        if Cut.x == 500:
            stat = 2
    if stat ==2 :
        Cut.move()       
        if Cut.y == 150:
            stat = 3
    if stat == 3 :
        Cut.move()
        if Cut.y == 250:
            stat = 4
    if stat == 4 :
        Cut.move()
        if Cut.x == 150:
            stat = 5
    if stat == 5 :
        Cut.move()
        if Cut.y == 700:
            stat = 6
    if stat == 6 :
        Monster    = pygame.image.load(random.choice(Cus))
        Cut.x = 1000
        Cut.y = 400
        stat = 1

    reload_s()
    
        
    

pygame.quit()