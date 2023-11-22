import matplotlib.pyplot as plt
import scienceplots
import seaborn as sns
plt.style.use(['science', 'no-latex'])
from math import exp, e


def float_range(start, end, step):
    ret_list = [start]
    i = start + step
    while i < end:
        ret_list.append(i)
        i += step
    return ret_list

n = 8; N = n ** 2
k = 0

folder = f'{n}on{n}'; jmax = 112; jmin = -jmax
X = 0
M_avg = []; g_max_lst = []
N_max = 2 ** N

x_axis = []; y_axis = []

T = 1

"""Обработка папки с файлами"""
for J in range(jmin, jmax + 1, 2):
    with open(f'{folder}/gem_glass{n * n}_J{J}_{k}.dat', 'r') as f:
        _skip = 4; M = []; g = []; E = []; Egs = 0

        for line in f:
            if _skip > 0:
                _skip -= 1
            else:
                if line != '':
                    g.append(int(line.split(' ')[0]))
                    E.append(int(line.split(' ')[1]))
                    M.append(int(line.split(' ')[2]))
                if _skip == 0:
                    Egs = int(line.split(' ')[1])
                    _skip -= 1

    M_gs = []; g_gs = []
    for i in range(len(M)):
        if E[i] == Egs:
            M_gs.append(M[i])
            g_gs.append(g[i])
        else:
            break

    sum_low = 0                 # знаменатель
    for i in range(len(g_gs)):
        print(g_gs[i] * e ** ((-E[i]) / T))

    P = (2 * e ** (-Egs / T))                                  #/ sum_low)     # вероятность
    print('{}\t{:.2f}\t{:.4f}\t{:.4f}'.format(J, X, 2 / sum(g_gs), P))
    x_axis.append(X)
    # y_axis.append(2 / sum(g_gs))

    X += (1 / jmax)

    # T += 0.001


# plt.plot(x_axis, y_axis, 'k.', )
# plt.xlabel('P')
# plt.ylabel('Probability')
# plt.xlabel([0, 1])
# plt.show()
# # plt.savefig(f'gM/{J}.png', dpi=500)
# plt.clf()
