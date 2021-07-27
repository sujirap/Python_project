import pygame
import time
import random
pygame.init()
pygame.mixer.init()
best = 0
width = 1000
height = 500
window = pygame.display.set_mode((564,870))
pygame.display.set_caption("ZOMBIE GAME")

interphase = pygame.display.set_mode((564,870))

bg = [pygame.image.load('zompok.jpg'),pygame.image.load('zompok.jpg'),pygame.image.load('zompok.jpg'),pygame.image.load('zompok.jpg'),pygame.image.load('zompok1.jpg'),pygame.image.load('zompok1.jpg'),pygame.image.load('zompok1.jpg'),pygame.image.load('zompok1.jpg')]
zombie = [pygame.image.load('zb.png'),pygame.image.load('zb1.png'),pygame.image.load('zb2.png')]
heart  = [pygame.image.load('Hp1.png'),pygame.image.load('Hp2.png'),pygame.image.load('Hp3.png'),pygame.image.load('Hp4.png'),pygame.image.load('Hp5.png'),pygame.image.load('Hp6.png')] 
thing = pygame.image.load('organ1.gif')
thing2 = pygame.image.load('organ2.gif')
thing3 = pygame.image.load('organ3.gif')
thing4 = pygame.image.load('organ4.gif')
thing5 = pygame.image.load('organ5.gif')
thing6 = pygame.image.load('organ6.gif')
thing7 = pygame.image.load('organ7.gif')
thing8 = pygame.image.load('gsy.png')
bgplay = pygame.image.load('wall.jpg')
bghowto = pygame.image.load('howto2.jpg')
go = pygame.image.load('go2.jpg')
gameover = pygame.display.set_mode((564,870))
how_to_play = pygame.display.set_mode((564,870))
clock = time.clock()
button_sound = pygame.mixer.Sound('button-3.1.wav')
Death = pygame.mixer.Sound('Zombie Death.wav')




play = True

class falleiei(object):
    def __init__(self):
        self.d = random.choice([0,1,2,3,4,5,6,7,7,0,1,2,3,4,5,6,7,7])   
        
        self.y = 0
        self.uu = random.choice([50,150,250,350,450])
        self.x = self.uu
    def draw(self,window):
        
        if self.d == 0:
            window.blit(thing,(self.x,self.y))
        if self.d == 1:
            window.blit(thing2,(self.x,self.y))
        if self.d == 2:
            window.blit(thing3,(self.x,self.y))
        if self.d == 3:
            window.blit(thing4,(self.x,self.y)) 
        if self.d == 4:
            window.blit(thing5,(self.x,self.y)) 
        if self.d == 5:
            window.blit(thing6,(self.x,self.y)) 
        if self.d == 6:
            window.blit(thing7,(self.x,self.y))
        if self.d == 7:
            window.blit(thing8,(self.x,self.y)) 
        self.move()
    def move(self):
        self.y += 5
over = True
    
how = True
inf = True
run = True
while play:
    pygame.mixer.music.load('CHALLENGE.mp3')
    pygame.mixer.music.play(-1)
    
    score = 0
    x = 50
    y = 700
    width_cha = 40
    height_cha = 60
    vel = 20
    
    
    c= 0
    v = 0
    fall = []
    life = 0
    size = 1      
    while inf :
        
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inf = False
                run = False
                over = False  
                how = False
                pygame.quit()
                
        time.clock
        interphase.blit(bg[c%8],(0,0))
        c+=1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            pygame.mixer.Sound.play(button_sound)

            inf = False
            
            pygame.time.delay(100)
        print(c)
        pygame.display.update()
    
    c = 0
    while how:
        how_to_play.blit(bghowto,(0,0))
        c += 1
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                how = False 
                run = False
                over = False  
                        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            pygame.mixer.Sound.play(button_sound)
            how = False  
            pygame.time.delay(100)    
            
        pygame.display.update()
    
    c=0

    while run:
        window.blit(bgplay,(0,0)) 
        c += 1
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                over = False    
                
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 510 - width_cha - vel:
            x += vel
            
        if(size == 1):
            window.blit(zombie[0],(x,y))    
        if(size == 2):
            window.blit(zombie[1],(x,y-30))    
        if(size == 3):
            window.blit(zombie[2],(x,y-70))    
            
        if(score >=60):
            size = 3
        elif(score >=20):
            size = 2
        else :
            size = 1
        v+=1
        if v < 300:
            if v% 100 == 0 :
                fall.append(falleiei())
            if v > 50:
                for ee in fall:
                    ee.draw(window)
        if v > 300:
            if v% 80 == 0 :
                fall.append(falleiei())
        
                
      
        print(score)
        for ee in fall:
            ee.draw(window)
            
            if ee.y > 600 and ee.y < 700 and ee.x > x - 100 and ee.x < x + 100:
                if size == 1:
                    if ee.d == 4 or ee.d == 6:
                        score+= 2  
                    elif ee.d == 7:
                        life+=1
                    else:
                        score -= 2
                if size == 2:
                    if ee.d == 1 or ee.d == 3:
                        score+= 3         
                    elif ee.d == 7:
                        life+=1
                    else:
                        score -= 3
                if size == 3:
                    if ee.d == 2 or ee.d == 5 or ee.d == 6:
                        score+= 5      
                    elif ee.d == 7:
                        life+=1
                    else:
                        score -= 5      
               
                
                fall.remove(ee)
            if ee.y > 1000 :
                fall.remove(ee)
        if life == 5:
            pygame.mixer.Sound.play(Death)
            pygame.mixer.music.stop()
            run = False
            over = True
        window.blit(heart[life],(-10,0))
        font = pygame.font.SysFont('comicsans',48)
        text = font.render('Score: '+ str(score ),1,(176,48,96))
        window.blit(text,(400,50))
        pygame.display.update()
    end = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                over = False   
                play = False
                
        
        keys = pygame.key.get_pressed()
        font = pygame.font.SysFont('comicsans',48)
        gameover.blit(go,(0,0))
        if best < score:
            best = score
        text = font.render('BEST Score: '+ str(best ),1,(0,0,0))
        window.blit(text,(160,250))
        if keys[pygame.K_s] and end:
            pygame.mixer.Sound.play(button_sound)
           
            print("2")
            
            score = 0
            over = False
            
            inf = False
          
            how = False
        
            run = True
            end = False
        pygame.display.update()
       
pygame.quit()