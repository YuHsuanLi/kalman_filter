import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frame_size = 480
ball_size = 30 #radis
ball_init_position = (200, 200)
ball_init_vel = (100, 200)
dt = 0.02
total_time = 10 #s
fps = int(1/dt)
total_frame = total_time*fps
circle = plt.Circle(ball_init_position, ball_size, color='r')
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim([0, frame_size])
ax.set_ylim([0, frame_size])

class Ball():
	def __init__(self, ax):
		self.ax = ax
		self.x = ball_init_position[0]
		self.y = ball_init_position[1]
		self.vx = ball_init_vel[0]
		self.vy = ball_init_vel[1]

	def init(self):
		self.ax.add_patch(circle)
		return circle,

	def update(self, t):
		self.x = self.x + dt*self.vx
		self.y = self.y + dt*self.vy
		if self.x - ball_size <= 0:
			self.x = ball_size
			self.vx = -self.vx
		if self.y - ball_size <= 0:
			self.y = ball_size
			self.vy = -self.vy
		if self.x + ball_size >= frame_size:
			self.x = frame_size - ball_size
			self.vx = -self.vx
		if self.y + ball_size >= frame_size:
			self.y = frame_size - ball_size
			self.vy = -self.vy
	
		circle.center = (self.x, self.y)
		return circle,
	
	def animate(self):
		ani = FuncAnimation(fig, self.update, frames=total_frame, init_func=self.init, blit=True)
		plt.show()
		#ani.save('ball.gif', writer='imagemagick', fps=fps)

ball = Ball(ax)
ball.animate()