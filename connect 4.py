import pygame
pygame.init()
pygame.font.init()


def thereisawinner():
    global game_end
    window.fill((255, 255, 255))
    game_end.append(Button(100, 100, 0, 0))
    game_end.append(Button(400, 100, 0, 0))


def iswinner(playboard, player):
    for i in range(len(playboard)):
        for j in range(len(playboard[0])):
            if isawinner(playerboard, player, i, j):
                return True
    return False


def isawinner(playerboard, player, i, j):
    count = 0
    x = i
    y = j
    while x < len(playerboard) and y < len(playerboard[0]):
        if playerboard[x][y] == player:
            x += 1
            y += 1
            count += 1
        else:
            break
        if count == 4:
            return True
    count = 0
    x = i
    y = j
    while x < len(playerboard) and y > 0:
        if playerboard[x][y] == player:
            x += 1
            y -= 1
            count += 1
        else:
            break
        if count == 4:
            return True
    count = 0
    x = i
    y = j
    while x > 0 and y < len(playerboard[0]):
        if playerboard[x][y] == player:
            x -= 1
            y += 1
            count += 1
        else:
            break
        if count == 4:
            return True
    count = 0
    x = i
    y = j
    while x > 0 and y > 0:
        if playerboard[x][y] == player:
            x -= 1
            y -= 1
            count += 1
        else:
            break
        if count == 4:
            return True
    count = 0
    x = i
    y = j
    while x < len(playerboard):
        if playerboard[x][y] == player:
            x += 1
            count += 1
        else:
            break
        if count == 4:
            return True
    count = 0
    x = i
    y = j
    while y < len(playerboard[0]):
        if playerboard[x][y] == player:
            y += 1
            count += 1
        else:
            break
        if count == 4:
            return True
    return False


def isvalidmove(playboard, i, j):
    for _ in range(i + 1, len(playboard)):
        if playboard[_][j] == 0:
            return False
    return True


def endgame(playerboard):
    for item in playerboard[0]:
        if item != 0:
            return False
    return True


