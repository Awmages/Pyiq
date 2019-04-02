import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 2 * np.pi, 0.001)
s_a0 = 5
s_f0 = 1
c_a0 = 5
c_f0 = 1
delta_f = 1.0
s = s_a0 * np.sin(2 * np.pi * s_f0 * t)
c = c_a0 * np.cos(2 * np.pi * c_f0 * t)
l, = plt.plot(t, s, lw=2, color='red')
m, = plt.plot(t, c, lw=2, color='blue')
n, = plt.plot(t, s+c, lw=2, color='purple')
plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'
saxamp = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor=axcolor)
saxfreq = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
caxamp = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
caxfreq = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

samp = Slider(saxamp, 'Sin Amp', 0.0, 5.0, valinit=s_a0)
sfreq = Slider(saxfreq, 'Sin Freq', -5.0, 5.0, valinit=s_f0, valstep=delta_f)

camp = Slider(caxamp, 'Cos Amp', 0.0, 5.0, valinit=s_a0)
cfreq = Slider(caxfreq, 'Cos Freq', -5.0, 5.0, valinit=s_f0, valstep=delta_f)


def update(val):
    s_amp = samp.val
    s_freq = sfreq.val
    c_amp = camp.val
    c_freq = cfreq.val
    l.set_ydata(s_amp * np.sin(2 * np.pi * s_freq * t))
    m.set_ydata(c_amp * np.cos(2 * np.pi * c_freq * t))
    n.set_ydata(s_amp * np.sin(2 * np.pi * s_freq * t) + c_amp * np.cos(2 * np.pi * c_freq * t))
    fig.canvas.draw_idle()


sfreq.on_changed(update)
samp.on_changed(update)
cfreq.on_changed(update)
camp.on_changed(update)


resetax = plt.axes([0.01, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
    cfreq.reset()
    camp.reset()


button.on_clicked(reset)

plt.show()
