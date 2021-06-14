import pygame
import mainwindow

if __name__ == "__main__":
	pygame.init()
	Screen = mainwindow.Screen(700, 500)
	Screen.mainloop()