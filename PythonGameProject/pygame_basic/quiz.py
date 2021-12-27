import pygame
import random
#################################################3
#
#하늘에서 떨어지는 똥피하기 게임
#
#[게임조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동가능
# 2. 똥은 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정
#
#[게임이미지]
# 1. 배경 : 640 * 480
# 2. 캐릭터 : 70 * 70
# 3. 똥 : 70 * 70
#
##################################################


#기본 초기화 반드시 해야함
pygame.init()



#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoon's Game")
#pygame.display.set_caption("Hoon's Game")

#FPS
clock = pygame.time.Clock()
#clock = pygame.time.Clock()


###############################3
#1. 사용자 게임 초기화(배경화면, 좌표, 속도, 게임 이미지, 좌표, 폰트, 시간 등)

background = pygame.image.load("C:/Users/franh/OneDrive/문서/PythonGameProject/pygame_basic/background.png")

character = pygame.image.load("C:/Users/franh/OneDrive/문서/PythonGameProject/pygame_basic/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = (screen_width / 2) - (character_width / 2)
character_ypos = screen_height - character_height

#똥
ddong = pygame.image.load("C:/Users/franh/OneDrive/문서/PythonGameProject/pygame_basic/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_xpos = random.randint(0, screen_width - ddong_width)
ddong_ypos = 0



#이동할 좌표
to_x = 0


#게임스피드
game_speed = 1


#폰트
font = pygame.font.Font(None, 0)

#캐릭터 스피드
character_speed = 10

#똥스피드
ddong_speed = 10



# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30)

    #2. 이벤트 처리(키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        #3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_xpos += to_x

    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width


    ddong_ypos += ddong_speed

    if ddong_ypos > screen_height:
        ddong_ypos = 0
        ddong_xpos = random.randint(0, screen_width - ddong_width)


    #4. 충돌처리

    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_xpos
    ddong_rect.top = ddong_ypos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False


  

    #5. 화면에 그리기
    screen.blit(background, (0,0))

    screen.blit(character, (character_xpos, character_ypos))

    screen.blit(ddong, (ddong_xpos, ddong_ypos))

    pygame.display.update() #게임화면을 다시 그리기



#잠시 대기
pygame.time.delay(2000)


#pygame 종료처리
pygame.quit()