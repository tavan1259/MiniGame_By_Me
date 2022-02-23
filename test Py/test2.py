import pygame
import random
FPS = 60
clock = pygame.time.Clock()
pygame.init()

# pink = pygame.image.load("img/Customer/ping/standL.png")
# blue = pygame.image.load("img/Customer/blue/standL.png")
# whith = pygame.image.load("img/Customer/whith/standL.png")

# Cus = [pink,blue,whith]

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
#ดึงรูปมา

Walk = whithLeft

background = pygame.image.load("img/BG3.png")
botground  = pygame.image.load("img/botdown.png")
character = pygame.image.load("img/character/png/stand/standR/standR1.png")


# Monster    = random.choice(Cus)

#ขนาดของจอ กับ ชื่อ
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("Test")
#สี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
        # global Walk
        

        # if self.walkCount + 1 >= 18:
        #     self.walkCount = 0

        # if self.left:
            
        #     win.blit(Walk[self.walkCount // 3], (self.x, self.y))
        #     self.walkCount += 1
            
        # else:
        #     win.blit(Monster, (self.x, self.y))
    #การเดินของ custommer
    def move(self):
        
        # if stat == 1 :
        #     self.left = True
        #     self.x -= self.velocity
        # elif stat == 2:
        #     self.left = True
        #     self.y -= self.velocity
        # elif stat == 3:
        #     self.left = True
        #     self.y += self.velocity
        # elif stat == 4:
        #     self.left = True
        #     self.x -= self.velocity
        # elif stat == 5:
        #     self.left = True
        #     self.y += self.velocity

Number = "0"
font1 = pygame.font.Font("Font/Baskic8-Bold.otf", 34)


#อัพเดทจอ
def ReroadScreen():
    screen.blit(background, (0, 0))
    man.draw(screen)
    Cut.draw(screen)
    screen.blit(botground, (0, 600))
    text = font1.render(Number, True, WHITE)
    screen.blit(text, (300,640))
    pygame.display.flip()
    pygame.display.update()
    

man = Player(150, 111, 64, 64)
Cut = Customer(1000, 400, 64, 64)
running = True
stat = 1
while running:
    if Monster == pink:
        Walk = PinkLeft
    if Monster == blue:
        Walk = blueLeft
    if Monster == whith:
        Walk = whithLeft
    print(Monster)
    print(pink)
    print(blue)
    print(whith)
    clock.tick(27)
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
    # if stat == 1: #เมื่อถึงจุดแรก
    #     Cut.move()
    #     if Cut.x == 470:
    #         stat = 2
    # if stat == 2 : #เมื่อถึงหน้าตู้สินค้า
    #     Cut.move()       
    #     if Cut.y == 150:
    #         stat = 3
    # if stat == 3 : #ให้เดินถอยกลับมาจุดที่กำหนด
    #     Cut.move()
    #     if Cut.y == 250:
    #         stat = 4
    # if stat == 4 : #ให้เดินไปยังหน้าเครื่องคิดเงิน
    #     Cut.move()
    #     if Cut.x == 120:
    #         stat = 5
    # if stat == 5 : #ให้เดินออกจากร้าน
    #     Cut.move()
    #     if Cut.y == 700:
    #         stat = 6
    # if stat == 6 :
    #     Monster    = random.choice(Cus)
    #     Cut.x = 1000
    #     Cut.y = 400
    #     stat = 1
    #
    
    
    ReroadScreen()

pygame.quit()