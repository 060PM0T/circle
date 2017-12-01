from matplotlib import pylab, lines, mlab
import numpy as np
from sympy import diff, symbols, cos, sin

def test_conditions(pr, func, func_d1, func_d2):
    x = pr
    print(pr)
    func_scalar = eval(str(func))
    func_d1_scalar = eval(str(func_d1))
    func_d2_scalar = eval(str(func_d2))
    print(func_scalar)
    
    if func_scalar != 0:
        func1 = pr * (func_d1_scalar / func_scalar)  # условие A
        print (func1)
        if func1 != 0:
            if func1.real > 0:  # Проверка условия A
                func2 = 1 + pr * (func_d2_scalar /
                                  func_d1_scalar)  # условие B
                if func2.real > 0:  # Проверка условия B
                    #print(func2)
                    graf1.plot(func2.real, func2.imag, '-k.')


def build(n):
    dr = 1 / n  # Расстояние
    df = (2 * np.pi) / n  # Поворот
    d = 0.1
    l = np.arange(-1, 1, d)
    X = []
    Y = []
    graf = pylab.subplot(1,2,1)
    global graf1
    graf1 = pylab.subplot(1,2,2)

    x = 'x'
    func = 'x / (x + 1)'# исходная функция
    func_d1 = diff(func, x) # производная по x
    func_d2 = diff(func_d1, x) # вторя производная по х
    #отображение функций
    #print(func)
    #print(func_d1)
    #print(func_d2)
    
    # рисует точки в кружке)))
    for x in l:
        for y in l:
            if x**2 + y**2 < 1:
                X.append(x)
                Y.append(1j * y)

    # Отрисовка точек в круге
    for i in range(len(Y)):
        graf.plot(X[i], Y[i].imag, '-b.')
        #вызов функции тест
        test_conditions(X[i] + Y[i], func, func_d1, func_d2)

    #Точки в кручке
    k = np.arange(n + 1)  # Формируем массив
    alfa = k * df
    rad = n * dr
    z = rad * np.cos(alfa) + 1j * rad * np.sin(alfa)
    graf.plot(z.real, z.imag, '-k.')
    #graf1.plot(z.real, z.imag, '-k.')

    graf.axis('equal')
    #graf1.axis('equal')# Маштабирование - круг кругом


if __name__ == '__main__':
    n = 25
    main_window = pylab.figure()  # Окно с графиком
    build(n)
    pylab.show()
