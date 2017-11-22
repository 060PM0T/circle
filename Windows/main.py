from matplotlib import pylab, lines
import numpy as np

def build(n):
    # n - кол-во кругов, m - кол-во узлов в "круге", L - центр L=(0,0) , scale - масштаб
    dr = 1 / n  # Расстояние
    df = (2 * np.pi) / n  # Поворот

    k = np.arange(n + 1)  # Формируем массив

    alfa = k * df
    rad = n * dr
    z = rad * np.cos(alfa) + 1j * rad * np.sin(alfa)
    pylab.plot(z.real, z.imag, '-m.')

    pylab.axis('equal')  # Маштабирование - круг кругом
    
if __name__ == '__main__':
    
    n = 25
    main_window = pylab.figure()  # Окно с графиком
    build(n)
    pylab.show()
    

    
