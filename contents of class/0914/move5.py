from pico2d import *

#pivot or origin

open_canvas()

gra = load_image('images/grass.png')
ch = load_image('images/run_animation.png')

x = 0
frame_index = 0
while x < 800:
	clear_canvas()
	gra.draw(400, 30)
	ch.clip_draw(100 * frame_index, 0, 100, 100, x, 85)
	update_canvas() 

	get_events()
	# for e in evts:
	#	print(e)

	x += 2
	frame_index += 1
	if frame_index >= 8: 
		frame_index = 0

	delay(0.02)

delay(1)

close_canvas()
