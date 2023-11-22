import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import scienceplots
import seaborn as sns
plt.style.use(['science', 'no-latex'])

n = 8; N = n ** 2
p = 0

count = 0

folder = f'{n}on{n}'; jmax = 112; jmin = -112#-jmax
M_avg = []; g_max_lst = []

file_output = open('out.dat', 'w')
file_output.write('J\tg\tE\tM\n')

"""Обработка папки с файлами"""
for J in range(jmin, jmax + 1, 2):
    with open(f'{folder}/gem_glass{n * n}_J{J}_{p}.dat', 'r') as f:
        _skip = 4; Egs = None; M = []; g = []

        for line in f:
            if _skip > 0:
                _skip -= 1
            elif _skip == 0:
                g.append(int(line.split(' ')[0]))
                Egs = int(line.split(' ')[1])
                M.append(int(line.split(' ')[2]))   # /N
                _skip -= 1
            else:
                if int(line.split(' ')[1]) == Egs:
                    g.append(int(line.split(' ')[0]))
                    M.append(int(line.split(' ')[2]))
                else:
                    for i in range(len(M)):
                        file_output.write(f'{J/jmax}\t{g[i]}\t{Egs}\t{M[i]}\n')
                    break

        M_a = 0
        sum_m_g = []; sum_g = []

        for i in range(len(M)):
            if M[i] >= 0:
                # print(f'{g[i]}\t{M[i]}')
                sum_m_g.append(g[i] * M[i])         #  * math.e ** (-Egs - M[i])
                sum_g.append(g[i])

        M_a = sum(sum_m_g) / sum(sum_g)

        plt.bar(M, g)
        plt.xlabel('M')
        plt.ylabel('g')
        plt.title(f'J={J}')
        plt.savefig(f'gM1/{count}.png', dpi=500)
        plt.clf()

        count+=1

        # M_max = -10000; g_max = -10000
        # for i in range(len(M)):
        #     if M_max < M[i]:
        #         M_max = M[i]
        #         g_max = g[i]
        #
        # M_min = 10000; g_min = 10000
        # for i in range(len(M)):
        #     if M_min > M[i]:
        #         M_min = M[i]
        #         g_min = g[i]
        #
        # print(f'{J/jmax}\t{M_max}\t{g_max}\t{M_min}\t{g_min}')
        # g_max_lst.append(g_max)

    # print(f'{J}\t{M_a}\t{sum(sum_g)}\t{sum(M) / len(M)}')
    M_avg.append(M_a)



file_output.close()

x_axis = [j / jmax  for j in list(range(jmin, jmax + 1, 2))]

"""Построение графика"""
# df = pd.read_csv('out.dat', sep='\t')
# plt.plot(df['M'], df['g'], 'kx', markersize=1)
# plt.hist(df['M'], len(df['g']))

# plt.plot(x_axis, g_max_lst, 'kx', markersize=1)
#
# plt.title(f"g(Mmax) (M >= 0)")
# plt.xlabel('J')
# plt.ylabel('g')
# plt.savefig(f'{folder}_{p}.png', dpi=500)
# plt.show()

