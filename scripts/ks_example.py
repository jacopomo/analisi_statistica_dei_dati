'''
Script that follows an example application of the Kolmogorov-Smirnov test, creating the 
appropriate tables and plots.
'''
import numpy as np
import matplotlib.pyplot as plt
from asd import utils
from scipy.special import erf

N = 10

# Sample N values from a standard Normal distribution (null hypothesis):
np.random.seed(12345)
x_sampled = np.random.normal(loc=0, scale=1, size=N)
x_grid = np.linspace(min(x_sampled), max(x_sampled), 1000)

# Sort the sampled values
x_sorted = np.sort(x_sampled)


# Create horizontal table of the extracted x values
fmt_x_row = [rf"${x:.2f}$" for x in x_sorted]
labels_x_row = tuple(rf"$x_{{{i+1}}}$" for i in range(N))
content_x_row = tuple([[fmt_x_row[i]] for i in range(N)])

utils.table_generator(
    n_columns=N,
    labels=labels_x_row,
    content=content_x_row,
    output_file_name="ks_x_values_row.tex"
)


# Compute the sample cumulative:
y_sampled = np.arange(1, N + 1) / N

# Compute the theoretical cumulative under the null hypothesis (standard Normal distribution)
phi_grid = 0.5 * (1 + erf(x_grid / np.sqrt(2)))

# Values of the theoretical CDF at the sorted sample points
phi_sorted = 0.5 * (1 + erf(x_sorted / np.sqrt(2)))
abs_diff = np.abs(y_sampled - phi_sorted)
D = np.max(abs_diff)
max_idx = int(np.argmax(abs_diff))

# Create table data for the KS example, bolding the max
fmt_x = [rf"${x:.2f}$" for x in x_sorted]
fmt_sample = [rf"${y:.2f}$" for y in y_sampled]
fmt_phi = [rf"${phi:.2f}$" for phi in phi_sorted]
fmt_diff = [
    r"$\mathbf{{{:.2f}}}$".format(d) if i == max_idx else rf"${d:.2f}$"
    for i, d in enumerate(abs_diff)
]

note = r"As we can see the maximum value is $D_{%d} = \mathbf{%.2f}$." % (max_idx + 1, abs_diff[max_idx])

utils.table_generator(
    n_columns=4,
    labels=(r"$x_i$", r"$S_N(x_i)$", r"$\Phi(x_i)$", r"$|S_N(x_i) - \Phi(x_i)|$"),
    content=(fmt_x, fmt_sample, fmt_phi, fmt_diff),
    output_file_name="ks_example_table.tex",
    note=note
)

# Generate plot with the sampled values, the theoretical cumulative, and the KS statistic
fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))
ax.step(x_sorted, y_sampled, where='post', label='Sample CDF', color='blue')
ax.plot(x_grid, phi_grid, label='Theoretical CDF (Standard Normal)', color='black', linestyle='--')
ax.legend()
ax.set_xlabel('Value')
ax.set_ylabel('Cumulative Probability')

ax.grid(alpha=0.3)

ax.set_title('Kolmogorov-Smirnov Test Example')
plt.savefig("images/ks_example.pgf", bbox_inches='tight')
plt.close()

