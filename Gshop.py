import pygame
import random
FPS = 60
clock = pygame.time.Clock()
pygame.init()

VELOCITY = 5
Delay = 0



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

#ดึงรูปมาใช้
pink = pygame.image.load("img/Customer/ping/standL.png")
blue = pygame.image.load("img/Customer/blue/standL.png")
whith = pygame.image.load("img/Customer/whith/standL.png")

Cus = [pink,blue,whith]
# รูปตัวละครต่างๆ
PinkLeft = [pygame.image.load("img/Customer/ping/runL/1.png"),
            pygame.image.load("img/Customer/ping/runL/2.png"),
            pygame.image.load("img/Customer/ping/runL/3.png"),
            pygame.image.load("img/Customer/ping/runL/4.png"),
            pygame.image.load("img/Customer/ping/runL/5.png"),
            pygame.image.load("img/Customer/ping/runL/6.png")]

blueLeft = [pygame.image.load("img/Customer/blue/runL/1.png"),
            pygame.image.load("img/Customer/blue/runL/2.png"),
            pygame.image.load("img/Customer/blue/runL/3.png"),
            pygame.image.load("img/Customer/blue/runL/4.png"),
            pygame.image.load("img/Customer/blue/runL/5.png"),
            pygame.image.load("img/Customer/blue/runL/6.png")]

whithLeft = [pygame.image.load("img/Customer/whith/runL/1.png"),
            pygame.image.load("img/Customer/whith/runL/2.png"),
            pygame.image.load("img/Customer/whith/runL/3.png"),
            pygame.image.load("img/Customer/whith/runL/4.png"),
            pygame.image.load("img/Customer/whith/runL/5.png"),
            pygame.image.load("img/Customer/whith/runL/6.png")]

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

Menu_img = pygame.image.load("img/Home.png")
background = pygame.image.load("img/BG3.png")
botground  = pygame.image.load("img/botdown.png")
Show_price = pygame.image.load("img/Show_price2.png")
How_to_play = pygame.image.load("img/How_To.png")
background_BUY = pygame.image.load("img/sell1.png")
character = pygame.image.load("img/character/png/stand/standR/standR1.png")

Monster    = random.choice(Cus)
Walk = whithLeft
But_top = pygame.image.load('img/RL/RLtop.png')
But_down = pygame.image.load('img/RL/RLdown.png')
But_Buy = pygame.image.load('img/RL/Buy.png')
But_Exit = pygame.image.load('img/RL/Exit.png')

But_Exit_Menu = pygame.image.load('img/RL/Exit_menu.png')
But_Play_Menu = pygame.image.load('img/RL/Start.png')
But_Show_Menu = pygame.image.load('img/RL/Show_score.png')


But_Over = pygame.image.load('img/RL/GameOver.png')
But_Win = pygame.image.load('img/RL/You Win.png')
But_ReturnToMenu = pygame.image.load('img/RL/ReturnToMenu.png')

melon_img = pygame.image.load("img/goods/fr/melon.png")
banana_img = pygame.image.load("img/goods/fr/banana.png")
apple_img = pygame.image.load("img/goods/fr/apple.png")
potato_img = pygame.image.load("img/goods/fr/potato.png")
stawberry_img = pygame.image.load("img/goods/fr/strawberry.png")

sausage_img = pygame.image.load("img/goods/food/sausage_p.png")
fish_img = pygame.image.load("img/goods/food/fish.png")
selmon_img = pygame.image.load("img/goods/food/salmon.png")
bacon_img = pygame.image.load("img/goods/food/bacon.png")
cow_img = pygame.image.load("img/goods/food/cow.png")

water_img = pygame.image.load("img/goods/water/water.png")
cola_img = pygame.image.load("img/goods/water/soft_drink_red.png")
oil_img = pygame.image.load("img/goods/water/olive_oil.png")
milk_img = pygame.image.load("img/goods/water/milk_pack.png")
wine_img = pygame.image.load("img/goods/water/wine_red.png")

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

# กำหนดตัวอักษร
font1 = pygame.font.Font("Font/Baskic8-Bold.otf", 34)
font2 = pygame.font.Font("Font/Baskic8-Bold.otf", 18)
custom_font = pygame.font.Font('Font/THSarabun Italic.ttf', 32)

# เพลง
sound_Sell = pygame.mixer.Sound('Money.wav')
sound_Over = pygame.mixer.Sound('Game_Over_1.wav')
pygame.mixer.music.load('Sound_menu.wav')
pygame.mixer.music.play(-1, 0.0)

file1 = open('best_score.txt','r') #  ดึงไฟล์ HIGH Score .txt มาใช้

Ark = 0 # สถานะการถาม
Feel = "" # ความรู้สึก
money = 100 #จำนวนเงินเรื่มต้น
HP = 5 # เลือด

# การสุ่มจำนวนเงินกำไร
Profit1 = [5,10]
Profit2 = [25,50]
Profit3 = [100,200]

# ค่าไว้ทดการบวกลบของจำนวนเงิน
Profit_add = 0
All_price = 0
All_price2 = 0

HIGH_score = 0 # จำนวนลูกค้าที่ขายสินค้าให้


# จำนวนสินค้าต่างๆ
# # ผลไม้
melon = 0
melon_price = 10

banana = 0
banana_price = 10

apple = 0
apple_price = 50

potato = 0
potato_price = 100

stawberry = 0
stawberry_price = 200

# # เนื้อ
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

# # น้ำ
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


