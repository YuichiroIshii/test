# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'qt')

import neuron
from neuron import h

"""
a simple hh cell
"""

tstop = 200
v_init = -65

soma = h.Section()
soma.diam = 30
soma.L = 30
soma.insert('hh')

cvode = h.CVode()
cvode.active(1)
cvode.atol(1.0e-5)

vv = h.Vector()
tv = h.Vector()
vv.record(soma(0.5)._ref_v)
tv.record(h._ref_t)

h.finitialize(v_init)
h.fcurrent()
neuron.run(tstop)

ax = plt.subplot()
ax.set_ylim([-80, 40])
ax.plot(tv.as_numpy(), vv.as_numpy())

plt.xlabel('Time (ms)')
plt.ylabel('potential (mV)')
plt.savefig('./figs/n01.pdf')
plt.show()
