import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hoon's Game")

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/franh/OneDrive/문서/PythonGameProject/pygame_basic/background.png")


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 맨위 X 표시
            running = False

    screen.blit(background, (0,0)) #배경 그리기 blit을 통해 그림
    #screen.fill((0,0,255)) #rgb값으로 색을 채워 넣음


    pygame.display.update() #게임화면을 다시 그리기



#pygame 종료처리
pygame.quit()