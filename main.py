import pygame

def game_build(): #method create

    pygame.init() #initialize pygame
    window = pygame.display.set_mode((360,640)) #display size
    bkg_img = pygame.image.load("gallery\\images\\bg.png") #background load

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
        clock.tick(60) #frame rate... if i take low then it will lag, if i take high value, then it will run faster

        # #updating screen
        pygame.display.update()

    pygame.quit() #uninitialize pygame

if __name__=="__main__":
    game_build() #method call