score_int =0 #ค่าที่ใช้เก็บค่าสูงสุดในไฟล์ .txt


InStock = [] # ระบุสินค้าในคลัง


#ขนาดของจอ กับ ชื่อ
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("My First GShop")
#สี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Button(): #ใช้สร้างปุ่มกดต่างๆ
    def __init__(self, x, y, image, goods_type , add_type): # (จุด x , จุด y, ใช้รูปภาพอะไร , ชนิด, ชนิดที่ 2,)
        self.image = image # กำหนดรูปภาพ
        self.rect = self.image.get_rect() # กำหนด hit block
        self.rect.topleft = (x, y) # กำหนดจุด x y 
        # กำหนดขนาดรูปภาพ
        self.size = (30,30) #
        if add_type == "Exit":
            self.size = (105,50)
        if add_type == "Exit_menu":
            self.size = (230,76)
        if add_type == "Ark":
            self.size = (80,38)
        if add_type == "Sell":
            self.size = (110,46)

        self.goods_type = goods_type # กำหนดชนิด
        self.add_type = add_type # กำหนดชนิด

    def _Show_(self): # แสดงรูปภาพ
        screen.blit(self.image, (self.rect.x ,self.rect.y))

    def _is_hovered(self): # ตรวจสอบการชี้ของ เมาล์ว่าเลือกอยู่หรือไม่
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

    def draw(self,event): # ใช้สร้างเงือนไขเมื่อกดโดนปุ่ม
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

            # เมื่อกดจะเกิดการทำงานต่างๆ (ลบสินค้า,เพิ่มสินค้า,ออก)
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

class Player(object): #ตัวละครของตัวเรา
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

