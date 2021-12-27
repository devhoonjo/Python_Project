##################################
#
# 이 프로젝트는 나도코딩님과
# https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=277s
# 가속님 블로그와
# https://m.blog.naver.com/2020xodn/222009846710
# JBMPA님의 블로그를 참고하여 진행하였습니다.
# https://www.jbmpa.com/pygame/20
#
#
#
#
#
###############################
#
# 게임 조건 설정
# 1. 5초씩 지남에 따라 공이 1개씩 추가된다.
# 2. 10초가 지날때 마다 공 속도가 전체적으로 빨라진다.
# 3. 시간단위는 초(s)로 0.00단위까지 책정이 된다.
# 4. 공에 맞으면 아웃.
# 5. 
#
#
#
################################

import pygame
import os
import random

pygame.init()


#화면 크기 설정
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoon's Dodge")

#FPS
clock = pygame.time.Clock()

###############################3
#1. 사용자 게임 초기화(배경화면, 좌표, 속도, 게임 이미지, 좌표, 폰트, 시간 등)

path = os.path.dirname(__file__)
image_path = os.path.join(path, "images")

#배경화면
background = pygame.image.load(os.path.join(image_path, "background.png"))

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect()
character_width = character_size.size[0]
character_height = character_size.size[1]
character_xpos = (screen_width / 2) - (character_width / 2)
character_ypos = (screen_height / 2) - (character_height / 2)

character_speed = 1

#볼 만들기
ball = pygame.image.load(os.path.join(image_path, "enemy.png"))
ball_size = ball.get_rect()
ball_width = ball_size.size[0]
ball_height = ball_size.size[1]
ball_spawnPoint = None
ball_xpos = 0
ball_ypos = 0
# ball_xpos = random.choice([0, (screen_width - ball_width), random.randint(0, screen_width - ball_width)])
# if ball_xpos == 0:
#     #ball_ypos = random.randint(0,screen_height - ball_height)
    
# elif screen_width - ball_width:
#     #ball_ypos = random.randint(0,screen_height - ball_height)
# else:
#     #ball_ypos = 0
ball_rad = 0

ball_speed = 1

ball_num = 15

#볼설정하기
balls = []
# for i in range(ball_num):
#     status = {
#         "ball_size" : ball.get_rect(),
#         "ball_width" : ball_size.size[0],
#         "ball_height" : ball_size.size[1],
#         "ball_spawnPoint" : none,
#         "ball_xpos" : 
#         "ball_ypos" : 
#         "ball_rad" : 
#         "ball_speed" :
#         "ball_dir" : 
#
#     }
#     for j in range(10):
#         balls.append(status)




#시간 설정
time = pygame.time.get_ticks()
total_score = time * 100

#폰트
font = pygame.font.Font(None, 40)


#게임 메세지 설정
game_msg = "Hello Dodge World"



#캐릭터 이동 변수
character_tox = 0
character_toy = 0


# 이벤트 루프
running = True
while running:
    fps = clock.tick(30)
    time_sec = fps / 1000.0
    #나가기 버튼 클릭시 꺼짐.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #2. 이벤트 처리(키보드, 마우스)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_tox -= 5
            elif event.key == pygame.K_RIGHT:
                character_tox += 5
            elif event.key == pygame.K_UP:
                character_toy -= 5
            elif event.key == pygame.K_DOWN:
                character_toy += 5
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_tox = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_toy = 0

    character_xpos += character_tox * fps
    character_ypos += character_toy * fps


    #3. 게임 캐릭터 위치 정의

    if character_xpos <= 0:
        character_xpos = 0
    elif character_xpos >= screen_width - character_width:
        character_xpos = screen_width - character_width

    if character_ypos <= 0:
        character_ypos = 0
    elif character_ypos >= screen_height - character_height:
        character_ypos = screen_height - character_height


    #4. 충돌처리
  
    #5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_xpos, character_ypos))
    pygame.display.update()



#게임화면을 다시 그리기



#잠시 대기
pygame.time.delay(2000)


#pygame 종료처리
pygame.quit()