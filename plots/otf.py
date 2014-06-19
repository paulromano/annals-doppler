#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

nucs, t0, t = np.loadtxt('../testing/beavrs/runtime-study/output_2014-04-08-075152.txt', unpack=True)
plt.plot(nucs, t/t0, 'k.')
plt.xlabel('Number of nuclides in fuel', fontsize=16)
plt.ylabel(r'Fractional increase in run time with Doppler broadening', fontsize=16)
plt.grid(True, color='lightgray', ls='-', alpha=0.7)
plt.gca().set_axisbelow(True)
plt.savefig('otf.pdf', bbox_inches='tight')
