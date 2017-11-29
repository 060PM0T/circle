from matplotlib import pylab, lines, mlab
import numpy as np
from sympy import diff, symbols, cos, sin

def test(pr):
    x = 'x'
    func = 'x / (x**3 - x + 1)'
    x = pr
    print(eval(str(func)))
    x = 'x'
    funcDpr1 = diff(func,x) #первая производная от функции
    x = pr
    print(eval(str(funcDpr1)))
    x = 'x'
    funcDpr2 = diff(funcDpr1,x) #вторая производная от функции
    x = pr
    print(eval(str(funcDpr2)))
    
    func1 = pr * any(funcDpr1) / any(func) # условие A
    if func1 != 0:        
        if func1.real > 0: # Проверка условия A
            func2 = 1+ rp * (funcDpr2 / funcDpr1) # условие B
            if func2.real > 0: # Проверка условия B
                print(1)
            else:
                print(0)
        else:
            print(0)
        
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
                iy = y * 1j
                Y.append(iy)
                
    # Отрисовка точек в круге

    for i in range(len(Y)):
        pylab.plot(X[i], Y[i].imag, 'b.')

    for i in X:
        for j in Y:
            test(i + j)

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
    

    
