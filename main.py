from matplotlib import pylab
import numpy as np

# В добрый путь!


def build(n):
    # n - кол-во кругов, m - кол-во узлов в "круге", L - центр L=(0,0) , scale - масштаб
    dr = 1 / n  # Расстояние
    df = (2 * np.pi) / n  # Поворот
    pylab.axis('equal')  # Маштабирование - круг кругом

    k = np.arange(n + 1)  # Формируем массив

    alfa = k * df
    rad = n * dr
    z = rad * np.cos(alfa) + 1j * rad * np.sin(alfa)
    pylab.plot(z.real, z.imag, '-m.')

    a = []  # Массив для k. k не поддерживает методы pop,index
    for i in range(len(k)):
        a.append(k[i])

    b = []
    for i in range(len(a)):
        if len(a) != 1:
            b.append(a.pop(a.index(min(a))))  # [0,10,1,9,8,7...]
            b.append(a.pop(a.index(max(a))))

    for i in range(0, len(b), 2):
        if i != len(b) - 1:
            alfa_1 = b[i + 1] * df
        alfa = b[i] * df
        rad = n * dr
        z = rad * np.cos(alfa) + 1j * rad * np.sin(alfa)
        z_1 = rad * np.cos(alfa_1) + 1j * rad * np.sin(alfa_1)
        pylab.plot([z.real, z_1.real], [z.imag, z_1.imag], 'b.-')

    d = []
    j = 0
    center = int(len(k) / 2)
    for i in range(0, len(k), 5):
        d.append(k[center - j])
        d.append(k[0 + j])
        d.append(k[center * 2 - j])
        d.append(k[center + j])
        j += 1

    for i in range(0, len(d), 2):
        if i != len(d) - 1:
            alfa_1 = d[i + 1] * df
        alfa = d[i] * df
        rad = n * dr
        z = rad * np.cos(alfa) + 1j * rad * np.sin(alfa)
        z_1 = rad * np.cos(alfa_1) + 1j * rad * np.sin(alfa_1)
        pylab.plot([z.real, z_1.real], [z.imag, z_1.imag], 'b.-')


if __name__ == '__main__':

    n = 50  # Обязательно четный/нечетный иначе не работает
    main_window = pylab.figure()  # Окно с графиком
    build(n)
    mng = pylab.get_current_fig_manager()
    mng.full_screen_toggle()
    pylab.show()
