import pygame, random

def pause():
    paused = True
    pygame.mixer.music.pause() #music pause

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() #if i press cross button during pause, it will quit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False #if i press c during pause, it will resume
                    pygame.mixer.music.unpause() #music unpause

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit() #if i press q during pause, then it will quit

def base_movement(window, base_img, var_x): #animated base
    window.blit(base_img, (var_x, 640 - 112))  # display base image...   var_x is move from right to left position...
    # 640 =total screen height - base image height 112
    window.blit(base_img, (var_x+1008, 640 - 112)) #here 1008 = base image's width
    # second window which will join base as merge... that's why x+1008... 1009 no pt will show 0 of image.. see down

def bird_movement(window, bird_img, bird_rect):
    window.blit(bird_img,bird_rect) #display bird image

def pipe_movement(window, pipes, pipe_img):

    for pipe in pipes:
        pipe.centerx -= 5

    for pipe in pipes:
        window.blit(pipe_img, pipe) #show pipes

def collision(pipes, bird_rect): #collision function
    for pipe in pipes:
        if pipe.colliderect(bird_rect):
            print("Collided")

    #upper & lower bound hit
    if bird_rect.top <= -5:
        print("Exceeded Upper Limit")

    if bird_rect.bottom >= 640-112:
        print("Exceeded Lower Limit")

#--------------------------------------------------------------------------------------------------------#

def game_build(): #function create for game build

    pygame.init() #initialize pygame
    window = pygame.display.set_mode((1080,640)) #display size

    #background music
    pygame.mixer.init() #initialize music
    pygame.mixer.music.load("gallery\\music\\rafsan.mp3") #music selection
    pygame.mixer.music.set_volume(0.25) # range will be 0 to 1.. depends on volume
    pygame.mixer.music.play(3) # 3 times continious play... if i put nothing... then it will play 1 time...

    bkg_img = pygame.image.load("gallery\\images\\bg_image.png") #background load
    base_img = pygame.image.load("gallery\\images\\base_image.png") #base image
    var_x= 0

    # bird
    bird_img = pygame.image.load("gallery\\images\\bird.png") #bird image load
    bird_rect = bird_img.get_rect(center=(75,640/2)) #get rectangle function, 336/2. 640/2 will place the bird in center
    #center means... image will displayed from center
    g_force = 1
    bird_new_pos = 640/2 #total screen height/2 ... bird will start from middle of screen

    #pipes
    pipe_img = pygame.image.load("gallery\\images\\pipe.png")
    list_of_pipe = []

    TIMER = pygame.USEREVENT
    pygame.time.set_timer(TIMER, 1000)


    #main loop
    clock = pygame.time.Clock() #control frame rate of the screen
    running = True
    while running: #while game is running then
        print(list_of_pipe)

        #event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False #cross button click

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                     bird_new_pos -= 25

                if event.key == pygame.K_p:
                    pause() #call of pause function

            if event.type == TIMER:
                random_pipe_height = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050] #pipe height
                pipes = pipe_img.get_rect(midtop = (1080,random.choice(random_pipe_height)))
                list_of_pipe.append(pipes) #show the list of pipes


        #game logic
        window.blit(bkg_img,(0,0)) #display background... imagine graph pt(0,0) is center

        #collition
        collision(list_of_pipe, bird_rect)

        # pipe movement
        pipe_movement(window, list_of_pipe, pipe_img)

        #base movement
        var_x-= 1
        base_movement(window, base_img,var_x) #call of base movement func

        if var_x <= -336: #when base image is gone upto it's total width 336
            var_x= 0 #then base image animation will start from begin

        # bird movment
        bird_new_pos += g_force
        bird_rect.centery = bird_new_pos
        bird_movement(window, bird_img, bird_rect) #call the bird movement function

        # updating screen
        clock.tick(60) #frame rate... if i take low then it will lag, if i take high value, then it will run faster ....60fps
        pygame.display.update()

    pygame.quit() #uninitialize pygame

#--------------------------------------------------------------------------------------------------------#

if __name__=="__main__":
    game_build() #call of game build func