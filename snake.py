import pygame #Importerer modulen.
import random #Importerer random. Modulen kan brukes til å lage tilfeldige tall.
import time #Importerer time.

#Programmet:
pygame.init() #Initialiserer pygame-modulene.
clock = pygame.time.Clock() 
fps = 60

#Variabler for fargekodene:
WHITE = (255,255,255) 
GREEN = (124,252,0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BACKGROUNDCOLOR = (200, 100, 0)

CELL_SIZE = 40 #Størrelsen på hver rute. 
CELL_NUMBER = 15 
BREDDE = CELL_SIZE * CELL_NUMBER #Regner ut bredden.
HØYDE = CELL_SIZE * CELL_NUMBER #Regner ut høyden

#Definerer verdiene til slangen:
slange = [ 7 * CELL_SIZE + 1, 7 * CELL_SIZE + 1 , CELL_SIZE - 1, CELL_SIZE - 1] #Plasserer slangen midt i ruta.

screen = pygame.display.set_mode((BREDDE, HØYDE)) #Setter størrelsen på vinduet

class Snake: #Klasse-objekt for slangen
    def __init__(self): #Definerer verdier til slangen:
        self.dir = "r" #Retning slangen går. r = høyre.
        self.height = CELL_SIZE #Høyde og bredde på slangen.
        self.width = CELL_SIZE
        self.body = [[ 7 * CELL_SIZE + 1, 7 * CELL_SIZE + 1 , CELL_SIZE - 1, CELL_SIZE - 1], [ 6 * CELL_SIZE + 1, 7 * CELL_SIZE + 1 , CELL_SIZE - 1, CELL_SIZE - 1], [ 5 * CELL_SIZE + 1, 7 * CELL_SIZE + 1 , CELL_SIZE - 1, CELL_SIZE - 1]] #Oppretter 3 blokker på slangen, og disse blir plassert midt i en rute. 
        self.color = GREEN #Farge på slangen.
        self.timer = round(time.time() * 1000)
        self.speed = 500
        self.score = 0


    def draw(self): #Slange-funksjon som tegner slangen.  
        for block in self.body: #For hver blokk i kroppen til slangen.
            pygame.draw.rect(screen, self.color, block)

    def move(self): #Funksjon som beveger slangen i et bestemt tempo.
        if self.timer < (time.time() * 1000) - self.speed: 
            newHead = self.body.pop()
            newHead[0] = self.body[0][0]
            newHead[1] = self.body[0][1]
            if self.dir == "r": #Hvis retningen er r. (høyre)
                newHead[0] += 1 * CELL_SIZE #Beveg slangen til høyre.
            
            elif self.dir == "l": #l = venstre
                newHead[0] -= 1 * CELL_SIZE #Beveg slangen til venstre.
                
            elif self.dir == "d": #d = ned
                newHead[1] += 1 * CELL_SIZE #Beveg slangen ned.
                
            elif self.dir == "u": #u = opp
                newHead[1] -= 1 * CELL_SIZE #Beveg slangen opp.
                
            self.body.insert(0, newHead) #Legger til nytt hode.
            self.timer = round(time.time() * 1000) #Oppdaterer tiden.

    
    def add_block(self): #Funksjon som legger til en blokk til slangen
        newBlock = self.body[-1].copy() #Lager en kopi av en av blokkene til slangen.
        self.body.insert(-1, newBlock) #Legger til kopien i slangen.
        self.score += 1 #Øker antall epler samlet. (teksten på skjermen)
        if self.speed > 200: #Hvis farten er mer enn 200. (Dette sikrer at slangen ikke blir ukontrollerbar rask)
            self.speed -= 20 #Øker farten.
        

    def reset_game(self): #Funksjon som setter slangen til sin opprinnelige posisjon.
        self.body = [[ 7 * CELL_SIZE + 1, 7 * CELL_SIZE + 1 , CELL_SIZE - 1, CELL_SIZE - 1], [ 6 * CELL_SIZE + 1, 7 * CELL_SIZE + 1 , CELL_SIZE - 1, CELL_SIZE - 1], [ 5 * CELL_SIZE + 1, 7 * CELL_SIZE + 1 , CELL_SIZE - 1, CELL_SIZE - 1]] #Oppretter 3 blokker på slangen, og disse blir plassert midt i en rute. 
        self.speed = 500 #Setter farten til 500
        self.dir = "r" #Setter retningen på slangen til høyre.
        self.score = 0 #Setter antall epler samlet inn til 0.



class Apple: #Klasse for eple-objektet. 
    def __init__(self): #Definerer ulike spesifikasjoner for eplet. 
        self.height = CELL_SIZE - 1 #Regner ut høyden på eplet.
        self.width = CELL_SIZE - 1 #Regner ut bredden å eplet.
        self.xPos = random.randint(0, 14) * CELL_SIZE + 1 #Tilfeldig x posisjon hvor slangen starter.
        self.yPos = random.randint(0, 14) * CELL_SIZE + 1 #TIlfeldig y posisjon hvor slangen starter. 
        self.color = RED #Setter fargen på slangen.

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.xPos, self.yPos, self.height, self.width)) #Tegner et rødt eple med tilfeldig posisjon.

