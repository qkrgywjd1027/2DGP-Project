from pico2d import *

#pivot or origin

open_canvas()

gra = load_image('grass.png')
ch = load_image('run_animation.png')

x = 0
while x < 800:
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas() 

	x += 2
	delay(0.02)

delay(2)

close_canvas()