class Customer (object): # ตัวละครลูกค้า
    def __init__(self, x, y, width, height):
        self.x = x # กำหนดแกน x 
        self.y = y # กำหนดแกน y
        self.width = width # กำหนดขนาดความกว้าง
        self.height = height # กำหนดขนาดความสูง
        self.velocity = 10 
        # กำหนดการเดิน ซ้าย หรือ ขวา
        self.left = False
        self.right = False
        self.walkCount = 0
    def draw(self, win):
        global Walk
        # ตรวจสอบว่าเป็นตัวละครใด
        if Monster == pink:
            Walk = PinkLeft
        if Monster == blue:
            Walk = blueLeft
        if Monster == whith:
            Walk = whithLeft
        # แสดงอนิเมชั่นการเดินของลูกค้า
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.left:
            win.blit(Walk[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            
        else:
            win.blit(Monster, (self.x, self.y))
    
    def move(self): #การเดินของ custommer
        # แบ่งเป็น stat เพื่อให้เข้าใจง่ายว่าอยู่ใน stat ไหน อธิบายเพิ่มใน whitl loop
        if stat == 1 :
            self.left = True
            self.x -= self.velocity
        elif stat == 2:
            self.left = True
            self.y -= self.velocity
        elif stat == 3:
            self.left = True
            self.y += self.velocity
        elif stat == 4:
            self.left = True
            self.x -= self.velocity
        elif stat == 5:
            self.left = True
            self.y += self.velocity

Number = "0" # ตัวเลขคิดเงิน


def Cus_choose(): #สร้างรูปภาพสินค้าตอนคิดเงิน
    # ดึงค่าตัวแปร จาก global
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
    # สร้างภาพสินค้าที่ 1 ขึ้นมา 
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
    
    elif Ran_Stock == sausage_img:
        screen.blit(sausage_img, (25, 640))
    elif Ran_Stock == fish_img:
        screen.blit(fish_img, (25, 640))
    elif Ran_Stock == selmon_img:
        screen.blit(selmon_img, (25, 640))
    elif Ran_Stock == bacon_img:
        screen.blit(bacon_img, (25, 640))
    elif Ran_Stock == cow_img:
        screen.blit(cow_img, (25, 640))

    elif Ran_Stock == water_img:
        screen.blit(water_img, (25, 640))
    elif Ran_Stock == cola_img:
        screen.blit(cola_img, (25, 640))
    elif Ran_Stock == oil_img:
        screen.blit(oil_img, (25, 640))
    elif Ran_Stock == milk_img:
        screen.blit(milk_img, (25, 640))
    elif Ran_Stock == wine_img:
        screen.blit(wine_img, (25, 640))


    if len(InStock) > 1 : # ถ้าหากมีสินค้าในคลังมากกว่า 1 จะแสดงเพิ่ม
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

        elif Ran_Stock2 == sausage_img:
            screen.blit(sausage_img, (25, 690))
        elif Ran_Stock2 == fish_img:
            screen.blit(fish_img, (25, 690))
        elif Ran_Stock2 == selmon_img:
            screen.blit(selmon_img, (25, 690))
        elif Ran_Stock2 == bacon_img:
            screen.blit(bacon_img, (25, 690))
        elif Ran_Stock2 == cow_img:
            screen.blit(cow_img, (25, 690))

        elif Ran_Stock2 == water_img:
            screen.blit(water_img, (25, 690))
        elif Ran_Stock2 == cola_img:
            screen.blit(cola_img, (25, 690))
        elif Ran_Stock2 == oil_img:
            screen.blit(oil_img, (25, 690))
        elif Ran_Stock2 == milk_img:
            screen.blit(milk_img, (25, 690))
        elif Ran_Stock2 == wine_img:
            screen.blit(wine_img, (25, 690))

def ADD_INS(): #ตรวจสอบสินค้าว่าเหลืออะไรบ้าง
    global InStock
    # หากมีสินค้าเพิ่ม จะทำการเพิ่มตัวแปรไปยัง Instock 
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
    
    if sausage > 0 :
        if InStock.count(sausage_img) == 0:
            InStock.append(sausage_img)
    elif sausage <= 0 :
        if InStock.count(sausage_img) > 0 :
            InStock.remove(sausage_img)
    if fish > 0 :
        if InStock.count(fish_img) == 0:
            InStock.append(fish_img)
    elif fish <= 0 :
        if InStock.count(fish_img) > 0 :
            InStock.remove(fish_img)
    if selmon > 0 :
        if InStock.count(selmon_img) == 0:
            InStock.append(selmon_img)
    elif selmon <= 0 :
        if InStock.count(selmon_img) > 0 :
            InStock.remove(selmon_img)
    if bacon > 0 :
        if InStock.count(bacon_img) == 0:
            InStock.append(bacon_img)
    elif bacon <= 0 :
        if InStock.count(bacon_img) > 0 :
            InStock.remove(bacon_img)
    if cow > 0 :
        if InStock.count(cow_img) == 0:
            InStock.append(cow_img)
    elif cow <= 0 :
        if InStock.count(cow_img) > 0 :
            InStock.remove(cow_img)

    if water > 0 :
        if InStock.count(water_img) == 0:
            InStock.append(water_img)
    elif water <= 0 :
        if InStock.count(water_img) > 0 :
            InStock.remove(water_img)
    if cola > 0 :
        if InStock.count(cola_img) == 0:
            InStock.append(cola_img)
    elif cola <= 0 :
        if InStock.count(cola_img) > 0 :
            InStock.remove(cola_img)
    if oil > 0 :
        if InStock.count(oil_img) == 0:
            InStock.append(oil_img)
    elif oil <= 0 :
        if InStock.count(oil_img) > 0 :
            InStock.remove(oil_img)
    if milk > 0 :
        if InStock.count(milk_img) == 0:
            InStock.append(milk_img)
    elif milk <= 0 :
        if InStock.count(milk_img) > 0 :
            InStock.remove(milk_img)
    if wine > 0 :
        if InStock.count(wine_img) == 0:
            InStock.append(wine_img)
    elif wine <= 0 :
        if InStock.count(wine_img) > 0 :
            InStock.remove(wine_img)

def Cal_price(): #คำนวนราคาต่างๆ
    global Profit_add
    global All_price
    global All_price2
    global Ran_Stock
    global Ran_Stock2
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
    # ทำการสุ่มราคาและบวกเข้ากับราคาเริ่มต้น หลังจากนั้นคูณเข้ากับจำนวนสุ่ม
    if Ran_Stock == melon_img:
        Ran_goods1 = random.randint(1, melon)
        All_price = Ran_goods1 * (melon_price + random.choice(Profit1))
    elif Ran_Stock == banana_img:
        Ran_goods1 = random.randint(1, banana)
        All_price = Ran_goods1 * (bacon_price + random.choice(Profit1))
    elif Ran_Stock == apple_img:
        Ran_goods1 = random.randint(1, apple)
        All_price = Ran_goods1 * (apple_price + random.choice(Profit2))
    elif Ran_Stock == potato_img:
        Ran_goods1 = random.randint(1, potato)
        All_price = Ran_goods1 * (potato_price + random.choice(Profit2))
    elif Ran_Stock == stawberry_img:
        Ran_goods1 = random.randint(1, stawberry)
        All_price = Ran_goods1 * (stawberry_price + random.choice(Profit3))

    elif Ran_Stock == sausage_img:
        Ran_goods1 = random.randint(1, sausage)
        All_price = Ran_goods1 * (sausage_price + random.choice(Profit1))
    elif Ran_Stock == fish_img:
        Ran_goods1 = random.randint(1, fish)
        All_price = Ran_goods1 * (fish_price + random.choice(Profit1))
    elif Ran_Stock == selmon_img:
        Ran_goods1 = random.randint(1, selmon)
        All_price = Ran_goods1 * (selmon_price + random.choice(Profit2))
    elif Ran_Stock == bacon_img:
        Ran_goods1 = random.randint(1, bacon)
        All_price = Ran_goods1 * (bacon_price + random.choice(Profit2))
    elif Ran_Stock == cow_img:
        Ran_goods1 = random.randint(1, cow)
        All_price = Ran_goods1 * (cow_price + random.choice(Profit3))

    elif Ran_Stock == water_img:
        Ran_goods1 = random.randint(1, water)
        All_price = Ran_goods1 * (water_price + random.choice(Profit1))
    elif Ran_Stock == cola_img:
        Ran_goods1 = random.randint(1, cola)
        All_price = Ran_goods1 * (cola_price + random.choice(Profit1))
    elif Ran_Stock == oil_img:
        Ran_goods1 = random.randint(1, oil)
        All_price = Ran_goods1 * (oil_price + random.choice(Profit2))
    elif Ran_Stock == milk_img:
        Ran_goods1 = random.randint(1, milk)
        All_price = Ran_goods1 * (milk_price + random.choice(Profit2))
    elif Ran_Stock == wine_img:
        Ran_goods1 = random.randint(1, wine)
        All_price = Ran_goods1 * (wine_price + random.choice(Profit3))


    

    if len(InStock) > 1 : # หากมีสินค้ามากกว่าหนึ่ง
        Ran_Stock2 = random.choice(InStock)
        if Ran_Stock == Ran_Stock2: # หากสุ่มได้ค่าเดียวกัน จะทำการสุ่มใหม่จนกว่าจะเจอค่าที่ไม่ซ้ำ
            while Nomore:
                Ran_Stock2 = random.choice(InStock)
                if Ran_Stock != Ran_Stock2:
                    if Ran_Stock2 == melon_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, melon)
                        All_price2 = Ran_goods2 * (melon_price + random.choice(Profit1))
                    elif Ran_Stock2 == banana_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, banana)
                        All_price2 = Ran_goods2 * (banana_price + random.choice(Profit1))
                    elif Ran_Stock2 == apple_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, apple)
                        All_price2 = Ran_goods2 * (apple_price + random.choice(Profit2))
                    elif Ran_Stock2 == potato_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, potato)
                        All_price2 = Ran_goods2 * (potato_price + random.choice(Profit2))
                    elif Ran_Stock2 == stawberry_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, stawberry)
                        All_price2 = Ran_goods2 * (stawberry_price + random.choice(Profit3))
                    
                    
                    elif Ran_Stock2 == sausage_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, sausage)
                        All_price2 = Ran_goods2 * (sausage_price + random.choice(Profit1))
                    elif Ran_Stock2 == fish_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, fish)
                        All_price2 = Ran_goods2 * (fish_price + random.choice(Profit1))
                    elif Ran_Stock2 == selmon_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, selmon)
                        All_price2 = Ran_goods2 * (selmon_price + random.choice(Profit2))
                    elif Ran_Stock2 == bacon_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, bacon)
                        All_price2 = Ran_goods2 * (bacon_price + random.choice(Profit2))
                    elif Ran_Stock2 == cow_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, cow)
                        All_price2 = Ran_goods2 * (cow_price + random.choice(Profit3))
                        
                    elif Ran_Stock2 == water_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, water)
                        All_price2 = Ran_goods2 * (water_price + random.choice(Profit1))
                    elif Ran_Stock2 == cola_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, cola)
                        All_price2 = Ran_goods2 * (cola_price + random.choice(Profit1))
                    elif Ran_Stock2 == oil_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, oil)
                        All_price2 = Ran_goods2 * (oil_price + random.choice(Profit2))
                    elif Ran_Stock2 == milk_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, milk)
                        All_price2 = Ran_goods2 * (milk_price + random.choice(Profit2))
                    elif Ran_Stock2 == wine_img and Ran_Stock != Ran_Stock2:
                        Ran_goods2 = random.randint(1, wine)
                        All_price2 = Ran_goods2 * (wine_price + random.choice(Profit3))
                    break

        elif Ran_Stock2 == melon_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, melon)
            All_price2 = Ran_goods2 * (melon_price + random.choice(Profit1))
        elif Ran_Stock2 == banana_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, banana)
            All_price2 = Ran_goods2 * (banana_price + random.choice(Profit1))
        elif Ran_Stock2 == apple_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, apple)
            All_price2 = Ran_goods2 * (apple_price + random.choice(Profit2))
        elif Ran_Stock2 == potato_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, potato)
            All_price2 = Ran_goods2 * (potato_price + random.choice(Profit2))
        elif Ran_Stock2 == stawberry_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, stawberry)
            All_price2 = Ran_goods2 * (stawberry_price + random.choice(Profit3))
        
        
        elif Ran_Stock2 == sausage_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, sausage)
            All_price2 = Ran_goods2 * (sausage_price + random.choice(Profit1))
        elif Ran_Stock2 == fish_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, fish)
            All_price2 = Ran_goods2 * (fish_price + random.choice(Profit1))
        elif Ran_Stock2 == selmon_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, selmon)
            All_price2 = Ran_goods2 * (selmon_price + random.choice(Profit2))
        elif Ran_Stock2 == bacon_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, bacon)
            All_price2 = Ran_goods2 * (bacon_price + random.choice(Profit2))
        elif Ran_Stock2 == cow_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, cow)
            All_price2 = Ran_goods2 * (cow_price + random.choice(Profit3))
            
        elif Ran_Stock2 == water_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, water)
            All_price2 = Ran_goods2 * (water_price + random.choice(Profit1))
        elif Ran_Stock2 == cola_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, cola)
            All_price2 = Ran_goods2 * (cola_price + random.choice(Profit1))
        elif Ran_Stock2 == oil_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, oil)
            All_price2 = Ran_goods2 * (oil_price + random.choice(Profit2))
        elif Ran_Stock2 == milk_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, milk)
            All_price2 = Ran_goods2 * (milk_price + random.choice(Profit2))
        elif Ran_Stock2 == wine_img and Ran_Stock != Ran_Stock2:
            Ran_goods2 = random.randint(1, wine)
            All_price2 = Ran_goods2 * (wine_price + random.choice(Profit3))
        
    Profit_add += All_price  # ทำการเพิ่มค่าสินค้า แรก เขาไปยัง Profit 

    if len(InStock) > 1 :
        Profit_add += All_price2 # ทำการเพิ่มค่าสินค้า สอง เขาไปยัง Profit 
    print(str(Profit_add))