def draw_score(tall): #Funksjon som tegner antall epler so blir samlet inn. (tekst)
    myFont = pygame.font.SysFont("monospace", 38)  #Velger font.
    label = myFont.render(f"Antall epler: {tall}" ,1, BLACK) #Setter teksten til antall epler som er samlet inn, og fargen til svart.
    screen.blit(label, (20, 20))

def collide(): #FUnksjon for å sjekke om slangen har tatt et eple. 
    if snake.body[0][0] == apple.xPos and snake.body[0][1] == apple.yPos: #Hvis hodet til slangen er der eplet er.

        #Genererer ny tilfeldig posisjon, og setter eplet der: 
        apple.xPos = random.randint(0, 14) * CELL_SIZE + 1
        apple.yPos = random.randint(0, 14) * CELL_SIZE + 1


        snake.add_block() #Kjører funksjonen i slange-klassen. Funksjonen legger til en ny blokk til slangen.


    if snake.body[0][0] > BREDDE: #Hvis hodet til slangen er større enn bredden på skjermen. (Om slangen går ut av skjermen til høyre)
        snake.reset_game() #Kjører funksjonen som starter spillet på nytt.

    elif snake.body[0][1] > BREDDE: #Sjekker om slangen går ut av bunnen av skjermen.
        snake.reset_game()

    elif snake.body[0][1] < 0: #Sjekker om spilleren går ut av skjermen oppe.
        snake.reset_game()
    
    elif snake.body[0][0] < 0: #Sjekker om spilleren går ut av skjermen til venstre.
        snake.reset_game()

    for block in snake.body[1:]: #Går igjennom alle blokkene til slangen.
        if snake.body[0][0] == block[0] and snake.body[0][1] == block [1]: #Hvis slangen kolliderer med den blokken.
            snake.reset_game()

        

#Funksjon som tegner rutene slangen kan bevege seg i:
def draw_cells():
    for x in range(CELL_NUMBER): #For-løkke som tegner linjer nedover, og beveger seg til høyre. Gjentar antall ganger som er sagt i CELL_NUMBER.
        pygame.draw.line(screen, (0,0,0), (x * CELL_SIZE, 0 ), (x * CELL_SIZE, HØYDE)) #Tegner linjer rett ned, forflytter seg litt til høyre, og fortsetter å tegne nedover.


    for y in range(CELL_NUMBER): #For-løkke som tegner linjer til høyre, og beveger seg nedover. Gjentar antall ganger som er sagt i CELL_NUMBER.
        pygame.draw.line(screen, (0,0,0), (0, y * CELL_SIZE ), (BREDDE, y * CELL_SIZE)) #Tegner linjer rett ned, forflytter seg litt til høyre, og fortsetter å tegne nedover.



    


def update(): #Funksjon som oppdaterer spillet.
    screen.fill(BACKGROUNDCOLOR)#Tegner hvit bakgrunn.

    
    
    
    #Kjører funksjonene fra slange og eple-klassen:
    snake.draw()
    snake.move()
    apple.draw()

    #Kjører funksjonene:
    draw_score(snake.score)
    collide() #Hvis slangen kolliderer med veggen, seg selv, eller eplet.
    

    pygame.display.update() #Oppdaterer skjermen.
    

snake = Snake() #Får ut verdiene til slangen fra slange-klassen, og setter det til et objekt "snake".
apple = Apple() #Gjør det samme, men med eple-objektet. 

main = True #Setter main til True. 

#While løkke som kjører så lenge main er True:
while main:

    clock.tick(fps) #Kjører løkka antall ganger hvert sekund. (fps).

    for event in  pygame.event.get():
        if event.type == pygame.KEYDOWN: #Hvis krysset på høyre side av vinduet trykkes, lukkes vinduet.
           
            if event.key == pygame.K_ESCAPE: #Hvis escape trykkes, avslutt.
                main = False #Setter main til false, slik at while-løkka avsluttes, og programemt lukkes.
            
            #Inndata for å bevege slangen med piltastene eller W, A, S, D.
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: #Hvis pil til venstre trykkes, eller tasten "A".
                if snake.dir != "r": #Hvis retningen ikke er r.
                    snake.dir = "l" #forandrer "dir" til l. 

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                if snake.dir != "l": #Hvis retningen ikke er r.
                    snake.dir = "r"
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if snake.dir != "d": #Hvis retningen ikke er r.
                    snake.dir = "u"
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if snake.dir != "u": #Hvis retningen ikke er r.
                    snake.dir = "d"
       
            

    
    update() #Kjører funksjonen som styrer de andre funksjonene. 