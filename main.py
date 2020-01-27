from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.graphics import Line
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint


class AnimationWidget(Widget):
	"""App class to run the animation"""
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.angles = [[-90, 90] for _ in range(16)]
		self.draw_circles()

		self.anim_event = Clock.schedule_interval(lambda _: self.change_angles(), 0.05)

		self._keyboard = Window.request_keyboard(self.keyboard_closed, self, 'text')
		self.bind(on_touch_down=self.toggle_animation)
		self._keyboard.bind(on_key_down=self.on_key_down)
	
	def keyboard_closed(self, *args):
		print("Keyboard is closed")

	def on_key_down(self, keyboard, keycode, text, modifiers):
		if text == " ":
			self.toggle_animation()

	def toggle_animation(self, *args):
		if self.anim_event.is_triggered:
			self.anim_event.cancel()
		else:
			self.anim_event = Clock.schedule_interval(lambda _: self.change_angles(), 0.05)

	def change_angles(self):
		for i in range(16):
			for j in range(2):
				self.angles[i][j] += (i + 1) * 2

		self.draw_circles()

	def draw_circles(self):
		self.canvas.clear()
		with self.canvas:
			Color(rgba=(1, 1, 1, 1))
			Rectangle(pos=self.pos, size=(Window.size[0], Window.size[1]))
			Color(rgba=(0, 0, 0, 1))
			for i in range(1, 17):
				Line(width=4.5, cap="square", circle=(Window.size[0] / 2, Window.size[1] / 2, i * 10, *self.angles[i-1]))

if __name__ == "__main__":
	runTouchApp(AnimationWidget())