def minus_goods(): # ลบสินค้าที่อยู่ในคลัง
    # ฟังชัน นี้จะลบตามจำนวน ค่าที่ Ran_stock มีอยู่
    global Profit_add
    global All_price
    global All_price2
    global Ran_Stock
    global Ran_Stock2
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
        melon -= Ran_goods1
    elif Ran_Stock == banana_img:
        banana -= Ran_goods1
    elif Ran_Stock == apple_img:
        apple -= Ran_goods1
    elif Ran_Stock == potato_img:
        potato -= Ran_goods1
    elif Ran_Stock == stawberry_img:
        stawberry -= Ran_goods1
    
    elif Ran_Stock == sausage_img:
        sausage -= Ran_goods1
    elif Ran_Stock == fish_img:
        fish -= Ran_goods1
    elif Ran_Stock == selmon_img:
        selmon -= Ran_goods1
    elif Ran_Stock == bacon_img:
        bacon -= Ran_goods1
    elif Ran_Stock == cow_img:
        cow -= Ran_goods1
    
    elif Ran_Stock == water_img:
        water -= Ran_goods1
    elif Ran_Stock == cola_img:
        cola -= Ran_goods1
    elif Ran_Stock == oil_img:
        oil -= Ran_goods1
    elif Ran_Stock == milk_img:
        milk -= Ran_goods1
    elif Ran_Stock == wine_img:
        wine -= Ran_goods1

    # ล่าง
    if len(InStock) > 1:
        if Ran_Stock2 == melon_img:
            melon -= Ran_goods2
        elif Ran_Stock2 == banana_img:
            banana -= Ran_goods2
        elif Ran_Stock2 == apple_img:
            apple -= Ran_goods2
        elif Ran_Stock2 == potato_img:
            potato -= Ran_goods2
        elif Ran_Stock2 == stawberry_img:
            stawberry -= Ran_goods2
        
        elif Ran_Stock2 == sausage_img:
            sausage -= Ran_goods2
        elif Ran_Stock2 == fish_img:
            fish -= Ran_goods2
        elif Ran_Stock2 == selmon_img:
            selmon -= Ran_goods2
        elif Ran_Stock2 == bacon_img:
            bacon -= Ran_goods2
        elif Ran_Stock2 == cow_img:
            cow -= Ran_goods2
        
        elif Ran_Stock2 == water_img:
            water -= Ran_goods2
        elif Ran_Stock2 == cola_img:
            cola -= Ran_goods2
        elif Ran_Stock2 == oil_img:
            oil -= Ran_goods2
        elif Ran_Stock2 == milk_img:
            milk -= Ran_goods2
        elif Ran_Stock2 == wine_img:
            wine -= Ran_goods2

