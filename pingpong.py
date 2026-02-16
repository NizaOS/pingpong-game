import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <=0:
        player_score += 1
        score_time = pygame.time.get_ticks()

        
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()


    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1   

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0 
    if player.bottom >= screen_height:
        player.bottom = screen_height

def oppononet_ai():
    if opponent.top < ball.y + 50:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y + 50:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    
def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    
   

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None
    
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('pingpong')

iceblock = pygame.image.load("/Users/MyPC/brick.png").convert_alpha()
iceblock_ld = pygame.transform.scale(iceblock, (15, 210))

background = pygame.image.load('/Users/MyPC/Downloads/vecteezy_winter-snowfall-at-midnight-with-the-moon-and-stars-on-sky_16157330_175/vecteezy_winter-snowfall-at-midnight-with-the-moon-and-stars-on-sky_16157330.jpg')

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 105, 15, 210)
opponent = pygame.Rect(10, screen_height/2 - 105, 15, 210)

bg_color =pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
timer_font = pygame.font.SysFont(None, 64)
score_time = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed +=7

    ball_animation()
    player_animation()
    oppononet_ai()
    
    if score_time:
        ball_restart()
          
    screen.fill(bg_color)
    screen.blit(background, (0,0))
    screen.blit(iceblock_ld, player)
    screen.blit(iceblock_ld, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height)) 

    player_text = score_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))
    opponent_text = score_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (610, 470))
    pygame.display.flip()
    clock.tick(60)
