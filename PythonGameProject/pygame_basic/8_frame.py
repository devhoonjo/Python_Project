import pygame
#################################################3
#기본 초기화 반드시 해야함
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoon's Game")

#FPS
clock = pygame.time.Clock()

###############################3
#1. 사용자 게임 초기화(배경화면, 좌표, 속도, 게임 이미지, 좌표, 폰트, 시간 등)






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



    pygame.display.update() #게임화면을 다시 그리기



#잠시 대기
pygame.time.delay(2000)


#pygame 종료처리
pygame.quit()