def __Show_sell(): # แสดงภาพหน้าจอตอนขายของ
    man.draw(screen)
    Cut.draw(screen)
    screen.blit(Show_price, (330, 40))
    # แสดงข้อความบนหน้าจอ
    screen.blit(font1.render(str(HIGH_score), True, BLACK), (75,75))
    Button_Sell._Show_()

    if Ark == 0: # ถ้าหากมี Ark ค่าไม่ตรง จะไม่แสดงรูป
        Button_Ark._Show_()

def But_SellandArk(): #สถานะการกดปุ่ม Ark
    Button_Sell.draw(event) # ส่งค่า event ไปยัง class Button
    if Ark == 0: # ถ้าหากมี Ark ค่าไม่ตรง จะไม่ส่ง event 
        Button_Ark.draw(event)

def reload_s(): # แสดงจำนวนสินค้าบนหน้าจอ
    # ผลไม้
    # Bott()
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
    __show()
    
    pygame.display.flip()
    pygame.display.update()

def __show(): # แสดงภาพสินค้าบนหน้าจอ
    #ผลไม้
    Button_top_melon._Show_()
    Button_down_melon._Show_()

    Button_top_banana._Show_()
    Button_down_banana._Show_()

    Button_top_apple._Show_()
    Button_down_apple._Show_()

    Button_top_potato._Show_()
    Button_down_potato._Show_()

    Button_top_stawberry._Show_()
    Button_down_stawberry._Show_()

    # เนื้อ
    Button_top_sausage._Show_()
    Button_down_sausage._Show_()

    Button_top_fish._Show_()
    Button_down_fish._Show_()

    Button_top_selmon._Show_()
    Button_down_selmon._Show_()

    Button_top_bacon._Show_()
    Button_down_bacon._Show_()

    Button_top_cow._Show_()
    Button_down_cow._Show_()
    
    # น้ำ
    Button_top_water._Show_()
    Button_down_water._Show_()

    Button_top_cola._Show_()
    Button_down_cola._Show_()

    Button_top_oil._Show_()
    Button_down_oil._Show_()

    Button_top_milk._Show_()
    Button_down_milk._Show_()

    Button_top_wine._Show_()
    Button_down_wine._Show_()

    Button_Exit._Show_()
    # Button_Buy._Show_()

def Bott(): # ตรวจสอบการกดใช้งาน ของการเพิ่มสินค้า
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



    
    # Button_Exit.draw(event)
    # Button_Buy.draw(event)

def set_zero(): # เซ็ดค่าเกมส์ใหม่ เมื่อเรียกใช้งาน
    global HIGH_score 
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
    global HP
    HP = 5
    HIGH_score = 0
    money = 100
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
    
def Key_mon(): # การรับค่าจากคียืบอร์ด
    global Number
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

