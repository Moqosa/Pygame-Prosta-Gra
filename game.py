import sys
import pygame
import random

end_point_x_position = random.randint(0,1800) #Losowania punktu ma mapie
end_pint_y_position = random.randint(0, 900)
pygame.init() #Funkcja która inicjalizuje wszystkie moduły
screen = pygame.display.set_mode((1920, 1080))  #Tworzenie okna gry
box = pygame.Rect(10,10,30,30) #Kwadrat gracza
point = pygame.Rect(10,10,50,50) #Punkt startowy
end_point = pygame.Rect(end_point_x_position, end_pint_y_position,25,25) #Punkt końcowy gracza
text = pygame.display.set_caption("You won!") #Zmienna z tekstem
border_rect = screen.get_rect() #Border mapy


while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sys.exit()

    # Sprawdzanie Input
    keys = pygame.key.get_pressed() #Pobieranie wciśnięktych klawiszy
    if keys[pygame.K_d]:
        box.x += 1
    if keys[pygame.K_s]:
        box.y += 1
    if keys[pygame.K_w]:
        box.y -= 1
    if keys[pygame.K_a]:
        box.x -= 1
    if keys[pygame.K_r]:
        print("Reset")
        game_state = True


    #Tworzenie obramowania mapy
    border_color = (0, 255, 0)
    pygame.draw.line(screen, border_color, (0, 0), (1920, 0))
    pygame.draw.line(screen, border_color, (0, 0), (0, 1080))
    pygame.draw.line(screen, border_color, (1915, 0), (1915, 1080))
    pygame.draw.line(screen, border_color, (0, 1070), (1920, 1070))

    box.clamp_ip(border_rect)

    # Rysowanie gracza
    pygame.draw.rect(screen, (0, 200, 255), box)

    # Rysowanie punktu
    pygame.draw.rect(screen, (255, 10, 10), point)

    # Rysowanie end point
    pygame.draw.rect(screen, (0, 255, 0), end_point)

    def display_message(message, font_size, x, y):
        font = pygame.font.Font(None, font_size)
        text = font.render(message, True, (255, 255, 255))
        screen.blit(text, (x, y))


    if isinstance(box, pygame.Rect) and isinstance(end_point, pygame.Rect):
        if box.colliderect(end_point):
            display_message("You won!", 54, 540, 360)

    display_message("Space = Quite", 54, 1550, 50)
    pygame.display.flip()  # Pokazanie użytkownikowi rysunku



