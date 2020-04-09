import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import math
import time
from matplotlib.colors import ListedColormap

#Choose gray colormap
cmap = plt.cm.gray
#Get colormap colors
my_cmap = cmap(np.arange(cmap.N))
#Set alpha (transparancy) 
my_cmap[:,-1] = [1]*cmap.N
#Create new colormap
my_cmap = ListedColormap(my_cmap)

def myimshow(I, **kwargs):
    # utility function to show image
    plt.figure(figsize=(50,22));
    plt.axis('off')
    plt.imshow(I, cmap=my_cmap,interpolation='bicubic',**kwargs)

def genSinusoid(sz, A, omega, rho):
    # Generate Sinusoid grating
    # sz: size of generated image (width, height)
    radius = (int(sz[0]/2.0), int(sz[1]/2.0))
    [x, y] = np.meshgrid(range(-radius[0], radius[0]+1), range(-radius[1], radius[1]+1)) # a BUG is fixed in this line

    stimuli = A * np.cos(omega[0] * x  + omega[1] * y + rho)
    return stimuli


theta = np.pi/4
omega = [np.cos(theta), np.sin(theta)]
sinusoidParam = {'A':1, 'omega':omega, 'rho':np.pi/2, 'sz':(100,100)}

%matplotlib qt
myimshow(genSinusoid(**sinusoidParam))

#You can ignore things below this, this was just code I was messing with
import numpy as np
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap

# Random data
data1 = np.random.random((4,4))

# Choose colormap
cmap = pl.cm.gray

# Get the colormap colors
my_cmap = cmap(np.arange(cmap.N))

# Set alpha
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)

# Create new colormap
my_cmap = ListedColormap(my_cmap)

pl.figure()
pl.subplot(121)
pl.pcolormesh(data1, cmap=pl.cm.RdBu)
pl.colorbar()

pl.subplot(122)
pl.pcolormesh(data1, cmap=my_cmap)
pl.colorbar()

#Choose gray colormap
cmap = plt.cm.gray
#Get colormap colors
my_cmap = cmap(np.arange(cmap.N))
#Set alpha (transparancy) 
my_cmap[:,-1] = np.linspace(0,1,cmap.N)
#Create new colormap
my_cmap = ListedColormap(my_cmap)




