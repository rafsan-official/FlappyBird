import pygame

def base_movement(window, base_img, var_x): #animated base
    window.blit(base_img, (var_x, 640 - 112))  # display base image...   var_x is move from right to left position... 640 =total screen height - base image height 112
    #second window which will join base as merge
    window.blit(base_img, (var_x+336, 640 - 112)) #here 336 = base image's width


def game_build(): #method create

    pygame.init() #initialize pygame
    window = pygame.display.set_mode((336,640)) #display size


    bkg_img = pygame.image.load("gallery\\images\\bg.png") #background load

    base_img = pygame.image.load("gallery\\images\\base.png") #base image
    var_x= 0

    #main loop
    clock = pygame.time.Clock() #control frame rate of the screen
    running = True
    while running: #while game is running then

        #event loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False #cross button click

        #game logic
        window.blit(bkg_img,(0,0)) #display background

        #base movement
        var_x-= 1
        base_movement(window, base_img,var_x) #method call

        if var_x <= -336: #when base image is gone upto it's total width 336
            var_x= 0 #then base image animation will start from begin


        clock.tick(60) #frame rate... if i take low then it will lag, if i take high value, then it will run faster

        # #updating screen
        pygame.display.update()

    pygame.quit() #uninitialize pygame

if __name__=="__main__":
    game_build() #method call