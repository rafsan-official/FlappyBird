import pygame

def base_movement(window, base_img, var_x): #animated base
    window.blit(base_img, (var_x, 640 - 112))  # display base image...   var_x is move from right to left position...
    # 640 =total screen height - base image height 112
    window.blit(base_img, (var_x+336, 640 - 112)) #here 336 = base image's width
    # second window which will join base as merge... that's why x+336... 337 no pt will show 0 of image.. see down

def bird_momvent(window, bird_img, bird_rect):
    window.blit(bird_img,bird_rect) #display bird image

def game_build(): #function create for game build

    pygame.init() #initialize pygame
    window = pygame.display.set_mode((336,640)) #display size

    #background music
    pygame.mixer.init() #initialize music
    pygame.mixer.music.load("gallery\\music\\rafsan.mp3") #music selection
    pygame.mixer.music.set_volume(0.5) # range will be 0 to 1.. depends on volume
    pygame.mixer.music.play(3) # 3 times continious play... if i put nothing... then it will play 1 time...

    bkg_img = pygame.image.load("gallery\\images\\bg.png") #background load
    base_img = pygame.image.load("gallery\\images\\base.png") #base image
    var_x= 0

    # bird
    bird_img = pygame.image.load("gallery\\images\\bird.png") #bird image load
    bird_rect = bird_img.get_rect(center=(336/2,640/2)) #get rectangle function, 336/2. 640/2 will place the bird in center
    #center means... image will displayed from center

    #main loop
    clock = pygame.time.Clock() #control frame rate of the screen
    running = True
    while running: #while game is running then

        #event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False #cross button click

        #game logic
        window.blit(bkg_img,(0,0)) #display background... imagine graph pt(0,0) is center

        #base movement
        var_x-= 1
        base_movement(window, base_img,var_x) #call of base movement func

        if var_x <= -336: #when base image is gone upto it's total width 336
            var_x= 0 #then base image animation will start from begin

        # bird movment
        bird_momvent(window, bird_img, bird_rect) #call the bird movement function

        clock.tick(60) #frame rate... if i take low then it will lag, if i take high value, then it will run faster ....60fps

        # updating screen
        pygame.display.update()

    pygame.quit() #uninitialize pygame

if __name__=="__main__":
    game_build() #call of game build func