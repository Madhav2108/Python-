import numpy as np
import matplotlib.pyplot as p1
#***********************
a=np.arange(0,10,0.1)
x=np.cos(a)
y=np.sin(a)
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(a,x,'b',linewidth=5,linestyle='dashed')# dashed,solid,dashdot,dotted
p1.plot(a,y,'r',linewidth=2)
p1.show()
#******************
import numpy as np
import matplotlib.pyplot as plt
color = 'cornflowerblue'
points = np.ones(5)  # Draw 5 points for each line
text_style = dict(horizontalalignment='right', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'monospace'})
def format_axes(ax):
    ax.margins(0.2)
    ax.set_axis_off()
fig, ax = plt.subplots()

linestyles = ['-', '--', '-.', ':']
for y, linestyle in enumerate(linestyles):
    ax.text(-0.1, y, repr(linestyle), **text_style)
    ax.plot(y * points, linestyle=linestyle, color=color, linewidth=3)
    format_axes(ax)
    ax.set_title('line styles')

plt.show()
#***********************
a=np.arange(0,10,0.1)
x=np.cos(a)
y=np.sin(a)
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(a,x,'b',linewidth=5,linestyle=':')# '-', '--', '-.', ':'
p1.plot(a,y,'r',linewidth=2)
p1.show()
#******************
a=np.arange(0,10,0.1)
x=np.cos(a)
y=np.sin(a)
print(x)
print(y)
p1.xlabel("DATA FROM A")
p1.ylabel("DATA FROM B")
p1.title("DATA ALL")
p1.plot(x, y, 'go--', linewidth=2, markersize=12)
p1.show()
#******************

import plotly.plotly as py
import plotly.tools as tls

import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle

lines = ["-","--","-."]
linecycler = cycle(lines)
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(10):
    x = range(i,i+10)
    ax.plot(range(10),x,next(linecycler))

ax.set_title('Cycling through line styles in matplotlib')

plotly_fig = tls.mpl_to_plotly( fig )
py.iplot(plotly_fig, filename='mpl-cycle-linestyles')
