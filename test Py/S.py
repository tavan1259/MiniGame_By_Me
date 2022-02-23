import pygame
import random
FPS = 60
clock = pygame.time.Clock()
pygame.init()
VELOCITY = 5
Delay = 0
HP = 5
YOU_HIT = pygame.image.load("img/RL/bule.png")
YOU_HIT_ract = YOU_HIT.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
YOU_HIT_ract.left = 160
YOU_HIT_ract.centery = 200

BUY_HIT = pygame.image.load("img/RL/red.png")
BUY_HIT_ract = BUY_HIT.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
BUY_HIT_ract.centerx = 360
BUY_HIT_ract.centery = 200

ORDER_HIT = pygame.image.load("img/RL/red.png")
ORDER_HIT_ract = ORDER_HIT.get_rect()     # รูปสี่เหลี่ยมที่มี image ข้างใน
ORDER_HIT_ract.centerx = 160
ORDER_HIT_ract.centery = 200


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
#ดึงรูปมา
background = pygame.image.load("img/BG3.png")
botground  = pygame.image.load("img/botdown.png")
Show_price = pygame.image.load("img/Show_price.png")
character = pygame.image.load("img/character/png/stand/standR/standR1.png")
Monster    = pygame.image.load(random.choice(Cus))

Ark = 0
Feel = ""
money = 1000

Profit = [10,10,10,10,20,20,30,40,50]
Profit_add = 0
All_price = 0
HIGH_score = 0


melon = 10
melon_price = 10

banana = 10 
banana_price = 10

apple = 0
apple_price = 50

potato = 0
potato_price = 100

stawberry = 0
stawberry_price = 200


sausage = 0
sausage_price = 10

fish = 0
fish_price = 30

selmon = 0
selmon_price = 60

bacon = 0
bacon_price = 120

cow = 0
cow_price = 300


water = 0
water_price = 5

cola = 0
cola_price = 15

oil = 0
oil_price = 25

milk = 0
milk_price = 50

wine = 0
wine_price = 500

Ran_goods1 = 0
Ran_goods2 = 0


melon_img = pygame.image.load("img/goods/fr/melon.png")
banana_img = pygame.image.load("img/goods/fr/banana.png")
apple_img = pygame.image.load("img/goods/fr/apple.png")
potato_img = pygame.image.load("img/goods/fr/potato.png")
stawberry_img = pygame.image.load("img/goods/fr/strawberry.png")

sausage_img = pygame.image.load("img/BG3.png")
fish_img = pygame.image.load("img/BG3.png")
selmon_img = pygame.image.load("img/BG3.png")
bacon_img = pygame.image.load("img/BG3.png")
cow_img = pygame.image.load("img/BG3.png")

water_img = pygame.image.load("img/BG3.png")
cola_img = pygame.image.load("img/BG3.png")
oil_img = pygame.image.load("img/BG3.png")
milk_img = pygame.image.load("img/BG3.png")
wine_img = pygame.image.load("img/BG3.png")

But_Sell = pygame.image.load('img/RL/SELL.png')
But_Ark = pygame.image.load('img/RL/ARK.png')

HP_5 = pygame.image.load('img/RL/HP_5.png')
HP_4 = pygame.image.load('img/RL/HP_4.png')
HP_3 = pygame.image.load('img/RL/HP_3.png')
HP_2 = pygame.image.load('img/RL/HP_2.png')
HP_1 = pygame.image.load('img/RL/HP_1.png')
HP_0 = pygame.image.load('img/RL/HP_0.png')

ANGRY = pygame.image.load('img/RL/Angry.png')
GOOD = pygame.image.load('img/RL/Good.png')
# InStock = [melon_img,banana_img,apple_img,potato_img,stawberry_img,
#         sausage_img,fish_img,selmon_img,bacon_img,cow_img,
#         water_img,cola_img,oil_img,milk_img,wine_img]

InStock = []


