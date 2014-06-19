#!/usr/bin/env python

import subprocess
from StringIO import StringIO

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# Compile and run Fortran program
subprocess.call('gfortran quadrature.f90 -o quadrature', shell=True)
quadrature = subprocess.check_output('./quadrature')

# Load data
order, range = np.loadtxt(StringIO(quadrature), unpack=True)

# Make plot
plt.plot(order, range, 'k.')
plt.xlabel('Gauss-Hermite polynomial order', fontsize=16)
plt.ylabel('Largest root of Gauss-Hermite polynomial', fontsize=16)
plt.grid(True, color='lightgray', ls='-', alpha=0.7)
plt.gca().set_axisbelow(True)
plt.savefig('quadrature.pdf', bbox_inches='tight')
plt.close()
