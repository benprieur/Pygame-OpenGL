import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

SOMMETS = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

ARETES = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for arete in ARETES:
        for sommet in arete:
            glVertex3fv(SOMMETS[sommet])
    glEnd()

pygame.init()
ZONE = (800,800)
pygame.display.set_mode(ZONE, pygame.DOUBLEBUF|pygame.OPENGL)

gluPerspective(45, (ZONE[0]/ZONE[1]), 0.1, 50.0)
glTranslatef(0.0,0.0, -5)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

  glRotatef(1, 3, 1, 1)
  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
  Cube()
  pygame.display.flip()
  pygame.time.wait(10)

