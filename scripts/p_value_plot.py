'''
Script that generates a plot to visualize the properties of p-values, 
especially the fact that they are uniformly distributed under the null hypothesis.
'''
import numpy as np
import matplotlib.pyplot as plt
from asd import utils


x_grid = np.linspace(0, 1, 1000)
H_0 = np.ones_like(x_grid)  # Under H0, p-values are uniformly distributed
H_1 = 1.6 * (0.12*np.sin(np.cos(2 * np.pi * x_grid)) ** 2 + 1 - x_grid)  # Under H1, p-values are not uniform

# Generate plot
fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))

ax.plot(x_grid, H_0, linewidth=1, ls="--", label=r"$H_0$: Uniform distribution", color='black')
ax.plot(x_grid, H_1, linewidth=1, label=r"$H_1$: Non-uniform distribution", color="C0")
ax.axvline(0.05, color="red", ls=":", lw=1.0, label=r"Significance level $\alpha = 0.05$")
ax.legend(loc="upper right")

ax.set_xlabel('$p$-value')
ax.set_ylabel(r'$p(p\text{-value})$')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.8)
ax.set_xticks([0, 0.05, 0.5, 1])
ax.set_xticklabels(['0', '0.05', '0.5', '1'])
ax.set_yticks([0, 0.5, 1, 1.5])
ax.set_yticklabels(['0', '0.5', '1', '1.5'])

ax.grid(alpha=0.3)

ax.set_title('Distribution of p-values under $H_0$ and $H_1$')
plt.savefig("images/p_value_plot.pgf", bbox_inches='tight')
plt.close()
