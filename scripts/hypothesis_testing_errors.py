"""
Script to generate a clean PGF plot illustrating
Type I (alpha) and Type II (beta) errors in hypothesis testing.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from asd import utils


# Define parameters
x = np.linspace(-5, 8, 2000)

mu0, sigma0 = 0.0, 0.75
mu1, sigma1 = 3.0, 1.5

XC = 1.5

pdf_H0 = norm.pdf(x, mu0, sigma0)
pdf_H1 = norm.pdf(x, mu1, sigma1)


# Generate plot
fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))

ax.plot(x, pdf_H0, color='black', lw=1.0)
ax.plot(x, pdf_H1, color='black', lw=1.0)

mask_left = x < XC
mask_right = x > XC

ax.fill_between(
    x[mask_left], pdf_H1[mask_left],
    color='blue', alpha=0.6, label=r'$\beta$',
    hatch='///'
)

ax.fill_between(
    x[mask_right], pdf_H0[mask_right],
    color='red', alpha=0.6, label=r'$\alpha$',
    hatch='XXX'
)

ax.axvline(XC, color='black', lw=1.0, linestyle='--')

ymax = max(pdf_H0.max(), pdf_H1.max())

ax.text(mu0, norm.pdf(mu0, mu0, sigma0)*1.1, r'$p(T(x) | H_0)$', 
        ha='center')
ax.text(mu1, norm.pdf(mu1, mu1, sigma1)*1.1, r'$p(T(x) | H_1)$', 
        ha='center')

ax.text(XC - 0.8, ymax*0.25, r'$\beta$', color='blue')
ax.text(XC + 0.3, ymax*0.10, r'$\alpha$', color='red')

ax.set_xlabel(r'$T(x)$')
ax.set_ylabel(r'$p(T(x))$')

ax.set_xlim(-3, 8)
ax.set_ylim(0, ymax * 1.2)

ax.set_xticks([])
ax.set_yticks([])

plt.savefig("images/hypothesis_testing_errors.pgf", bbox_inches="tight")
plt.close()
