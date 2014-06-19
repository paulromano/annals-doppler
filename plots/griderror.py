#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt

from ndlibrary import NdLibrary

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

lib1 = NdLibrary('../testing/exact/ND_LIBRARY.h5')
lib2 = NdLibrary('../testing/gauss-hermite/ND_LIBRARY.h5')

sigma1 = lib1.get_reaction('U238', 1200, 18)
sigma2 = lib2.get_reaction('U238', 1200, 18)
difference = (sigma2[1] - sigma1[1])/sigma1[1]

plt.semilogx(sigma1[0], difference)
plt.xlabel('Energy (eV)', fontsize=16)
plt.ylabel('Relative error', fontsize=16)
plt.xlim((1e-5,2e7))
plt.grid(True, color='lightgray', ls='-', alpha=0.7)
plt.gca().set_axisbelow(True)
plt.savefig('griderror.pdf', bbox_inches='tight')

