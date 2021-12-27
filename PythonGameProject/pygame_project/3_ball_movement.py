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

character_to_X = 0
character_speed = 10

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect()
weapon_width = weapon_size.size[0]


#무기를 한번에 여러번 사용
weapons = []

#무기속도
weapon_speed = 10


#공만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

#공크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] #index 0, 1, 2, 3 에 해당하는 값

#공들
balls = []


#최초로 발생하는 큰공 추가
balls.append({
    "pos_x" : 50, #공의 x좌표
    "pos_y" : 50, #공의 t좌표
    "img_idx" : 0, #공의 이미지 인덱스
    "to_x" : 3, #x축 이동방향, -3이면 왼쪽, 3이면 오른쪽
    "to_y" : -6, #y축 이동방향
    "init_spd_y" : ball_speed_y[0] #y 최초속도
})


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
                character_to_X -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_X += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_xpos = character_xpos + (character_width / 2) - (weapon_width / 2)
                weapon_ypos = character_ypos
                weapons.append([weapon_xpos, weapon_ypos])



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_X = 0


    character_xpos += character_to_X     


    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width


    #무기 위치 조정
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    #천장에 닿은 무기 없애기 
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0 ]

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #공 팅겨나오는 효과
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        
        #세로위치
        #스테이지에 팅겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    #4. 충돌처리
  

    #5. 화면에 그리기

    screen.blit(background, (0,0))

    for weapon_xpos , weapon_ypos in weapons:
        screen.blit(weapon, (weapon_xpos , weapon_ypos))
        
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))


    screen.blit(stage, (0, screen_height - stage_height))

    screen.blit(character, (character_xpos, character_ypos))

    

    pygame.display.update() #게임화면을 다시 그리기





#잠시 대기
pygame.time.delay(2000)


#pygame 종료처리
pygame.quit()