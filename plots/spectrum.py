#!/usr/bin/env python

import sys
sys.path.insert(0, '../testing/beavrs')

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from statepoint import StatePoint

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# Make sure argument was given
if len(sys.argv) < 2:
    sys.exit('Need to specify statepoint')

# Load data from statepoint
sp = StatePoint(sys.argv[1])
sp.read_results()
energy = 1e6*np.array(sp.tallies[0].filters['energyin'].bins)
flux = sp.extract_results(0, 'flux')['mean']
flux = np.insert(flux, 0, 0.0)

# Make log-log plot with error bars
plt.step(energy, flux, 'k')
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.grid(True, color='lightgray', ls='-', alpha=0.7)
plt.xlabel('Energy (eV)', fontsize=16)
plt.ylabel('Flux (neutron/cm$^3$/source-neutron)', fontsize=16)
plt.xlim((1e-5,20e6))
plt.gca().set_axisbelow(True)
plt.savefig('spectrum.pdf', bbox_inches='tight')
