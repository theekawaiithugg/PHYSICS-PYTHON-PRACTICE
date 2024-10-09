#ANIMATION PARACTICE ALEXIS MARTINEZ 10/08/2024
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation, rc
from IPython.display import HTML #USED ON JUPYTER THROUGH ANACONDA

fig, ax = plt.subplots()

ax.set_xlim((0,2))
ax.set_ylim((-2,2))

line, = ax.plot([],[],lw =2)

def init():
        # Initialize the plot here
    line.set_data([],[])
    return(line,)

def animate(i):
        #update the plot for each frame
    x = np.linspace(0,2,1000)
    y = np.sin(2*np.pi *(x-0.01 *i))
    line.set_data(x,y)
    return(line,)

ani = animation.FuncAnimation(fig, animate, init_func = init, frames =100,interval =20, blit = True)
# To show the animation in VSCode
plt.show()

# If you want to save the animation as a file (optional)
# ani.save('animation.mp4', writer='ffmpeg')

#HTML (ani.to_html5_video()) #USED ON JUPYTER THROUGH ANACONDA