import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import waveEquation
import tqdm


#example propogation speed field
def mGen(x, y):
    m = np.zeros((x, y))

    for a in range(x):
        for b in range(y):
            m[a,b] = (3 + abs(a - 50) + abs(b - 250))

    return m

#second example propogation speed field
def filter(x, y):
    m = np.ones((x,y)) * 3

    l = 0.1

    #a is x, b is y (a is vertical, b is horizontal)
    for a in range(20, 30):
        for b in range(500):
            if(b % 25 == 0 and l == 3):
                l = 0.1
            elif(b % 25 == 0 and l == 0.1):
                l = 3

            m[a,b] = l

    
    return m


#initializing wave propagation speed field
sizex = 100
sizey = 500
O = mGen(sizex, sizey) #can be replaced with filter() propogation field for different results

#wave stop time
stopWaveTime = 3140

#intializing simulation
sim = waveEquation.WaveSim(sizex, sizey, 0.2, O, stopWaveTime, 0.001)

#intializing matplotlib visualizations
fig, pic = plt.subplots()
imageArr = []
imageGap = 50 #number of simulation iterations between saved images for animation. Setting to 1 means all iterations are saved.

for x in tqdm.tqdm(range(63001)):
    sim.iterate(x)

    #saving an image of the simulation after specified interval of iterations (imageGab variable)
    if(x%imageGap == 0):
        im = pic.imshow(sim.field[:,:], extent=(0, sizey-1, sizex-1, 0),
            interpolation='nearest', cmap=cm.gist_rainbow, vmin=-1, vmax=1, animated=True)
        imageArr.append([im])


ani = animation.ArtistAnimation(fig, imageArr, interval=50, blit=True,
                                repeat_delay=1000)

#saving video of the simulation
ffwriter = animation.FFMpegWriter()
ani.save('test.mp4', writer=ffwriter)

plt.show()
