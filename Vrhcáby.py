import sys, pygame, random, pygame_widgets
from pygame_widgets.button import Button

pygame.init()
pygame.font.init()

class Hra:
    def __init__(self) -> None:
        self.dvojkoskta = Dvojkostka()
        self.bar = Bar()
        volba = input("Budeš hrát s hráčem (1), nebo s AI (0)?")
        if volba == "1":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, "Bílá")
            hrac2 = input("Jméno hráče 2: ")
            self.Hrac2 = KonzolovyHrac(hrac2, "Černá")
        elif volba == "0":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, "Bílá")
            hrac2 = input("Jméno Ai 1: ")
            self.Hrac2 = AiHrac(hrac2, "Černá")
        self.plocha = HerniPole()

class HerniPole:
    def __init__(self) -> None:
        self.sirka = 1200
        self.vyska = 1000
        self.obraz = pygame.display.set_mode((self.sirka,self.vyska))
        self.obraz.fill((255,155,50))
        

        self.tlacitko_hod = Button(self.obraz, 
                                   825, 
                                   460, 
                                   80, 
                                   80,
                                   padding=20,
                                   text='Hod Kostkou',
                                   onClick=lambda: new.dvojkoskta.hod_kostkou())


        self.seznam_pol = []
        for i in range(0,1001, 200):
            polygon_1 = pygame.draw.polygon(self.obraz, (0,0,0), ((i,1000),(i+100,1000),(i+50,650)))
            polygon_2 = pygame.draw.polygon(self.obraz, (150,0,0), ((i+100,1000),(i+200,1000),(i+150,650)))
            self.seznam_pol.append(polygon_1)
            self.seznam_pol.append(polygon_2)

        """for i in range(0,1001, 200):
            polygon = pygame.draw.polygon(self.obraz, (150,0,0), ((i+100,1000),(i+200,1000),(i+150,650)))
            self.seznam_pol.append(polygon)"""


        """self.polygon_12 = pygame.draw.polygon(self.obraz, (0,0,0), ((0,1000),(100,1000),(50,650)))
        self.polygon_11 = pygame.draw.polygon(self.obraz, (150,0,0), ((100,1000),(200,1000),(150,650)))
        self.polygon_10 = pygame.draw.polygon(self.obraz, (0,0,0), ((200,1000),(300,1000),(250,650)))
        self.polygon_9 = pygame.draw.polygon(self.obraz, (150,0,0), ((300,1000),(400,1000),(350,650)))
        self.polygon_8 = pygame.draw.polygon(self.obraz, (0,0,0), ((400,1000),(500,1000),(450,650)))
        self.polygon_7 = pygame.draw.polygon(self.obraz, (150,0,0), ((500,1000),(600,1000),(550,650)))
        self.polygon_6 = pygame.draw.polygon(self.obraz, (0,0,0), ((600,1000),(700,1000),(650,650)))
        self.polygon_5 = pygame.draw.polygon(self.obraz, (150,0,0), ((700,1000),(800,1000),(750,650)))
        self.polygon_4 = pygame.draw.polygon(self.obraz, (0,0,0), ((800,1000),(900,1000),(850,650)))
        self.polygon_3 = pygame.draw.polygon(self.obraz, (150,0,0), ((900,1000),(1000,1000),(950,650)))
        self.polygon_2 = pygame.draw.polygon(self.obraz, (0,0,0), ((1000,1000),(1100,1000),(1050,650)))
        self.polygon_1 = pygame.draw.polygon(self.obraz, (150,0,0), ((1100,1000),(1200,1000),(1150,650)))"""

        pygame.draw.rect(self.obraz, (155,155,155), (400,450, 400,100))
        pygame.draw.rect(self.obraz, (255,255,255), (0,475, 200,50))
        pygame.draw.rect(self.obraz, (0,0,0), (1000,475, 200,50))

        self.polygon_13 = pygame.draw.polygon(self.obraz, (150,0,0), ((0,0),(100,0),(50,350)))
        self.polygon_14 = pygame.draw.polygon(self.obraz, (0,0,0), ((100,0),(200,0),(150,350)))
        self.polygon_15 = pygame.draw.polygon(self.obraz, (150,0,0), ((200,0),(300,0),(250,350)))
        self.polygon_16 = pygame.draw.polygon(self.obraz, (0,0,0), ((300,0),(400,0),(350,350)))
        self.polygon_17 = pygame.draw.polygon(self.obraz, (150,0,0), ((400,0),(500,0),(450,350)))
        self.polygon_18 = pygame.draw.polygon(self.obraz, (0,0,0), ((500,0),(600,0),(550,350)))
        self.polygon_19 = pygame.draw.polygon(self.obraz, (150,0,0), ((600,0),(700,0),(650,350)))
        self.polygon_20 = pygame.draw.polygon(self.obraz, (0,0,0), ((700,0),(800,0),(750,350)))
        self.polygon_21 = pygame.draw.polygon(self.obraz, (150,0,0), ((800,0),(900,0),(850,350)))
        self.polygon_22 = pygame.draw.polygon(self.obraz, (0,0,0), ((900,0),(1000,0),(950,350)))
        self.polygon_23 = pygame.draw.polygon(self.obraz, (150,0,0), ((1000,0),(1100,0),(1050,350)))
        self.polygon_24 = pygame.draw.polygon(self.obraz, (0,0,0), ((1100,0),(1200,0),(1150,350)))
         
        """self.seznam = [self.polygon_1, self.polygon_2, self.polygon_3]"""

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
        """self.kruh_1 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_1.centerx, new.plocha.polygon_1.bottom - self.vyska], 30, 0)
        self.kruh_2 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_1.centerx, new.plocha.polygon_1.bottom - self.vyska], 30, 0)
        self.kruh_3 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_12.centerx, new.plocha.polygon_12.bottom - self.vyska], 30, 0)
        self.kruh_4 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_12.centerx, new.plocha.polygon_12.bottom - self.vyska], 30, 0)"""
        self.kruh_5 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_18.centerx, new.plocha.polygon_18.top + self.vyska], 30, 0)
        self.kruh_6 = pygame.draw.circle(new.plocha.obraz, self.barva, [new.plocha.polygon_20.centerx, new.plocha.polygon_20.top + self.vyska], 30, 0)

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pygame.key.get_pressed()[pygame.K_q]:
        pygame.quit()
    

    if pygame.key.get_pressed()[pygame.K_k]:
        new.dvojkoskta.hod_kostkou()
    
    pygame_widgets.update(events)
    pygame.display.update()

#Dodělat základní rozestavení, hlavně nasazování žetonů na sebe