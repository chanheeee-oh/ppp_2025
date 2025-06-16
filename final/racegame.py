import pygame
import random

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

teams = [
    "Ferrari", "McLaren", "Red Bull", "Mercedes", "Aston Martin",
    "Alpine", "Haas", "Racing Bulls", "Williams", "Kick Sauber"
]

team_car_images = {
    "Ferrari": "C:/code/ppp2025/ferrariCar01.png",
    "McLaren": "C:/code/ppp2025/mclarenCar10.png",
    "Red Bull": "C:/code/ppp2025/redbullCar14.png",
    "Mercedes": "C:/code/ppp2025/MercedesCar04.png",
    "Aston Martin": "C:/code/ppp2025/Aston Martin Car09.png",
    "Alpine": "C:/code/ppp2025/alpineCar11.png",
    "Haas": "C:/code/ppp2025/hassCar03.png",
    "Racing Bulls": "C:/code/ppp2025/Racing BullsCar17.png",
    "Williams": "C:/code/ppp2025/WilliamsCar13.png",
    "Kick Sauber": "C:/code/ppp2025/sauberCar16.png"
}


class Car:
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.image = None
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def load_image(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y])

    def move_x(self):
        self.x += self.dx

    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):
        if self.x + self.width > WINDOW_WIDTH or self.x < 0:
            self.x -= self.dx

    def check_crash(self, car):
        if (self.x + self.width > car.x) and (self.x < car.x + car.width) and \
                (self.y < car.y + car.height) and (self.y + self.height > car.y):
            return True
        return False


def draw_team_selection():
    selected = 0
    font_path = "C:/code/ppp2025/formula1-display-bold (1)/Formula1-Bold_web_0.ttf"
    title_font = pygame.font.Font(font_path, 30)
    font_team = pygame.font.Font(font_path, 30)

    while True:
        screen.fill(BLACK)

        title = title_font.render("Select your racing team", True, WHITE)
        screen.blit(title, (30, 50))

        for i in range(len(teams)):
            color = RED if i == selected else WHITE
            text = font_team.render(teams[i], True, color)
            screen.blit(text, (80, 160 + i * 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(teams)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(teams)
                elif event.key == pygame.K_RETURN:
                    return selected


def draw_main_menu():
    draw_x = (WINDOW_WIDTH / 2) - 200
    draw_y = WINDOW_HEIGHT / 2

    image_intro = pygame.image.load("C:/code/ppp2025/KakaoTalk_20250607_033215698.jpg")
    screen.blit(image_intro, [draw_x, draw_y - 200])

    font_40 = pygame.font.Font(font_path, 40)
    font_30 = pygame.font.Font(font_path, 30)

    text_title = font_40.render("PyCar: Racing Car Game", True, BLACK)
    text_score = font_40.render("Score: " + str(score), True, WHITE)
    text_start = font_30.render("Press space key to Start!", True, RED)

    screen.blit(text_start, [draw_x, draw_y - 200])
    screen.blit(text_title, [draw_x, draw_y])
    screen.blit(text_score, [draw_x, draw_y + 70])

    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Racing Game")
    clock = pygame.time.Clock()

    font_path = "C:/code/ppp2025/formula1-display-bold (1)/Formula1-Bold_web_0.ttf"

    selected_team_index = draw_team_selection()
    selected_team_name = teams[selected_team_index]
    player_image_path = team_car_images[selected_team_name]

    pygame.mixer.music.load("C:/code/ppp2025/Race.wav")
    sound_crash = pygame.mixer.Sound("C:/code/ppp2025/crash.wav")
    sound_engine = pygame.mixer.Sound("C:/code/ppp2025/engine.wav")

    player = Car(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 150, 0, 0)
    player.load_image(player_image_path)

    lanes = []
    lane_width = 10
    lane_height = 80
    lane_margin = 20
    lane_count = 20
    lane_x = (WINDOW_WIDTH - lane_width) / 2
    lane_y = -10
    for _ in range(lane_count):
        lanes.append([lane_x, lane_y])
        lane_y += lane_height + lane_margin

    score = 0
    crash = True
    game_on = True

    default_enemy_images = [
        "C:/code/ppp2025/RacingCar02.png",
        "C:/code/ppp2025/RacingCar05.png",
        "C:/code/ppp2025/RacingCar06.png",
        "C:\code\ppp2025\RacingCar07.png",
        "C:\code\ppp2025\RacingCar08.png",
        "C:\code\ppp2025\RacingCar12.png",
        "C:\code\ppp2025\RacingCar15.png",
        "C:\code\ppp2025\RacingCar18.png",
        "C:\code\ppp2025\RacingCar19.png",
        "C:\code\ppp2025\RacingCar20.png",

    ]

    excluded_team_enemy_images = [
        path for team, path in team_car_images.items()
        if team != selected_team_name
    ]

    enemy_image_paths = default_enemy_images + excluded_team_enemy_images

    enemies = []
    enemy_spawn_delay = 30
    enemy_timer = 0

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

            if crash:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    crash = False
                    player.load_image(player_image_path)
                    player.x = WINDOW_WIDTH / 2
                    player.dx = 0
                    score = 0
                    pygame.mouse.set_visible(False)
                    sound_engine.play()
                    pygame.time.delay(1000)
                    pygame.mixer.music.play(-1)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player.dx = 4
                    elif event.key == pygame.K_LEFT:
                        player.dx = -4
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                        player.dx = 0

        screen.fill(BLACK)

        if not crash:
            def draw_score():
                font_30 = pygame.font.SysFont("FixedSys", 30, True, False)
                text_score = font_30.render("Score: " + str(score), True, BLACK)
                screen.blit(text_score, [15, 15])


            for i in range(lane_count):
                pygame.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
                lanes[i][1] += 10
                if lanes[i][1] > WINDOW_HEIGHT:
                    lanes[i][1] = -40 - lane_height
                    enemy_timer += 1
                    if enemy_timer > enemy_spawn_delay:
                        enemy_timer = 0
                        enemy = Car(random.randint(0, WINDOW_WIDTH - 50), -100, 0, 7)
                        random_image_path = random.choice(enemy_image_paths)
                        enemy.load_image(random_image_path)
                        enemies.append(enemy)

            player.draw_image()
            player.move_x()
            player.check_out_of_screen()

            for enemy in enemies[:]:
                enemy.move_y()
                enemy.draw_image()

                if player.check_crash(enemy):
                    sound_crash.play()
                    pygame.mixer.music.stop()
                    crash = True
                    pygame.mouse.set_visible(True)
                    enemies.clear()
                    break

                if enemy.y > WINDOW_HEIGHT:
                    enemies.remove(enemy)
                    score += 25

            draw_score()
            pygame.display.flip()
        else:
            draw_main_menu()

        clock.tick(60)

    pygame.quit()









