from matplotlib import pylab, lines, mlab
import numpy as np
from sympy import diff, symbols, cos, sin

def test_conditions(pr, func, func_d1, func_d2):
    x = pr
    func = eval(str(func))
    func_d1 = eval(str(func_d1))
    func_d2 = eval(str(func_d2))
    
    if func.real < 100 and func.real > -100:
        if func.imag < 100 and func.imag > -100:
            graf1.plot(func.real, func.imag, '-g.')

    if func != 0 and func_d1 != 0:
        func1 = x * (func_d1 / func)  # условие *
        if func1.real > 0:  # Проверка условия *
            func2 = 1 + x * (func_d2 / func_d1)  # условие 0
            if func2.real > 0:  # Проверка условия 0
                graf.plot(x.real, x.imag, '-k.')
                graf1.plot(func.real, func.imag, '-k.')
            else:
                graf.plot(x.real, x.imag, '-y.')
                graf1.plot(func.real, func.imag, '-y.')
        else:
            graf.plot(x.real, x.imag, '-r.')
               
def build(n):
    dr = 1 / n  # Расстояние
    df = (2 * np.pi) / n  # Поворот
    d = 0.05
    l = np.arange(-1, 1, d)
    X = []
    Y = []    
    global graf1, graf #graf2
    graf = pylab.subplot(1,2,1)
    graf1 = pylab.subplot(1,2,2)
    #graf2 = pylab.subplot(1,3,3)

    x = 'x'
    func = 'x / (x + 1)**2'# исходная функция
    func_d1 = diff(func, x) #'(1-x)/(1+x)**3' # производная по x
    func_d2 = diff(func_d1, x) #'(-4+2*x)/(1+x)**4' # вторя производная по х
    #отображение функций
    #print(func)
    #print(func_d1)
    #print(func_d2)
    
    # заполнение массива X и iY
    for x in l:
        for y in l:
            if x**2 + y**2 < 1-0.05:
                X.append(x)
                Y.append(1j * y)

    for i in range(len(Y)):
        # Отрисовка точек в круге.
        graf.plot(X[i], Y[i].imag, '-b.')
        # Вызов функции тест.
        test_conditions(X[i] + Y[i], func, func_d1, func_d2)

    # Граница круга
    k = np.arange(n + 1)  # Формируем массив
    alfa = k * df
    rad = n * dr
    z = rad * np.cos(alfa) + 1j * rad * np.sin(alfa)
    graf.plot(z.real, z.imag, '-k.')
    #graf1.plot(z.real, z.imag, '-k.')

    graf.axis('equal')
    #graf1.axis('equal')# Маштабирование - круг кругом

n = 25
main_window = pylab.figure()  # Окно с графиком
build(n)
pylab.show()
