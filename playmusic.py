import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')

# Play the music
pygame.mixer.music.play()

pygame.event.wait()
# Keep the program running until the user closes the window
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Adjust the tick rate as needed

# Clean up resources
pygame.quit()
