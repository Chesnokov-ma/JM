import matplotlib.pyplot as plt
import scienceplots
import seaborn as sns
# plt.style.use(['science', 'no-latex'])


n = 8; N = n ** 2
k = 0

folder = f'{n}on{n}'; jmax = 112; jmin = 0 #-jmax
M_avg = []; g_max_lst = []
N_max = 2 ** N

"""Обработка папки с файлами"""
for J in range(jmin, jmax + 1, 2):
    with open(f'{folder}/gem_glass{n * n}_J{J}_{k}.dat', 'r') as f:
        _skip = 4; M = []; g = []

        for line in f:
            if _skip > 0:
                _skip -= 1
            else:
                if line != '':
                    g.append(int(line.split(' ')[0]))
                    M.append(int(line.split(' ')[2]))

        plt.bar(M, g)
        plt.xlabel('M')
        plt.ylabel('g')
        # plt.ylim((0, 1))
        plt.show()
        plt.savefig(f'gM/{J}.png', dpi=500)
        plt.clf()
