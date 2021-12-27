import pygame
import os
#################################################3
#기본 초기화 반드시 해야함
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoon's Pang")

#FPS
clock = pygame.time.Clock()

###############################3
#1. 사용자 게임 초기화(배경화면, 좌표, 속도, 게임 이미지, 좌표, 폰트, 시간 등)
current_path = os.path.dirname(__file__) #현재 파일의 위치를 반환

image_path = os.path.join(current_path, "images")


#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만드릭
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect()
character_width = character_size.size[0]
character_height = character_size.size[1]
character_xpos = (screen_width / 2) - (character_width / 2)
character_ypos = screen_height - character_height - stage_height




# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30)

    #2. 이벤트 처리(키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    #3. 게임 캐릭터 위치 정의


    #4. 충돌처리
  

    #5. 화면에 그리기

    screen.blit(background, (0,0))

    screen.blit(stage, (0, screen_height - stage_height))

    screen.blit(character, (character_xpos, character_ypos))

    pygame.display.update() #게임화면을 다시 그리기





#잠시 대기
pygame.time.delay(2000)


#pygame 종료처리
pygame.quit()