#ขนาดของจอ กับ ชื่อ
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("Test")
#สี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Button():
    def __init__(self, x, y, image, goods_type , add_type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.size = (30,30)
        if add_type == "Exit":
            self.size = (105,50)
        if add_type == "Ark":
            self.size = (80,38)
        if add_type == "Sell":
            self.size = (110,46)
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

Number = "0"
font1 = pygame.font.Font("Font/Baskic8-Bold.otf", 34)

def Cus_choose():
    global Ran_goods1
    global Ran_goods2
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

    if Ran_Stock == melon_img:
        screen.blit(melon_img, (25, 640))
    elif Ran_Stock == banana_img:
        screen.blit(banana_img, (25, 640))
    elif Ran_Stock == apple_img:
        screen.blit(apple_img, (25, 640))
    elif Ran_Stock == potato_img:
        screen.blit(potato_img, (25, 640))
    elif Ran_Stock == stawberry_img:
        screen.blit(stawberry_img, (25, 640))
    
    # elif Ran_Stock == sausage_img:
    #     screen.blit(sausage_img, (25, 640))
    # elif Ran_Stock == fish_img:
    #     screen.blit(fish_img, (25, 640))
    # elif Ran_Stock == selmon_img:
    #     screen.blit(selmon_img, (25, 640))
    # elif Ran_Stock == bacon_img:
    #     screen.blit(bacon_img, (25, 640))
    # elif Ran_Stock == cow_img:
    #     screen.blit(cow_img, (25, 640))

    # elif Ran_Stock == water_img:
    #     screen.blit(water_img, (25, 640))
    # elif Ran_Stock == cola_img:
    #     screen.blit(cola_img, (25, 640))
    # elif Ran_Stock == oil_img:
    #     screen.blit(oil_img, (25, 640))
    # elif Ran_Stock == milk_img:
    #     screen.blit(milk_img, (25, 640))
    # elif Ran_Stock == wine_img:
    #     screen.blit(wine_img, (25, 640))


    if len(InStock) > 1 :
        if Ran_Stock2 == melon_img:
            screen.blit(melon_img, (25, 690))
        elif Ran_Stock2 == banana_img:
            screen.blit(banana_img, (25, 690))
        elif Ran_Stock2 == apple_img:
            screen.blit(apple_img, (25, 690))
        elif Ran_Stock2 == potato_img:
            screen.blit(potato_img, (25, 690))
        elif Ran_Stock2 == stawberry_img:
            screen.blit(stawberry_img, (25, 690))

        # elif Ran_Stock2 == sausage_img:
        #     screen.blit(sausage_img, (25, 640))
        # elif Ran_Stock2 == fish_img:
        #     screen.blit(fish_img, (25, 640))
        # elif Ran_Stock2 == selmon_img:
        #     screen.blit(selmon_img, (25, 640))
        # elif Ran_Stock2 == bacon_img:
        #     screen.blit(bacon_img, (25, 640))
        # elif Ran_Stock2 == cow_img:
        #     screen.blit(cow_img, (25, 640))

        # elif Ran_Stock2 == water_img:
        #     screen.blit(water_img, (25, 640))
        # elif Ran_Stock2 == cola_img:
        #     screen.blit(cola_img, (25, 640))
        # elif Ran_Stock2 == oil_img:
        #     screen.blit(oil_img, (25, 640))
        # elif Ran_Stock2 == milk_img:
        #     screen.blit(milk_img, (25, 640))
        # elif Ran_Stock2 == wine_img:
        #     screen.blit(wine_img, (25, 640))
    
def __show():
    man.draw(screen)
    Cut.draw(screen)
    screen.blit(Show_price, (440, 40))
    Button_Sell._Show_()
    if Ark == 0:
        Button_Ark._Show_()
def Bott():
    
    Button_Sell.draw(event)
    if Ark == 0:
        Button_Ark.draw(event)

#อัพเดทจอ
def ReroadScreen():
    screen.blit(background, (0, 0))
    
    man.draw(screen)
    Cut.draw(screen)
    
    screen.blit(botground, (0, 600))
    
    text = font1.render(Number, True, WHITE)
    screen.blit(text, (300,640))
    screen.blit(font1.render(str(money), True, WHITE), (605,640))
    if HP == 5 :
        screen.blit(HP_5, (540,685))
    elif HP == 4 :
        screen.blit(HP_4, (540,685))
    elif HP == 3 :
        screen.blit(HP_3, (540,685))
    elif HP == 2 :
        screen.blit(HP_2, (540,685))
    elif HP == 1 :
        screen.blit(HP_1, (540,685))
    elif HP == 0 :
        screen.blit(HP_0, (540,685))
    pygame.display.flip()
    pygame.display.update()

Button_Sell = Button(650, 725, But_Sell, "Sell", "Sell")
Button_Ark = Button(550, 730, But_Ark, "Ark", "Ark")

man = Player(150, 111, 64, 64)
Cut = Customer(1000, 400, 64, 64)
running = True
stat = 1
RanDow = True
Nomore = True
while running:
    clock.tick(30)
    if melon > 0 :
        if InStock.count(melon_img) == 0:
            InStock.append(melon_img)
    elif melon <= 0 :
        if InStock.count(melon_img) > 0 :
            InStock.remove(melon_img)
    if banana > 0 :
        if InStock.count(banana_img) == 0:
            InStock.append(banana_img)
    elif banana <= 0 :
        if InStock.count(banana_img) > 0 :
            InStock.remove(banana_img)
    if apple > 0 :
        if InStock.count(apple_img) == 0:
            InStock.append(apple_img)
    elif apple <= 0 :
        if InStock.count(apple_img) > 0 :
            InStock.remove(apple_img)
    if potato > 0 :
        if InStock.count(potato_img) == 0:
            InStock.append(potato_img)
    elif potato <= 0 :
        if InStock.count(potato_img) > 0 :
            InStock.remove(potato_img)
    if stawberry > 0 :
        if InStock.count(stawberry_img) == 0:
            InStock.append(stawberry_img)
    elif stawberry <= 0 :
        if InStock.count(stawberry_img) > 0 :
            InStock.remove(stawberry_img)


    # if sausage > 0 :
    #     if InStock.count(sausage_img) == 0:
    #         InStock.append(sausage_img)
    # elif sausage <= 0 :
    #     if InStock.count(sausage_img) > 0 :
    #         InStock.remove(sausage_img)
    # if fish > 0 :
    #     if InStock.count(fish_img) == 0:
    #         InStock.append(fish_img)
    # elif fish <= 0 :
    #     if InStock.count(fish_img) > 0 :
    #         InStock.remove(fish_img)
    # if selmon > 0 :
    #     if InStock.count(selmon_img) == 0:
    #         InStock.append(selmon_img)
    # elif selmon <= 0 :
    #     if InStock.count(selmon_img) > 0 :
    #         InStock.remove(selmon_img)
    # if bacon > 0 :
    #     if InStock.count(bacon_img) == 0:
    #         InStock.append(bacon_img)
    # elif bacon <= 0 :
    #     if InStock.count(bacon_img) > 0 :
    #         InStock.remove(bacon_img)
    # if cow > 0 :
    #     if InStock.count(cow_img) == 0:
    #         InStock.append(cow_img)
    # elif cow <= 0 :
    #     if InStock.count(cow_img) > 0 :
    #         InStock.remove(cow_img)

    # if water > 0 :
    #     if InStock.count(water_img) == 0:
    #         InStock.append(water_img)
    # elif water <= 0 :
    #     if InStock.count(water_img) > 0 :
    #         InStock.remove(water_img)
    # if cola > 0 :
    #     if InStock.count(cola_img) == 0:
    #         InStock.append(cola_img)
    # elif cola <= 0 :
    #     if InStock.count(cola_img) > 0 :
    #         InStock.remove(cola_img)
    # if oil > 0 :
    #     if InStock.count(oil_img) == 0:
    #         InStock.append(oil_img)
    # elif oil <= 0 :
    #     if InStock.count(oil_img) > 0 :
    #         InStock.remove(oil_img)
    # if milk > 0 :
    #     if InStock.count(milk_img) == 0:
    #         InStock.append(milk_img)
    # elif milk <= 0 :
    #     if InStock.count(milk_img) > 0 :
    #         InStock.remove(milk_img)
    # if wine > 0 :
    #     if InStock.count(wine_img) == 0:
    #         InStock.append(wine_img)
    # elif wine <= 0 :
    #     if InStock.count(wine_img) > 0 :
    #         InStock.remove(wine_img)


    

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                Number = Number[:-1]
        
            if len(Number) < 9 :
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
    # การขยับของฮิตบล็อค
    if keys[pygame.K_LEFT] and YOU_HIT_ract.left > 40:
        YOU_HIT_ract.x -= VELOCITY
    if keys[pygame.K_RIGHT] and YOU_HIT_ract.right < 380:
        YOU_HIT_ract.x += VELOCITY

    if YOU_HIT_ract.colliderect(BUY_HIT_ract): #เมื่อชนกับฮิตบล็อค
        print("HIT")
    if YOU_HIT_ract.colliderect(ORDER_HIT_ract): #เมื่อชนกับฮิตบล็อค

        if len(InStock) > 0 :
            if keys[pygame.K_SPACE] and stat == 10: #เมื่อกด Spacebar
                
                Ran_Stock = random.choice(InStock)
                
                
                if Ran_Stock == melon_img:
                    Ran_goods1 = random.randint(1, melon)
                    All_price = Ran_goods1 * (melon_price + random.choice(Profit))
                elif Ran_Stock == banana_img:
                    Ran_goods1 = random.randint(1, banana)
                    All_price = Ran_goods1 * (banana_price + random.choice(Profit))
                elif Ran_Stock == apple_img:
                    Ran_goods1 = random.randint(1, apple)
                    All_price = Ran_goods1 * (apple_price + random.choice(Profit))
                elif Ran_Stock == potato_img:
                    Ran_goods1 = random.randint(1, potato)
                    All_price = Ran_goods1 * (potato_price + random.choice(Profit))
                elif Ran_Stock == stawberry_img:
                    Ran_goods1 = random.randint(1, stawberry)
                    All_price = Ran_goods1 * (stawberry_price + random.choice(Profit))
                
                # if Ran_Stock == sausage_img:
                #     Ran_goods1 = random.randint(1, sausage)
                #     All_price = Ran_goods1 * (sausage_price + random.choice(Profit))
                # elif Ran_Stock == fish_img:
                #     Ran_goods1 = random.randint(1, fish)
                #     All_price = Ran_goods1 * (fish_price + random.choice(Profit))
                # elif Ran_Stock == selmon_img:
                #     Ran_goods1 = random.randint(1, selmon)
                #     All_price = Ran_goods1 * (selmon_price + random.choice(Profit))
                # elif Ran_Stock == bacon_img:
                #     Ran_goods1 = random.randint(1, bacon)
                #     All_price = Ran_goods1 * (bacon_price + random.choice(Profit))
                # elif Ran_Stock == cow_img:
                #     Ran_goods1 = random.randint(1, cow)
                #     All_price = Ran_goods1 * (cow_price + random.choice(Profit))

                # if Ran_Stock == water_img:
                #     Ran_goods1 = random.randint(1, water)
                #     All_price = Ran_goods1 * (water_price + random.choice(Profit))
                # elif Ran_Stock == cola_img:
                #     Ran_goods1 = random.randint(1, cola)
                #     All_price = Ran_goods1 * (cola_price + random.choice(Profit))
                # elif Ran_Stock == oil_img:
                #     Ran_goods1 = random.randint(1, oil)
                #     All_price = Ran_goods1 * (oil_price + random.choice(Profit))
                # elif Ran_Stock == milk_img:
                #     Ran_goods1 = random.randint(1, milk)
                #     All_price = Ran_goods1 * (milk_price + random.choice(Profit))
                # elif Ran_Stock == wine_img:
                #     Ran_goods1 = random.randint(1, wine)
                #     All_price = Ran_goods1 * (wine_price + random.choice(Profit))



                

                if len(InStock) > 1 :
                    Ran_Stock2 = random.choice(InStock)
                    if Ran_Stock == Ran_Stock2:
                        while Nomore:
                            Ran_Stock2 = random.choice(InStock)
                            if Ran_Stock != Ran_Stock2:
                                break

                    if Ran_Stock2 == melon_img:
                        Ran_goods2 = random.randint(1, melon)
                        All_price2 = Ran_goods2 * (melon_price + random.choice(Profit))
                    elif Ran_Stock2 == banana_img:
                        Ran_goods2 = random.randint(1, banana)
                        All_price2 = Ran_goods2 * (banana_price + random.choice(Profit))
                    elif Ran_Stock2 == apple_img:
                        Ran_goods2 = random.randint(1, apple)
                        All_price2 = Ran_goods2 * (apple_price + random.choice(Profit))
                    elif Ran_Stock2 == potato_img:
                        Ran_goods2 = random.randint(1, potato)
                        All_price2 = Ran_goods2 * (potato_price + random.choice(Profit))
                    elif Ran_Stock2 == stawberry_img:
                        Ran_goods2 = random.randint(1, stawberry)
                        All_price2 = Ran_goods2 * (stawberry_price + random.choice(Profit))

                    # elif Ran_Stock2 == sausage_img:
                    #     Ran_goods2 = random.randint(1, sausage)
                    #     All_price2 = Ran_goods2 * (sausage_price + random.choice(Profit))
                    # elif Ran_Stock2 == fish_img:
                    #     Ran_goods2 = random.randint(1, fish)
                    #     All_price2 = Ran_goods2 * (fish_price + random.choice(Profit))
                    # elif Ran_Stock2 == selmon_img:
                    #     Ran_goods2 = random.randint(1, selmon)
                    #     All_price2 = Ran_goods2 * (selmon_price + random.choice(Profit))
                    # elif Ran_Stock2 == bacon_img:
                    #     Ran_goods2 = random.randint(1, bacon)
                    #     All_price2 = Ran_goods2 * (bacon_price + random.choice(Profit))
                    # elif Ran_Stock2 == cow_img:
                    #     Ran_goods2 = random.randint(1, cow)
                    #     All_price2 = Ran_goods2 * (cow_price + random.choice(Profit))
                        
                    # elif Ran_Stock2 == water_img:
                    #     Ran_goods2 = random.randint(1, water)
                    #     All_price2 = Ran_goods2 * (water_price + random.choice(Profit))
                    # elif Ran_Stock2 == cola_img:
                    #     Ran_goods2 = random.randint(1, cola)
                    #     All_price2 = Ran_goods2 * (cola_price + random.choice(Profit))
                    # elif Ran_Stock2 == oil_img:
                    #     Ran_goods2 = random.randint(1, oil)
                    #     All_price2 = Ran_goods2 * (oil_price + random.choice(Profit))
                    # elif Ran_Stock2 == milk_img:
                    #     Ran_goods2 = random.randint(1, milk)
                    #     All_price2 = Ran_goods2 * (milk_price + random.choice(Profit))
                    # elif Ran_Stock2 == wine_img:
                    #     Ran_goods2 = random.randint(1, wine)
                    #     All_price2 = Ran_goods2 * (wine_price + random.choice(Profit))
                
                Profit_add += All_price 

                if len(InStock) > 1 :
                    Profit_add += All_price2 
                print(str(Profit_add))

                Number = ""

                while RanDow :
                    screen.blit(background, (0, 0))
                    screen.blit(botground, (0, 600))

                    text = font1.render(Number, True, WHITE)
                    screen.blit(text, (300,640))
                    x = font1.render("x", True, WHITE)
                    screen.blit(x, (100,665))
                    
                    
                    Cus_goods1 = font1.render(str(Ran_goods1), True, WHITE)
                    screen.blit(Cus_goods1, (130,665))
                    if len(InStock) > 1 :
                        screen.blit(x, (100,715))
                        Cus_goods2 = font1.render(str(Ran_goods2), True, WHITE)
                        screen.blit(Cus_goods2, (130,715))

                    screen.blit(font1.render(str(money), True, WHITE), (605,640))

                    if HP == 5 :
                        screen.blit(HP_5, (540,685))
                    elif HP == 4 :
                        screen.blit(HP_4, (540,685))
                    elif HP == 3 :
                        screen.blit(HP_3, (540,685))
                    elif HP == 2 :
                        screen.blit(HP_2, (540,685))
                    elif HP == 1 :
                        screen.blit(HP_1, (540,685))
                    elif HP == 0 :
                        screen.blit(HP_0, (540,685))
                    

                    Cus_choose()
                    for event in pygame.event.get():
                        print(event)

                        if event.type == pygame.QUIT:
                            RanDow = False
                                
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                Number = Number[:-1]
                        
                            if len(Number) < 9 :
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


                        if (event.type == pygame.MOUSEBUTTONDOWN and Button_Ark._is_hovered()) and len(Number) > 0:
                            if Button_Ark.goods_type == "Ark" :
                                Ark = 1
                                if int(Number) > Profit_add:
                                    Feel = "Bad"

                                if int(Number) <= Profit_add:
                                    Feel = "Good"
                                    
                                while Delay < 1000:
                                    if Feel == "Bad":
                                        Bott()
                                        __show()
                                        screen.blit(ANGRY, (190,220))
                                    if Feel == "Good":
                                        Bott()
                                        __show()
                                        screen.blit(GOOD, (190,220))
                                    pygame.display.flip()
                                    pygame.display.update()
                                        
                                    Delay +=1
                                Ark = 1
                                Feel = ""
                                Delay = 0



                        if (event.type == pygame.MOUSEBUTTONDOWN and Button_Sell._is_hovered()) and len(Number) > 0:
                            if Button_Sell.goods_type == "Sell" :

                                if int(Number) > Profit_add:
                                    HP -= 1
                                    stat = 5
                                    Feel = "Bad"

                                if int(Number) <= Profit_add:
                                    Feel = "Good"
                                    money += int(Number)
                                    HIGH_score += 1 

                                    if Ran_Stock == melon_img:
                                        melon -= Ran_goods1
                                    elif Ran_Stock == banana_img:
                                        banana -= Ran_goods1
                                    elif Ran_Stock == apple_img:
                                        apple -= Ran_goods1
                                    elif Ran_Stock == potato_img:
                                        potato -= Ran_goods1
                                    elif Ran_Stock == stawberry_img:
                                        stawberry -= Ran_goods1
                                    stat = 5
                                    
                                while Delay < 1000:
                                    if Feel == "Bad":
                                        Bott()
                                        __show()
                                        screen.blit(ANGRY, (190,220))
                                    if Feel == "Good":
                                        Bott()
                                        __show()
                                        screen.blit(GOOD, (190,220))
                                    pygame.display.flip()
                                    pygame.display.update()
                                        
                                    Delay +=1
                                RanDow = False
                                Delay = 0
                                Feel = ""
                                Number = "0"
                                
                    Bott()
                    __show()
                    
                    pygame.display.flip()
                    pygame.display.update()
    if len(InStock) < 1 and stat == 10:
        stat = 5


    Ark = 0
    RanDow = True


    ReroadScreen()
    # การเดินของตัวเรา
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

    

    # เช็คจำนวนรอบ ของลูกค้า
    if stat == 1: #เมื่อถึงจุดแรก
        Cut.move()
        if Cut.x == 500:
            stat = 2
    if stat == 2 : #เมื่อถึงหน้าตู้สินค้า
        Cut.move()       
        if Cut.y == 150:
            stat = 3
    if stat == 3 : #ให้เดินถอยกลับมาจุดที่กำหนด
        Cut.move()
        if Cut.y == 250:
            stat = 4
    if stat == 4 : #ให้เดินไปยังหน้าเครื่องคิดเงิน
        Cut.move()
        if Cut.x == 150:
            stat = 10
    if stat == 5 : #ให้เดินออกจากร้าน
        Cut.move()
        if Cut.y == 700:
            stat = 6
    if stat == 6 :
        Monster    = pygame.image.load(random.choice(Cus))
        Cut.x = 1000
        Cut.y = 400
        stat = 1
        if money >= 1100:
            print("you win")
            running = False
        if HP == 0 :
            print("you Lose")
            running = False
    #
    
    

pygame.quit()