def restart():
    global free_buttons
    global placeholders
    global playerboard
    global current_player
    global no_winner
    free_buttons = []
    placeholders = []
    playerboard = [[0 for i in range(7)] for j in range(6)]
    current_player = True
    no_winner = True
    for i in range(0, window_width, 100):
        for j in range(0, window_height, 100):
            free_buttons.append(Button(i, j, j // 100, i // 100))


class Player:
    def __init__(self, color, no_type):
        self.color = color
        self.no_type = no_type


class Grid:
    def __init__(self):
        self.grid_vertical = [((0,0),(0,600)),
                              ((100,0),(100,600)),
                         ((200,0),(200,600)),
                         ((300,0),(300,600)),
                         ((400,0),(400,600)),
                         ((500,0),(500,600)),
                         ((600,0),(600,600)), ((700,0),(700,600))]
        
        self.grid_horizontal = [((0, 0), (700, 0)),
                                ((0, 100), (700, 100)),
                           ((0, 200), (700, 200)),
                           ((0, 300), (700, 300)),
                           ((0, 400), (700, 400)),
                           ((0, 500), (700, 500)),
                                ((0, 600), (700, 600))]
        
    def creategrid(self):
        for line in self.grid_vertical:
            pygame.draw.line(window, (0, 0, 0), line[0], line[1], 3)
        for line in self.grid_horizontal:
            pygame.draw.line(window, (0, 0, 0), line[0], line[1], 3)


class Button:
    def __init__(self, i, j, x, y):
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        
    def ishover(self, mouse_position):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if mouse_position[0] > self.i + 25 and mouse_position[0] < self.i + 70:
            if mouse_position[1] > self.j + 25 and mouse_position[1] < self.j + 70:
                return True     
        return False
    
    def drawbutton(self, r, g, b):
        pygame.draw.rect(window, (r,g,b), (item.i + 25, item.j + 25,45, 45))


class Placeholder:
  def __init__(self, color, i, j):
    self.color = color
    self.i = i
    self.j = j
  def drawcircle(self):
    pygame.draw.circle(window, self.color,(self.i + 50, self.j + 50),45)


def text_objects(text, font):
    textsurface = font.render(text, True, (255, 255, 255))
    return textsurface, textsurface.get_rect()


def message_display(text, x, y, f):
    smalltext = pygame.font.Font("freesansbold.ttf", f)
    textsurf, textrect = text_objects(text, smalltext)
    textrect.center = (x, y)
    window.blit(textsurf, textrect)


game_end = []
newgrid = Grid()
free_buttons = []
placeholders = []
window_height = 600
window_width = 700
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Samuel Calmday and Chidindu Alim Lab 10")
run = True
playerboard = [[0 for i in range(7)] for j in range(6)]
player1 = Player((255, 0, 0), 1)
player2 = Player((0, 0, 255), 2)
current_player = True
no_winner = True
restart()
while run:
    
    pygame.time.delay(50)
    if no_winner:
        window.fill((255, 255, 255))
        for item in free_buttons:
            item.drawbutton(0, 255, 0)
        newgrid.creategrid()
        for item in range(len(placeholders)):
            placeholders[item].drawcircle()
    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        
    for item in free_buttons:
        if iswinner(playerboard, player1.no_type):
            no_winner = False
            window.fill((0, 0, 0))
            message_display("Red Wins", 350, 150, 60)
            pygame.draw.rect(window, (200, 0, 0), (100, 300, 150, 70))
            message_display("Quit", 175, 335, 20)
            pygame.draw.rect(window, (0, 200, 0), (400, 300, 150, 70))
            message_display("Restart", 475, 335, 20)
            if mouse_position[0] > 100 and mouse_position[0] < 250:
                if mouse_position[1] > 300 and mouse_position[1] < 370:
                    pygame.draw.rect(window, (255, 0, 0), (100, 300, 150, 70))
                    message_display("Quit", 175, 335, 20)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
            if mouse_position[0] > 400 and mouse_position[0] < 550:
                if mouse_position[1] > 300 and mouse_position[1] < 370:
                    pygame.draw.rect(window, (0, 255, 0), (400, 300, 150, 70))
                    message_display("Restart", 475, 335, 20)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        restart()
        elif iswinner(playerboard, player2.no_type):
            no_winner = False
            window.fill((0, 0, 0))
            message_display("Blue Wins", 350, 150, 60)
            pygame.draw.rect(window, (200, 0, 0), (100, 300, 150, 70))
            message_display("Quit", 175, 355, 20)
            pygame.draw.rect(window, (0, 200, 0), (400, 300, 150, 70))
            message_display("Restart", 475, 335, 20)
            if mouse_position[0] > 100 and mouse_position[0] < 250:
                if mouse_position[1] > 300 and mouse_position[1] < 370:
                    pygame.draw.rect(window, (255, 0, 0), (100, 300, 150, 70))
                    message_display("Quit", 175, 335, 20)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
            if mouse_position[0] > 400 and mouse_position[0] < 550:
                if mouse_position[1] > 300 and mouse_position[1] < 370:
                    pygame.draw.rect(window, (0, 255, 0), (400, 300, 150, 70))
                    message_display("Restart", 475, 335, 20)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        restart()
        elif item.ishover(mouse_position) and isvalidmove(playerboard, item.x, item.y):
            pygame.draw.rect(window, (255, 200, 100), (item.i + 25, item.j + 25, 45, 45))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for item in free_buttons:
                    if item.ishover(mouse_position) and isvalidmove(playerboard, item.x, item.y):
                        if current_player:
                            playerboard[item.x][item.y] = player1.no_type
                            placeholders.append(Placeholder(player1.color, item.i, item.j))
                            free_buttons.remove(item)
                            current_player = not current_player
                        else:
                            playerboard[item.x][item.y] = player2.no_type
                            placeholders.append(Placeholder(player2.color, item.i, item.j))
                            free_buttons.remove(item)
                            current_player = not current_player
    pygame.display.update()
pygame.quit()
