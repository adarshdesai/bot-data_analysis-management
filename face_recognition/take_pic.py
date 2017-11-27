import pygame
import pygame.camera
import time
import os 
base_dir = os.path.dirname(os.path.realpath(__file__))
pic_dir=os.path.join(base_dir,'unknown/img.jpg')
pygame.camera.init()
pygame.camera.list_cameras()
cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()
time.sleep(10)  # You might need something higher in the beginning
img = cam.get_image()
pygame.image.save(img, pic_dir)
cam.stop()
