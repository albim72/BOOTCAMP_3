import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
from mandelbrotset import mandelbrot_set

def main():
    xmin,xmax,xn = -2.25,+0.75,3000
    ymin,ymax,yn = -2.25,+1.25,2500
    maxiter = 200
    horizon = 2.0**40
    log_horizon = np.log2(np.log(horizon))
    Z,N = mandelbrot_set(xmin,xmax,ymin,ymax,xn,yn,maxiter,horizon)

    with np.errstate(invalid='ignore'):
        M = np.nan_to_num(N+1-np.log2(np.log(abs(Z)))+log_horizon)

    dpi=72
    width=10
    height = 10*yn/xn
    fig = plt.figure(figsize=(width,height),dpi=dpi)
    ax = fig.add_axes([0,0,1,1],frameon=False,aspect=1)

    light = colors.LightSource(azdeg=315,altdeg=10)
    M = light.shade(M,cmap=plt.cm.hot, vert_exag=1.5,norm=colors.PowerNorm(0.3),blend_mode='hsv')

    ax.imshow(M,extent=[xmin,xmax,ymin,ymax],interpolation='bicubic')
    ax.set_xticks([])
    ax.set_yticks([])

    year = time.strftime("%Y")
    text = (f"Fraktal Zbioru Mandelbrodta\n"
            f"Renderowany za pomocą matplotlib {matplotlib.__version__} {year}\n")
    ax.text(xmin+.25,ymin+.25,text,color="white",fontsize=12,alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()
