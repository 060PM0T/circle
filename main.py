from matplotlib import pylab, lines, mlab
import numpy as np
from sympy import diff, symbols, cos, sin

def test(pr):
    func = pr / (pr**3 - pr + 1)
    funcDpr1 = diff(func) #первая производная от функции
    funcDpr2 = diff(funcDpr1) #вторая производная от функции
    func1 = pr * funcDpr1 / func # условие A
    if func1.real > 0: # Проверка условия A
        func2 = 1+ rp * (funcDpr2 / funcDpr1) # условие B
        if func2.real > 0: # Проверка условия B
            return 1
        else:
            return 0
    else:
        return 0
    
def build(n):
    # n - кол-во кругов, m - кол-во узлов в "круге", L - центр L=(0,0) , scale - масштаб
    dr = 1 / n  # Расстояние
    df = (2 * np.pi) / n  # Поворот
    d = 0.1
    l = np.arange(-1,1,d)
    X = []
    Y = []
    # рисует точки в кружке)))
    for x in l:
        for y in l:
            if x**2 + y**2 < 1:
                X.append(x)
                Y.append(y)
    # Отрисовка точек в круге
    pylab.plot(X, Y, 'b.')

    for
    test()
    k = np.arange(n + 1)  # Формируем массив
    alfa = k * df
    rad = n * dr
    z = rad * np.cos(alfa) + 1j * rad * np.sin(alfa)
    pylab.plot(z.real, z.imag, '-k.')

    pylab.axis('equal')  # Маштабирование - круг кругом
    
if __name__ == '__main__':
    
    n = 25
    main_window = pylab.figure()  # Окно с графиком
    build(n)
    pylab.show()
    

    
