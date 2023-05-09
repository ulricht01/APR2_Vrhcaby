import sys, pygame, random, pygame_widgets, lance, os, json
from pygame_widgets.button import Button

pygame.init()
pygame.font.init()

class Hra:
    def __init__(self) -> None:
        self.file_path = './file.json'
        check_file = os.path.isfile(self.file_path)
        """if(check_file):
            print('FILE EXIST!')
        else:
            print('FILE NOT EXIST!')"""
        self.dvojkoskta = Dvojkostka()
        self.bar = Bar()
        volba = input("Budeš hrát s hráčem (1), nebo s AI (0)?")
        if volba == "1":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, "Bila")
            hrac2 = input("Jméno hráče 2: ")
            self.Hrac2 = KonzolovyHrac(hrac2, "Cerna")
        elif volba == "0":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, "Bila")
            hrac2 = input("Jméno Ai 1: ")
            self.Hrac2 = AiHrac(hrac2, "Cerna")
        self.plocha = HerniPole()

    def Ulozit(self) -> None:
        data = {
            'Bily': self.bar.pocet_zetonu_bila_cil,
            'Cerny': self.bar.pocet_zetonu_cerna_cil,
            'Player1': {
                'Jmeno': self.Hrac1.jmeno,
                'Barva': self.Hrac1.barva,
                'Score': self.bar.pocet_zetonu_bila_cil,
               # 'Pole': self.Hrac1.policko 
            },
            'Player2': {
                'Jmeno': self.Hrac2.jmeno,
                'Barva': self.Hrac2.barva,
                'Score': self.bar.pocet_zetonu_cerna_cil,
               # 'Pole': self.Hrac2.policko 
            }
        }
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
    

class HerniPole:
    def __init__(self) -> None:
        self.sirka = 1450
        self.vyska = 1000
        self.obraz = pygame.display.set_mode((self.sirka,self.vyska))
        self.obraz.fill((255,155,50))
        
        rect = pygame.Rect(1220, 0, 280, 1000)
        black = (0,0,0)
        pygame.draw.rect(self.obraz, black, rect)
        
        white = (255,255,255)
        red = (255, 0, 0)
        blue = (0, 0, 255)
        font = pygame.font.SysFont("Arial", 15)
        #player1name = (""+str(self.Hrac1))
        #player2name = (""+str(self.Hrac2))
        #current_player = 1
        #if current_player == 1:
        #    text_color = red
        #    current_player_name = player1name
        #else:
        #    text_color = blue
        #    current_player_name = player2name

        text_surface = font.render("Na tahu je hráč:" +str(Hrac), True, white)
        text_rect = text_surface.get_rect()
        text_rect.center = (1350, 500)
        self.obraz.blit(text_surface, text_rect)

        self.tlacitko_hod = Button(self.obraz, 
                                   1290, 
                                   750, 
                                   100, 
                                   80,
                                   padding=20,
                                   text='Hod Kostkami',
                                   onClick=lambda: new.dvojkoskta.hod_kostkou())
        
        self.ulozit_tlacitko = Button(self.obraz, 
                                      1290,
                                      110,
                                      100,
                                      70,
                                      padding=20,
                                      text='Ulozit',
                                      onClick=lambda: new.Ulozit())


        self.seznam_pol = []
        for i in range(0,1001, 200):
            polygon_1 = pygame.draw.polygon(self.obraz, (100,100,100), ((i,1000),(i+100,1000),(i+50,650)))
            polygon_2 = pygame.draw.polygon(self.obraz, (150,0,0), ((i+100,1000),(i+200,1000),(i+150,650)))
            self.seznam_pol.append(polygon_1)
            self.seznam_pol.append(polygon_2)

        for i in range(0,1001, 200):
            polygon_1 = pygame.draw.polygon(self.obraz, (100,100,100), ((i,0),(i+100,0),(i+50,350)))
            polygon_2 = pygame.draw.polygon(self.obraz, (150,0,0), ((i+100,0),(i+200,0),(i+150,350)))
            self.seznam_pol.append(polygon_1)
            self.seznam_pol.append(polygon_2)

        pygame.draw.rect(self.obraz, (155,155,155), (400,450, 400,100))
        pygame.draw.rect(self.obraz, (255,255,255), (0,475, 200,50))
        pygame.draw.rect(self.obraz, (0,0,0), (1000,475, 200,50))

        pygame.display.flip()


