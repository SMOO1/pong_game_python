import pygame

pygame.init()

screen_width = 1400
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pong game")

#set up
paddle_width = 15
paddle_height = 160
paddle_speed = 1
paddle1_pos = pygame.Rect(50, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)
paddle2_pos = pygame.Rect(screen_width - 50 - paddle_width, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)

ball_size = 20
ball_speed = 1
ball_pos = pygame.Rect(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2, ball_size, ball_size)
ball_direction = [1, 1]

countdown_font = pygame.font.Font(None, 100)
playagainfont = pygame.font.Font(None, 20)

button_colour = (255, 255, 255)
button_width = 100
button_height = 35
button_x = screen_width / 3
button_y = 50
button_rect = pygame.Rect(button_x- button_width/2, button_y - button_height/2, button_width, button_height)

playagaintext = playagainfont.render("Play Again", True, (0,0,0))
pag_rect = playagaintext.get_rect(center=(button_x, button_y))

score_font = pygame.font.Font(None, 50)
score1 = 0
score2 = 0
winnerfont = pygame.font.Font('freesansbold.ttf', 32)
winnertext = ""


countdowntime = 3
clock = pygame.time.Clock()


#game loop 
while True:

    if score1 == 15 or score2 == 15:
        ball_speed = 0
        paddle_speed = 0
        if score1>score2:
            winnertext = "Player 1 wins!"
        else:
            winnertext = "Player 2 wins!"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if button_x <= mouse_pos[0] <= button_x+button_width and button_y <= mouse_pos[1] <= button_y + button_height:
            score1, score2 = 0, 0
            winnertext = ""
            paddle1_pos = pygame.Rect(50, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)
            paddle2_pos = pygame.Rect(screen_width - 50 - paddle_width, screen_height / 2 - paddle_height / 2,paddle_width, paddle_height)
            pygame.display.update()
            pygame.time.wait(500)
            y = screen_width /4
            for x in ("3","2", "1", 'GO'):
                countdown = x
                countdownsurface=countdown_font.render(countdown, True, (255, 255, 255))
                if x == "GO":
                    countdown_pos = countdownsurface.get_rect(center=(screen_width/2, screen_height/2 +screen_height/4))
                else:
                    countdown_pos = countdownsurface.get_rect(center=(y, screen_height / 3))
                screen.blit(countdownsurface, countdown_pos)
                pygame.display.update()
                pygame.time.wait(500)
                y+= screen_width/4
            pygame.time.wait(500)
            ball_pos = pygame.Rect(screen_width/2- ball_size /2, screen_height / 2- ball_size/ 2, ball_size, ball_size)
            pygame.display.update()
            ball_speed, paddle_speed = 1, 1
            pygame.display.update()


    mouse_pos = pygame.mouse.get_pos()
    if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
        button_colour = (192,192,192)
    else:
        button_colour = (255,255,255)

    # move paddles
    keys =pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if paddle1_pos.top > 0:
            paddle1_pos.move_ip(0, -paddle_speed)
    if keys[pygame.K_s]:
        if paddle1_pos.bottom < screen_height:
            paddle1_pos.move_ip(0, paddle_speed)
    if keys[pygame.K_UP]:
        if paddle2_pos.top > 0:
            paddle2_pos.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN]:
        if paddle2_pos.bottom<screen_height:
            paddle2_pos.move_ip(0, paddle_speed)

    #update positions of game objects
    ball_pos.move_ip(ball_speed* ball_direction[0], ball_speed * ball_direction[1])

    # Check for collisions with the walls
    if ball_pos.top < 0 or ball_pos.bottom > screen_height:
        ball_direction[1] = -ball_direction[1]

    # Check for collisions with the paddles
    if ball_pos.colliderect(paddle1_pos) or ball_pos.colliderect(paddle2_pos):
        ball_direction[0] = -ball_direction[0]

    # Check if the ball has gone past a paddle
    if ball_pos.left < 0:
        score2 += 1
        ball_pos = pygame.Rect(screen_width / 2 - ball_size / 2, screen_height / 2 - ball_size / 2, ball_size, ball_size)
        ball_direction = [1, 1]

    if ball_pos.right > screen_width:
        score1 += 1
        ball_pos = pygame.Rect(screen_width/ 2 - ball_size / 2, screen_height / 2-ball_size / 2, ball_size, ball_size)
        ball_direction = [-1, 1]

    #score render
    score_text = f"{score1} : {score2}"
    score_surface = score_font.render(score_text, True, (255, 255, 255))
    score_pos = score_surface.get_rect(center=(screen_width/2, 50))

    #draw everything on the screen
    screen.fill((0, 0, 0))
    winnersurface = winnerfont.render(winnertext, True, (255, 223, 0))
    winnerpos = winnersurface.get_rect(center=(screen_width / 2, screen_height /3))
    screen.blit(winnersurface, winnerpos)
  
    button_rect = pygame.Rect(button_x - button_width / 2, button_y - button_height / 2, button_width, button_height)

    pygame.draw.rect(screen, button_colour, button_rect)
    pygame.draw.rect(screen, (255, 255, 255), paddle1_pos)
    pygame.draw.rect(screen, (255, 255, 255), paddle2_pos)
    pygame.draw.ellipse(screen, (255, 255, 255), ball_pos)
    screen.blit(score_surface, score_pos)
    screen.blit(playagaintext, pag_rect)
    pygame.display.update()
