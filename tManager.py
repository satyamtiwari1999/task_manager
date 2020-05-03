# importing pygame
import pygame


# initialising pygame
pygame.init()
pygame.font.init()
# colour combination that will be used :
# white, #143d59 and #f4b41a
white, blue, yellow = ((255, 255, 255), (20, 61, 89), (244, 180, 26))

# temporary tasks list
temp = ['Make Task Manger']


def gameloop():
    """Sets the game loop"""

    # defining the main screen
    y = 510  # will change dynamically after the list of event will be setup
    screen_dimention = (510, y)
    # working_screen_dimension = (500, 500)
    main_screen = pygame.display.set_mode(screen_dimention)
    pygame.display.set_caption('Task Manager')

    # making the game loop
    run_game = True
    while run_game:
        # setting display colour
        main_screen.fill(white)
        # seting the event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        for text in temp:
            font = pygame.font.SysFont('microsoftsansserif', 18, True)
            new_task = font.render(text, True, blue)
            main_screen.blit(new_task, (20, 10))

        pygame.display.update()
    print(pygame.font.get_fonts())
    pygame.quit()


if __name__ == "__main__":
    gameloop()
