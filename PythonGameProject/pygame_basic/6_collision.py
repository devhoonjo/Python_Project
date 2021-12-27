import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoon's Game")

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/franh/OneDrive/문서/PythonGameProject/pygame_basic/background.png")

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/franh/OneDrive/문서/PythonGameProject/pygame_basic/character.png")

character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭더 가로 크기
character_height = character_size[1] #캐릭터 세로 크기

character_xpos = (screen_width / 2) - (character_width / 2)  #화면 가로의 절반 크기에 위치
character_ypos = screen_height - character_height


#이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("C:/Users/franh/OneDrive/문서/PythonGameProject/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해옴
enemy_width = enemy_size[0] #적 가로 크기
enemy_height = enemy_size[1] #적 세로 크기
enemy_xpos = (screen_width / 2) - (enemy_width / 2)  #화면 가로의 절반 크기에 위치
enemy_ypos = (screen_height /2) - (enemy_height /2)  #화면 세로의 절반 크기에 위치


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60)

    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 맨위 X 표시
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_xpos += to_x * dt
    character_ypos += to_y * dt


    #가로 경계값 처리
    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width


    #세로 경계값 처리
    if character_ypos < 0:
        character_ypos = 0
    elif character_ypos > screen_height - character_height:
        character_ypos = screen_height - character_height


    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xpos
    enemy_rect.top = enemy_ypos


    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    screen.blit(background, (0,0)) #배경 그리기 blit을 통해 그림
    #screen.fill((0,0,255)) #rgb값으로 색을 채워 넣음

    screen.blit(character, (character_xpos, character_ypos)) # 캐릭터 위치에 그리기

    screen.blit(enemy, (enemy_xpos, enemy_ypos)) # 적 캐릭터 그리기


    pygame.display.update() #게임화면을 다시 그리기



#pygame 종료처리
pygame.quit()