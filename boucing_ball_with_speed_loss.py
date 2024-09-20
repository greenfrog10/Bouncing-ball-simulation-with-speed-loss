import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
x, y = screen.get_width() / 2, screen.get_height() / 2 - 300
pygame.display.set_caption('Infinite Bouncing Ball')
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
gravity = 0.0001
velocity = 0
energy_loss = 0.8
ball_velocity_x = 0.1  # initial horizontal velocity
min_bounce_velocity = 0.06  # minimum velocity to ensure the ball keeps bouncing
pygame.mixer.init()
# load the audio file
boing_sound = pygame.mixer.Sound("boing.mp3")
#create the platforms
platform1_x = 100
platform1_y = 450
platform1_velocity_x = 0.1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")
    
    # Draw the ball
    pygame.draw.circle(screen, "red", (int(x), int(y)),40)
    #drawing platforms
    platform1 = pygame.Rect(platform1_x,platform1_y,150,100)
    ball_collision_rect = pygame.Rect(x - 40,y - 40,80,80)
    pygame.draw.rect(screen, "blue", platform1)
    platform1_x += platform1_velocity_x
    # Update position and velocity
    y += velocity
    x += ball_velocity_x
    
    # Check for collision with screen edges
    if x + 40 >= 500:  
        x = 500 - 40
        ball_velocity_x = -ball_velocity_x  # Reverse horizontal direction
    if platform1_x + 130 >= 500:
        platform1_x = 500 - 130
        platform1_velocity_x = -platform1_velocity_x
    if x - 40 <= 0:  
        x = 40
        ball_velocity_x = -ball_velocity_x  # Reverse horizontal direction
    if platform1_x - 10 <= 0:  
        platform1_x = 10
        platform1_velocity_x = -platform1_velocity_x
    if ball_collision_rect.colliderect(platform1):
        velocity = -0.25 * energy_loss
        boing_sound.play()
    velocity += gravity
    
    # Bounce off the bottom
    if y >= 460:
        y = 460
        velocity = -velocity * energy_loss
        boing_sound.play()
        
        # Ensure the ball gains velocity if it's below the threshold
        if abs(velocity) < min_bounce_velocity:
            velocity = -0.25
            boing_sound.play()
            

    pygame.display.flip()

pygame.quit()
