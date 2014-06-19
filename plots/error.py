#!/usr/bin/env python

from __future__ import print_function

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = '\usepackage[bitstream-charter]{mathdesign}'
matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# Load data into dictionary
results = {}
reactions = {}
orders = set()
for line in open('../testing/gauss-hermite/accuracy.txt', 'r'):
    words = line.split()
    order = int(words[0])
    nuclide = words[1]
    temp = float(words[2])
    reaction = words[3]
    maxerror = float(words[4])
    interror = float(words[5])

    if (nuclide,temp,reaction) not in results:
        results[nuclide,temp,reaction] = {'maxerror': [], 'interror': []}
    if nuclide not in reactions:
        reactions[nuclide] = set()
    reactions[nuclide].add(reaction)
    orders.add(order)

    results[nuclide,temp,reaction]['maxerror'].append(maxerror)
    results[nuclide,temp,reaction]['interror'].append(interror)

color = {600: 'k', 900: 'b', 1200: 'r'}
abscissa = range(min(orders), max(orders) + 1)

# Plot results for each nuclide and temperature
for nuclide in ['U238', 'U235', 'U233', 'TH232', 'PU239', 'PU240', 'FE56', 'O16']:
    for reaction in reactions[nuclide]:
        print('Writing error_{0}_{1}.pdf'.format(nuclide,reaction))
        for temp in [600.0, 900.0, 1200.0]:
            res = results[nuclide,temp,reaction]

            # Plot maximum error
            plt.semilogy(abscissa, res['maxerror'], color[temp]+'-',
                         label='{0} K'.format(temp))
            plt.semilogy(abscissa, [abs(i) for i in res['interror']],
                         color[temp]+'--')

        plt.xlabel('Gauss-Hermite quadrature order', fontsize=16)
        plt.ylabel('Relative error', fontsize=16)
        plt.xlim((min(orders), max(orders)))
        plt.grid(True, color='lightgray', ls='-', alpha=0.7)
        plt.gca().set_axisbelow(True)
        plt.legend()
        plt.savefig('error_{0}_{1}.pdf'.format(nuclide,reaction), bbox_inches='tight')
        plt.close()
