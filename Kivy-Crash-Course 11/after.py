
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ListProperty
from kivy.core.window import Window
#from random import random
import random

Builder.load_string('''
<Root>:
    ClockRect:
        pos: 300, 300
    AnimRect:
        pos: 300, 300

<ClockRect>:
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

<AnimRect>:
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')

class Root(Widget):
    pass

class ClockRect(Widget):
    #velocity = ListProperty([10, 15])
    velocity = [5, 5]

    def __init__(self, **kwargs):
        super(ClockRect, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60.)

    def update(self, *args):

        self.x += self.velocity[0]
        self.y += self.velocity[1]
        #print('velocity =',self.velocity)
        #print('x,y =',self.x,self.y)
        #print(self.size)
        #print('AnimRect=',AnimRect.random_x,AnimRect.random_y)
        #if self.x < 0 or (self.x + self.width) > Window.width:
#+random
        if self.x<0 and self.velocity[0]<0:
            self.velocity[0] = random.randint(5,10)
            #print('velocity[0] =',self.velocity[0])
        elif  (self.x + self.width) > Window.width and self.velocity[0]>0:
            self.velocity[0] = -random.randint(5,10)
            #print('velocity[1] =',self.velocity[1])

        if self.y < 0 and self.velocity[1]<0:
            self.velocity[1] = random.randint(5,8)
        elif  (self.y + self.height) > Window.height and self.velocity[1]>0:
            self.velocity[1] = -random.randint(5,8)


#+rebounce
        if self.x+100>=AnimRect.random_xy[0]-10 and self.x+100<AnimRect.random_xy[0]+10 and self.velocity[0]>0:
            #print('self.x+100',self.x+100)
            if self.y+100>AnimRect.random_xy[1]-10 and self.y-100<AnimRect.random_xy[1]+10 :
                print('self.x+100',self.x+100)
                self.velocity[0]=-random.randint(10,15)
        if self.x-100>=AnimRect.random_xy[0]-10 and self.x-100<AnimRect.random_xy[0]+10 and self.velocity[0]<0:
            #print('self.x-100',self.x-100)
            if self.y+100>AnimRect.random_xy[1]-10 and self.y-100<AnimRect.random_xy[1]+10 :
                print('self.x-100',self.x-100)
                self.velocity[0]=random.randint(10,15)
        if self.y+100>=AnimRect.random_xy[1]-10 and self.y+100<AnimRect.random_xy[1]+10 and self.velocity[1]>0:
            #print('self.x+100',self.x+100)
            if self.x+100>AnimRect.random_xy[0]-10 and self.x-100<AnimRect.random_xy[0]+10 :
                print('self.y+100',self.y+100)
                self.velocity[1]=-random.randint(10,15)
        if self.y-100>=AnimRect.random_xy[1]-10 and self.y-100<AnimRect.random_xy[1]+10 and self.velocity[1]<0:
            #print('self.y-100',self.x+100)
            if self.x+100>AnimRect.random_xy[0]-10 and self.x-100<AnimRect.random_xy[0]+10 :
                print('self.y-100',self.y-100)
                self.velocity[1]=random.randint(10,15)                


class AnimRect(Widget):
	random_xy=[300,300]
	def anim_to_random_pos(self):
		Animation.cancel_all(self)
		self.random_xy[0] = int(random.random() * (Window.width - self.width))
		self.random_xy[1] = int(random.random() * (Window.height - self.height))

		anim = Animation(x=self.random_xy[0], y=self.random_xy[1],
						 duration=4,
						t='out_elastic')
		anim.start(self)

	def on_touch_down(self, touch):
		if self.collide_point(*touch.pos):
			self.anim_to_random_pos()
			#print('velocity[1] =',ClockRect.velocity[1])
			print('AnimRect=',self.random_xy)

runTouchApp(Root())

