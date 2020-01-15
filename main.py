from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.graphics import Line
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.core.window import Window


class AnimationWidget(Widget):
	"""App class to run the animation"""
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.circles = []
		self.draw_circles(Window, *Window.size)
		Window.bind(on_resize=self.draw_circles)
	
	def draw_circles(self, window, width, height):

		with self.canvas:
			Color(rgba=(1, 1, 1, 1))
			Rectangle(pos=self.pos, size=(width, height))
			for circle in self.circles:
				self.canvas.remove(circle)
			self.circles = []
			for i in range(1, 17):
				Color(rgba=(0, 0, 0, 1))
				self.circles.append(Line(width=4.5, cap="square", circle=(width / 2, height / 2, i * 10, -90, 90)))



if __name__ == "__main__":
	runTouchApp(AnimationWidget())