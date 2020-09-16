from pico2d import *

open_canvas()

gra = load_image('images/grass.png')
ch = load_image('images/character.png')

gra.draw_now(400, 30)
ch.draw_now(400, 85)

delay(4)

close_canvas()
