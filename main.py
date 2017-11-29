from matplotlib import pylab, lines, mlab
import numpy as np
from sympy import diff, symbols, cos, sin


def z_x_iy(point):
    return point.real + point.imag


def test_conditions(pr):
    x = 'x'
    func = 'x / (x**3 - x + 1)'
    func_d1 = diff(func, x)
    func_d2 = diff(func_d1, x)
    x = pr
    func_scalar = eval(str(func))
    func_d1_scalar = eval(str(func_d1))
    func_d2_scalar = eval(str(func_d2))

    func1 = pr * z_x_iy(func_d1_scalar) / z_x_iy(func_scalar)  # условие A
    if func1 != 0:
        if func1.real > 0:  # Проверка условия A
            func2 = 1 + pr * (z_x_iy(func_d2_scalar) /
                              z_x_iy(func_d1_scalar))  # условие B
            if func2.real > 0:  # Проверка условия B
                print(1)
            else:
                print(0)
        else:
            print(3)


def build(n):
    dr = 1 / n  # Расстояние
    df = (2 * np.pi) / n  # Поворот
    d = 0.1
    l = np.arange(-2, 2, d)
    X = []
    Y = []
    # рисует точки в кружке)))
    for x in l:
        for y in l:
            if x**2 + y**2 <= 1:
                X.append(x)
                Y.append(1j * y)
    # Отрисовка точек в круге

    for i in range(len(Y)):
        pylab.plot(X[i], Y[i].imag, 'b.')

    # for i in X:
    #     for j in Y:
    #         test(i + j)

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
