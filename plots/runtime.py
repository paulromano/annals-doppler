#!/usr/bin/env python

from StringIO import StringIO
import subprocess

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# Get runtimes
output = subprocess.check_output("""
for order in {5..30}; do
    echo $order $(cat ../testing/gauss-hermite/runtime-$order.txt | grep broadening | awk '{print $4}')
done
""", shell=True, executable='/bin/bash')

# Plot GH order versus execution time
order, runtime = np.loadtxt(StringIO(output), unpack=True)
plt.plot(order, runtime, 'k.')
plt.xlabel('Gauss-Hermite quadrature order', fontsize=16)
plt.ylabel('Exeuction time (s)', fontsize=16)
plt.xlim([0,30])
plt.ylim([0,3])
plt.grid(True, color='lightgray', ls='-', alpha=0.7)
plt.gca().set_axisbelow(True)
plt.savefig('runtime.pdf', bbox_inches='tight')
plt.close()
