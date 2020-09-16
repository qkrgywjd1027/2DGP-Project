from pico2d import *

#pivot or origin

open_canvas()

gra = load_image('images/grass.png')
ch = load_image('images/character.png')

x = 0
while x < 800:
	clear_canvas_now()
	gra.draw_now(400, 30)
	ch.draw_now(x, 85)
	x += 2
	delay(0.02)

delay(2)

close_canvas()