def ReroadScreen(): # อัพเดทจอตอนอยุ่ใรร้าน
    screen.blit(background, (0, 0))
    # วาดภาพตัวละคร โดยเรียกใช้ class cuttomber และ player 
    man.draw(screen)
    Cut.draw(screen)
    
    screen.blit(botground, (0, 600))
    
    text = font1.render(Number, True, WHITE)
    screen.blit(text, (300,640))
    screen.blit(font1.render(str(money), True, WHITE), (605,640)) # แสดงค่าบนหน้าจอ
    screen.blit(font1.render(str(HIGH_score), True, BLACK), (75,75)) # แสดงค่าบนหน้าจอ
     # แสดงเลือดบนหน้าจอ โดยดูจาก HP ว่ามีค่าเท่าไร
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

def Menu_reset():# อัพเดทจอหน้า เมนู
    global score_int
    screen.blit(Menu_img, (0, 0))
    # แสดงค่าปุ่มต่างๆ
    Button_Exit_menu._Show_()
    Button_Play_menu._Show_()
    Button_Show_menu._Show_()

    for score in file1:  # ดึงค่าจากไฟล์ .txt
        score_int = int(score)
    # ใช้ค่าที่ดึงมากจาก .txt มาแสดงบนหน้าจอ
    nowtime = (f'BEST score IS {str(score_int)}')      
    screen.blit(font1.render(nowtime, True, WHITE), (50,45))

    NameGame = "My First GShop"
    screen.blit(font1.render(NameGame, True, WHITE), (460, 435))
    Mynameis = ("64015048 นาย ตะวัน มณีรัตน์ ")      
    screen.blit(custom_font.render(Mynameis, True, WHITE), (460, 475))
    pygame.display.flip()
    pygame.display.update()

def Show_HIGHSCORE(): # แสดง และ บันทึก คะแนน
    global score_int
    global file1
    for score in file1: # ดึงค่าจากไฟล์ .txt
        score_int = int(score)
    # ใช้ค่าที่ดึงมากจาก .txt มาแสดงบนหน้าจอ
    if HIGH_score <= score_int: # ถ้าหาก HIGH_score น้อยกว่า ค่าที่มีในไฟล์ แสดงข้อความ New score

        New_score = ("You New Score")
        nowtime = (f'You End with {str(HIGH_score)} customer')
        
        screen.blit(font1.render(New_score, True, BLACK), (270,390))
        screen.blit(font2.render(nowtime, True, BLACK), (290,440))
        
    if HIGH_score > score_int: # ถ้าหาก HIGH_score มากกว่า ค่าที่มีในไฟล์ จะแสดง score ในรอบนั้น และแสดง score สูงสุด
        nowtime = (f'You End with {str(HIGH_score)} customer')
        Lasttime = (f'But Best Sell is {str(score_int)} customer')
        Fighting = ("Fighting Next Time")
        screen.blit(font2.render(nowtime, True, BLACK), (280,400))
        screen.blit(font2.render(Lasttime, True, BLACK), (265,440))
        screen.blit(font2.render(Fighting, True, BLACK), (320,480))


# หลังจากนี้เป็นการกำหนดค่า ของปุ่มต่างๆ
########################################################################################

# กำหนดค่าโดยใช้ Class Button ทั้งหมด
Button_Sell = Button(650, 725, But_Sell, "Sell", "Sell") 
Button_Ark = Button(550, 730, But_Ark, "Ark", "Ark")

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

Button_Exit = Button(350, 515, But_Exit, "Exit", "Exit")

Button_Show_menu = Button(450, 595, But_Show_Menu, "Exit_menu", "Exit_menu")
Button_Play_menu = Button(330, 695, But_Play_Menu, "Exit_menu", "Exit_menu")
Button_Exit_menu = Button(570, 695, But_Exit_Menu, "Exit_menu", "Exit_menu")

Button_ReturnToMenu_menu = Button(290, 300, But_ReturnToMenu, "Exit_menu", "Exit_menu")
Button_ReturnToMenu_menu2 = Button(50, 50, But_ReturnToMenu, "Exit_menu", "Exit_menu")
Button_Over_menu = Button(200, 150, But_Over, "Exit_menu", "Exit_menu")
Button_Win_menu = Button(200, 150, But_Win, "Exit_menu", "Exit_menu")
########################################################################################
# กำหนดค่าของ ตัวละคร
man = Player(150, 111, 64, 64)
Cut = Customer(1000, 400, 64, 64)
# สถานะของ loop ต่างๆ
running = False
stat = 1 # สถานะ ของการเดินลูกค้า
RanDow = True
Nomore = True

How = True
Menu = True
Lose = True
Win = True


