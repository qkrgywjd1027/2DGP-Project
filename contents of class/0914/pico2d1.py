import pico2d
Pico2d is prepared.
pico2d
<module 'pico2d' from 'C:\\Users\\samsung\\lib\\site-packages\\pico2d\\__init__.py'>

from pico2d import *
open_canvas()
import os
os.getcwd()
'C:\\Users\\samsung'

os.chdir('C:/Users/samsung/Desktop/2020년 2학기/2D게임프로그래밍/0914')
os.getcwd()
'C:\\Users\\samsung\\Desktop\\2020년 2학기\\2D게임프로그래밍\\0914'

os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'hello.py', 'run_animation.png']

load_image('grass.png')
<pico2d.pico2d.Image object at 0x0000026F8B2F44C0>

gra = load_image('grass.png')
gra
<pico2d.pico2d.Image object at 0x0000026F8B287C10>

gra.draw_now(400, 50)
 ch = load_image('character.png')
ch.draw_now(400, 100)

load_image('character.png')
<pico2d.pico2d.Image object at 0x0000026F8B2EBAC0>

ch = load_image('character.png')
ch
<pico2d.pico2d.Image object at 0x0000026F8B2EB700>

ch.draw_now(400, 100)
 close_canvas()
 
