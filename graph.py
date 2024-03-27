import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

p = 100000
val = np.arange(-2, 2, 1 / p)
fig, ax = plt.subplots()
xdata, ydata = [0], [0]
ln, = ax.plot([], [], 'ro', markersize=10)
x_start = -1
g = 9.81


def init():
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-0.1, 1.1)
    return ln,


def f(x):
    f_val = np.sin(x) ** 2 * (np.sign(x + 1) + 1) * -(np.sign(x - .8) - 1) - 2 * (np.sign(x + 1) - 1) * np.sin(
        -1) ** 2 + 2 * np.sign(x - .8) * np.sin(.8) ** 2
    return f_val / 2.8322936730942847 + 0.4332891417126131


def f_prime(x):
    return 2 * np.sin(x) * np.cos(x)


def theta(x):
    #return -np.arctan(f_prime(x) - f_prime(x) * x / f(x) + f(x)) + np.pi / 4 * (np.sign(x) + 1)
    return -np.arctan(f_prime(x))

def update(frame):
    xdata[0] = frame
    ydata[0] = f(frame)
    ln.set_data(xdata, ydata)
    return ln,


def frames(start) -> np.ndarray:
    return_frames = np.array([start])
    speed = np.array([0., 0.])
    pos = np.array([start, f(start)])
    delta_t = .01
    mu = .5
    i = 0
    m = 1
    while True:
        x = pos[0]
        R = m * g * np.cos(theta(x)) * np.array([np.sin(theta(x)), np.cos(theta(x))])
        friction = -mu * m * g * np.array([np.sin(theta(x)), -np.sin(theta(x))])
        P = m * g * np.array([0, 1])
        acceleration = (R + friction + P) / m
        speed += acceleration * delta_t
        pos += speed * delta_t
        return_frames = np.append(return_frames, x)
        i += 1
        if i % 10000 == 0:
            print(acceleration)
            print(180 * theta(x) / np.pi)
            print(x)
        if (np.all(abs(acceleration) <= .1) and i > 1_000) or i > 100_000:
            print(speed)
            print(return_frames)
            print(i)
            break
    return return_frames


plt.plot(val, f(val))
ani = FuncAnimation(fig, update, frames=frames(-.8),
                    init_func=init, blit=True, interval=25 / 3, repeat_delay=1000)
plt.show()