# Main หลัก
while Menu:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and  Button_Play_menu._is_hovered() : # เมื่อมรการกดปุ่ม จะเริ่มเกมส์
            if Button_Play_menu.goods_type == "Exit_menu":
                running = True
                Menu = False
                
                while running:
                    clock.tick(30)
                    ADD_INS()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                                
                        if event.type == pygame.KEYDOWN: # พิมพ์ตัวเลขลงบนเครืองคิดเลข
                            if event.key == pygame.K_BACKSPACE:
                                Number = Number[:-1]
                            Key_mon()
                    


                    keys = pygame.key.get_pressed()
                    # การขยับของฮิตบล็อค
                    if keys[pygame.K_LEFT] and YOU_HIT_ract.left > 40:
                        YOU_HIT_ract.x -= VELOCITY
                    if keys[pygame.K_RIGHT] and YOU_HIT_ract.right < 380:
                        YOU_HIT_ract.x += VELOCITY

                    elif YOU_HIT_ract.colliderect(BUY_HIT_ract) : # เพิ่ม/ลด สินค้า
                        ########################################################################################
                                                        #ส่วนนี้เพิ่มสินค้าลดสินค้า
                        ########################################################################################
                        if keys[pygame.K_SPACE]: #เมื่อชนกับฮิตบล็อค และกด space จะทำให้ loop run ทำงาน
                            run = True
                            while run:
                                clock.tick(20)
                                # ดึงภาพออกมาแสดง + ข้อความ
                                screen.blit(background, (0, 0))
                                screen.blit(background_BUY, (0, 0))
                                screen.blit(botground, (0, 600))
                                screen.blit(font1.render(str(money), True, WHITE), (605,645))


                                
                                for event in pygame.event.get():
                                    Bott()
                                    if event.type == pygame.MOUSEBUTTONDOWN and  Button_Exit._is_hovered() : # เมื่อกด loop จะหยุดทำงาน
                                        
                                        if  Button_Exit.goods_type == "Exit":
                                            
                                            run = False
                                            
                                            print("1")
                                    
                                reload_s()
                        ########################################################################################



                    if YOU_HIT_ract.colliderect(ORDER_HIT_ract): #เมื่อชนกับฮิตบล็อค
                        if len(InStock) > 0 :
                            if (keys[pygame.K_SPACE] and stat == 10) and keys != keys[pygame.K_LEFT] : #เมื่อกด Spacebar พร้อมกับลูกค้ามีค่า stat=10  loop Randow จะทำงาน
                                man.right = False
                                man.left = False
                                man.walkCount = 0

                                Ran_Stock = random.choice(InStock) #สุ่มค่าให้กับ Ran_Stock
                                
                                Cal_price() #เรียกใช้งานฟังชัน
                                
                                Number = "" 
                                ########################################################################################
                                #                                   เริ่มต้น loop คิดงาน
                                ########################################################################################
                                while RanDow : # การคิดคำนวนเงิน
                                    # ดึงภาพออกมาแสดง + ข้อความ
                                    screen.blit(background, (0, 0))
                                    screen.blit(botground, (0, 600))

                                    
                                    text = font1.render(Number, True, WHITE)
                                    screen.blit(text, (300,640))
                                    x = font1.render("x", True, WHITE)
                                    screen.blit(x, (100,665))
                                    
                                    # แสดงจำนวนสินค้า
                                    Cus_goods1 = font1.render(str(Ran_goods1), True, WHITE)
                                    screen.blit(Cus_goods1, (130,665))
                                    if len(InStock) > 1 : #ถ้าหากมีสินค้ามากกว่า 2 ชิ้น
                                        screen.blit(x, (100,715))
                                        Cus_goods2 = font1.render(str(Ran_goods2), True, WHITE)
                                        screen.blit(Cus_goods2, (130,715))

                                    screen.blit(font1.render(str(money), True, WHITE), (605,640))

                                    # แสดงสถานะเลือด ตามค่า HP 
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
                                    
                                    Cus_choose() # แสดงรูปออกบนหน้าจอ

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            RanDow = False
                                                
                                        if event.type == pygame.KEYDOWN: # พิมพ์ตัวเลขลงบนจอ
                                            if event.key == pygame.K_BACKSPACE:
                                                Number = Number[:-1]
                                            Key_mon()

                                        # เมื่อกดปุ่ม Ark
                                        if Ark == 0 : # ถ้าหาก Ark มีค่าเท่าหนึ่ง
                                            if (event.type == pygame.MOUSEBUTTONDOWN and Button_Ark._is_hovered()) and len(Number) > 0: # จะกดปุ่มได้ก้ต่อเมือมีค่า Number หากไม่มีจะไม่แสดง
                                                if Button_Ark.goods_type == "Ark" : 
                                                    Ark = 1
                                                    # ตรวจสอบสถานะ หากมีค่าอยู่ใน ขอบเขต Profit_add จะเป็น Good ถ้าไม่จะเป็น Bad
                                                    if int(Number) > Profit_add:
                                                        Feel = "Bad"

                                                    if int(Number) <= Profit_add:
                                                        Feel = "Good"
                                                        
                                                        
                                                    while Delay < 100: # สร้างdelay เพื่อแสดง
                                                        # ตรวจสอบ สถานะ Feel ว่าเป้นอะไรและแสดงสถานะ
                                                        if Feel == "Bad":
                                                            But_SellandArk() # สถานะ Ark
                                                            __Show_sell()# แสดงภาพหน้าจอตอนขายของ
                                                            screen.blit(ANGRY, (190,220))
                                                        if Feel == "Good":
                                                            But_SellandArk() # สถานะ Ark
                                                            __Show_sell()# แสดงภาพหน้าจอตอนขายของ
                                                            screen.blit(GOOD, (190,220))
                                                        pygame.display.flip()
                                                        pygame.display.update()
                                                            
                                                        Delay +=1
                                                    # เซ็ตค่าเมื่อมี loop เสร็จ
                                                    Ark = 1
                                                    Feel = ""
                                                    Delay = 0


                                        # เมื่อกดปุ่ม Sell
                                        if ((event.type == pygame.MOUSEBUTTONDOWN and Button_Sell._is_hovered()) and len(Number) > 0):
                                            if Button_Sell.goods_type == "Sell" :
                                                
                                                if int(Number) > Profit_add:
                                                    # เลือดลดลง 1 เมือ ค่าเกินขอบเขต Profit_add ที่คำนวนมาก และปรับ stat เป็น 5
                                                    HP -= 1
                                                    stat = 5
                                                    Feel = "Bad"

                                                if int(Number) <= Profit_add:
                                                    # หากอยู่ในขอบเขต
                                                    Feel = "Good"
                                                    money += int(Number) # เพิ่มเงินเข้าไปใน money
                                                    HIGH_score += 1 # เพิ่ม คะแนนไป 1
                                                    sound_Sell.play() # เล่นเสียงเพลง
                                                    minus_goods() # เรียกใช้ฟังชั่น เพื่อลบจำนวนสินค้าที่ขายออกไป
                                                    stat = 5 # ปรับ stat ลูกค้า เป็น 5
                                                    
                                                while Delay < 100:# สร้างdelay เพื่อแสดง
                                                    # ตรวจสอบ สถานะ Feel ว่าเป้นอะไรและแสดงสถานะ
                                                    if Feel == "Bad":
                                                        But_SellandArk() # สถานะ Ark
                                                        __Show_sell() # แสดงภาพหน้าจอตอนขายของ
                                                        screen.blit(ANGRY, (190,220))
                                                    if Feel == "Good":
                                                        But_SellandArk()# สถานะ Ark
                                                        __Show_sell() # แสดงภาพหน้าจอตอนขายของ
                                                        screen.blit(GOOD, (190,220))
                                                    pygame.display.flip()
                                                    pygame.display.update()
                                                        
                                                    Delay +=1
                                                RanDow = False# หยุด loop
                                                # เซ็ตค่าใหม่
                                                Delay = 0
                                                Feel = ""
                                                Number = "0"
                                        
                                                
                                    But_SellandArk()# สถานะ Ark
                                    __Show_sell() # แสดงภาพหน้าจอตอนขายของ
                                    
                                    pygame.display.flip()
                                    pygame.display.update()
                                ########################################################################################
                    
                    if len(InStock) < 1 and stat == 10: # สถานะการขยับการเดินของลูกค้า
                        stat = 5

                    # เซ็ตค่าขึ้นมาใหม่
                    Profit_add = 0
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
                        if Cut.x == 470:
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
                        if Cut.x == 120:
                            Cut.left = False
                            stat = 10
                    if stat == 5 : #ให้เดินออกจากร้าน
                        Cut.move()
                        if Cut.y == 700:
                            stat = 6
                    if stat == 6 : # เริ่มที่จุดเริ่มต้นใหม่
                        Monster    = random.choice(Cus) #สุ่มตัวละครใหม่
                        Cut.x = 1000
                        Cut.y = 400
                        stat = 1

                        if money >= 1000: #จะชนะเมื่อเงินถึง 1000
                            if HIGH_score <= score_int: #เซ็ตค่าถ้าหาก score น้อยกว่า ค่าเก่า
                                file2 = open('best_score.txt','w')
                                file2.write(str(HIGH_score))
                                file2.close
                            while Win:
                                for event in pygame.event.get():
                                    print(event)
                                    if event.type == pygame.MOUSEBUTTONDOWN and  Button_ReturnToMenu_menu._is_hovered() : # กดเพื่อกลับหน้า menu
                                        if Button_ReturnToMenu_menu.goods_type == "Exit_menu":
                                            set_zero() # เซ็ตค่าใหม่ของเกมส์ใหม่ดดยใช้ฟังชั่น
                                            Menu = True
                                            running = False
                                            Win = False
                                            
                                            
                                
                                Button_Win_menu._Show_()
                                Button_ReturnToMenu_menu._Show_()
                                Show_HIGHSCORE()
                                pygame.display.flip()
                                pygame.display.update()
                            Win = True

                        elif (HP == 0) or (money == 0 and len(InStock)  == 0) : # จะแพ้เมื่อ
                            sound_Over.play() #เล่นเสียงเพลง
                            while Lose:
                                for event in pygame.event.get():
                                    print(event)

                                    if event.type == pygame.MOUSEBUTTONDOWN and  Button_ReturnToMenu_menu._is_hovered() : # กดเพื่อกลับหน้า menu
                                        if Button_ReturnToMenu_menu.goods_type == "Exit_menu":
                                            set_zero() # เซ็ตค่าใหม่ของเกมส์ใหม่ดดยใช้ฟังชั่น
                                            Menu = True
                                            running = False
                                            Lose = False
                                            
                                Button_Over_menu._Show_()
                                Button_ReturnToMenu_menu._Show_()
                                pygame.display.flip()
                                pygame.display.update()
                            Lose = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and  Button_Show_menu._is_hovered() : #แสดงวิธีการเล่น
            if Button_Show_menu.goods_type == "Exit_menu":
                Menu = False
                while How:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and  Button_ReturnToMenu_menu2._is_hovered() :# กดเพื่อกลับหน้า menu
                            if Button_ReturnToMenu_menu2.goods_type == "Exit_menu":
                                
                                How = False
                                Menu = True
                            
                    

                    screen.blit(How_to_play, (0, 0))
                    Button_ReturnToMenu_menu2._Show_()
                    pygame.display.flip()
                    pygame.display.update()
                

        if event.type == pygame.MOUSEBUTTONDOWN and  Button_Exit_menu._is_hovered() : #กดเพื่อ ออกจากเกมส์
            if Button_Exit_menu.goods_type == "Exit_menu":
                Menu = False
        How = True
    
    Menu_reset() #ทำการแสดงภาพโดยใช้ฟังชั่น

file1.close
pygame.quit()