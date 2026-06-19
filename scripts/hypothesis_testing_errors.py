"""
Script to generate a clean PGF plot illustrating
Type I (alpha) and Type II (beta) errors in hypothesis testing.
Also inclues the power of a test as the hypothesis changes.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from asd import utils


# Define parameters
x = np.linspace(-5, 8, 2000)

mu0, sigma0 = 0.0, 0.75
mu1, sigma1 = 3.0, 1.5

# Critical value for the test, found by setting the upper tail probability under H0 to alpha
alpha = 0.05
XC = norm.ppf(1 - alpha, loc=mu0, scale=sigma0)

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

ax.text(XC - 0.8, ymax*0.22, r'$\beta$', color='blue')
ax.text(XC + 0.4, ymax*0.10, r'$\alpha$', color='red')

ax.set_xlabel(r'$T(x)$')
ax.set_ylabel(r'$p(T(x))$')

ax.set_xlim(-3, 8)
ax.set_ylim(0, ymax * 1.2)

ax.set_xticks([])
ax.set_yticks([])

plt.savefig("images/hypothesis_testing_errors.pgf", bbox_inches="tight")
plt.close()

#### Power of a test graph:
# Intermediate hypotheses, I want to change mu and sigma from H0 to H1 and then some more too
# After 100 points they should be at H1, and then after 200 points they should be further to show the asymptotic limit
mus = np.linspace(mu0, 2*mu1, 200)
sigmas = np.linspace(sigma0, 2*sigma1, 200)
i = np.arange(len(mus)) # Just an index to loop through the arrays

power = 1 - norm.cdf(XC, loc=mus[i], scale=sigmas[i])

fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))

ax.plot(i, power, color='C0', lw=1.0, label=r'$\text{pow}_T(i) = 1 - \beta_\alpha(i)$')
ax.axhline(alpha, color='black', lw=1.0, linestyle='--')
ax.axhline(1, color='black', lw=1.0, linestyle='--')

ax.set_xlabel(r'Intermediate hypothesis $i$')
ax.set_ylabel(r'Power of the test: $1 - \beta_\alpha(i)$')
ax.set_title('Power of a test as the hypothesis changes')
ax.legend(loc='upper right')

ax.set_xlim(0, 200)
ax.set_ylim(0, 1.18)

# Only x tick at H0 and H1, only y tick at 0, alpha, and 1
ax.set_xticks([0, 100])
ax.set_xticklabels([r'$H_0$', r'$H_1$'])
ax.set_yticks([0, alpha, 1])
ax.set_yticklabels([0, r'$\alpha$', 1])
ax.grid(alpha=0.3)

plt.savefig("images/hypothesis_testing_power.pgf", bbox_inches="tight")
plt.close()