class Dvojkostka:
    def __init__(self) -> None:
        self.kostka1 = None
        self.kostka2 = None

        self.tlacitko = True

        self.jedna = pygame.image.load('1.png')
        self.dva = pygame.image.load('2.png')
        self.tri = pygame.image.load('3.png')
        self.ctyri = pygame.image.load('4.png')
        self.pet = pygame.image.load('5.png')
        self.sest = pygame.image.load('6.png')
        

    def hod_kostkou(self) -> str:
        self.kostka1 = random.randrange(1,7)
        self.kostka2 = random.randrange(1,7)
        if self.kostka1 == 1:
            new.plocha.obraz.blit(self.jedna, (525,450))
        elif self.kostka1 == 2:
            new.plocha.obraz.blit(self.dva, (525,450))
        elif self.kostka1 == 3:
            new.plocha.obraz.blit(self.tri, (525,450))
        elif self.kostka1 == 4:
            new.plocha.obraz.blit(self.ctyri, (525,450))
        elif self.kostka1 == 5:
            new.plocha.obraz.blit(self.pet, (525,450))
        elif self.kostka1 == 6:
            new.plocha.obraz.blit(self.sest, (525,450))

        if self.kostka2 == 1:
            new.plocha.obraz.blit(self.jedna, (600,450))
        elif self.kostka2 == 2:
            new.plocha.obraz.blit(self.dva, (600,450))
        elif self.kostka2 == 3:
            new.plocha.obraz.blit(self.tri, (600,450))
        elif self.kostka2 == 4:
            new.plocha.obraz.blit(self.ctyri, (600,450))
        elif self.kostka2 == 5:
            new.plocha.obraz.blit(self.pet, (600,450))
        elif self.kostka2 == 6:
            new.plocha.obraz.blit(self.sest, (600,450))

        return f"Hodil jsi: [{self.kostka1}, {self.kostka2}]"
    
    

class Bar:
    def __init__(self) -> None:
        self.pocet_zetonu_bila_cil = 0
        self.pocet_zetonu_cerna_cil = 0
        self.zeton = None

    def vytvor_zeton_cerny(self):
        self.zeton = HerniKamen(200,200, (0,0,0))
        self.zeton.vytvor_zeton()

    def vytvor_zeton_bily(self):
        self.zeton = HerniKamen(200,200, (255,255,255))
        self.zeton.vytvor_zeton()
        
class HerniKamen:
    def __init__(self, x, y, barva) -> None:
        self.x = x
        self.y = y
        self.vyska = 30
        self.sirka = 10
        self.pozice = 0
        self.barva = barva
        self.kruh = None

    def akt_pozice(self) -> str:
        return print(f"Aktuální pozice = [{self.pozice}]")
    
    def vytvor_zeton(self):
        self.kruh_1 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[0].centerx, new.plocha.seznam_pol[0].bottom - self.vyska], 30, 0)
        self.kruh_2 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.seznam_pol[1].centerx, new.plocha.seznam_pol[1].bottom - self.vyska], 30, 0)
        """self.kruh_3 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_12.centerx, new.plocha.polygon_12.bottom - self.vyska], 30, 0)
        self.kruh_4 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_12.centerx, new.plocha.polygon_12.bottom - self.vyska], 30, 0)
        self.kruh_5 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_18.centerx, new.plocha.polygon_18.top + self.vyska], 30, 0)
        self.kruh_6 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_20.centerx, new.plocha.polygon_20.top + self.vyska], 30, 0)"""

class Hrac:
    def __init__(self, jmeno, barva) -> None:
        self.jmeno = jmeno
        self.barva = barva
    
    def vypis_hrace(self) -> str:
        return print(f"Hráč: {self.jmeno}, barva: {self.barva}")

class KonzolovyHrac(Hrac):
    pass

class AiHrac(Hrac):
    pass

new = Hra()
font = pygame.font.SysFont('Arial', 30)
new.plocha.obraz.blit(font.render(new.Hrac1.jmeno, True, (255,0,0)), (0, 480))
new.plocha.obraz.blit(font.render(new.Hrac2.jmeno, True, (255,0,0)), (1000, 480))
new.bar.vytvor_zeton_bily()
new.bar.vytvor_zeton_cerny()

while True:
    events = pygame.event.get()
    if pygame.mixer.get_busy() != None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if pygame.key.get_pressed()[pygame.K_q]:
            new.Ulozit()
            pygame.quit()

        if pygame.key.get_pressed()[pygame.K_k]:
            new.dvojkoskta.hod_kostkou()
        
        pygame_widgets.update(events)
        pygame.display.update()

#Dodělat základní rozestavení, hlavně nasazování žetonů na sebe
#Musí se předělat kdo je na tahu v textové podobě v levém bloku