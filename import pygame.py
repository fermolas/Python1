import pygame

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego con Pygame")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Jugador
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 5

# Bucle principal
going = True
clock = pygame.time.Clock()

while going:
    screen.fill(WHITE)  # Fondo blanco
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # Dibujar el jugador
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
