import pygame, sys, random, os


def load_asset(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
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
    global opponent_speed

    distance = opponent.centery - ball.centery
    if abs(distance) > 20:
        if distance > 0:
            opponent.y -= opponent_speed
        else:
            opponent.y += opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    
def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    elapsed_time = current_time - score_time

    if elapsed_time < 700:
        number = "3"
    elif 700 <= elapsed_time < 1400:
        number = "2"
    elif 1400 <= elapsed_time < 2100:
        number = "1"
    else:
        number = None
                    
    if elapsed_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
        return number
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None
        return None


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Winter Ping-Pong')


try:
    
    iceblock_img = pygame.image.load(load_asset("brick.png")).convert_alpha()
    iceblock_l = pygame.transform.scale(iceblock_img, (15, 210))
    iceblock_r = pygame.transform.flip(iceblock_l, True, False)

    background = pygame.image.load(load_asset("background.jpg")).convert()
    background = pygame.transform.scale(background, (screen_width, screen_height))
except FileNotFoundError:
    print("Error: Could not find image assets in the script folder!")
    print("Make sure 'brick.png' and 'background.jpg' are in the same directory as this script.")
    pygame.quit()
    sys.exit()


ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 105, 15, 210)
opponent = pygame.Rect(10, screen_height/2 - 105, 15, 210)


bg_color = pygame.Color('grey12')
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
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    
    ball_animation()
    player_animation()
    oppononet_ai()
    
    
    screen.fill(bg_color)
    screen.blit(background, (0,0))
    
    if score_time:
        timer_number = ball_restart()
        if timer_number:
            timer_surf = timer_font.render(timer_number, True, light_grey)
            timer_rect = timer_surf.get_rect(center=(screen_width/2,  screen_height/2 - 50))
            screen.blit(timer_surf, timer_rect)
            
    screen.blit(iceblock_l, player)
    screen.blit(iceblock_r, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height)) 

    player_text = score_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))
    opponent_text = score_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (605, 470))
    
    pygame.display.flip()
    clock.tick(60)