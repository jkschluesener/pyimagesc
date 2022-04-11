import numpy as np
import matplotlib.pylab as plt
from pyimagesc import imagesc

if __name__ == '__main__':
    
    m = np.random.rand(200, 5)
    m[9, 2] = 5
    
    fig, ax = plt.subplots(2, 1, figsize=(5, 10))
    
    fig.suptitle('imshow vs pyimagesc')
    
    ax[0].set_title('imshow')
    ax[0].imshow(m)
    
    ax[1].set_title('pyimagesc')
    imagesc(m, ax=ax[1])
    
    fig.tight_layout()
    
    fig.savefig('comparison.png')
