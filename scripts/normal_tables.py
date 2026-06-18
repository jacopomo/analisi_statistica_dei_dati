'''
Script to generate tables for the normal distribution, including:
1. A table mapping significance levels (alpha) to critical sigma values.

'''
from scipy.stats import norm
import numpy as np
from asd import utils
import matplotlib.pyplot as plt

# TABLE 1: alpha (significance level) → sigma (critical sigma-value)
alpha_values = [0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.001]

alpha_col = [f"${alpha}$" for alpha in alpha_values]
sigma_col = []

for alpha in alpha_values:
    # Find sigma-value such that P(Z > sigma) = alpha (right tail)
    sigma_value = norm.ppf(1 - alpha)
    formatted = utils.number_formatter(sigma_value, 3)
    sigma_col.append(formatted)

labels_1 = ("$\\alpha$", "$\\sigma$")
content_1 = (alpha_col, sigma_col)

utils.table_generator(
    n_columns=len(labels_1),
    labels=labels_1,
    content=content_1,
    output_file_name="normal_table_a.tex"
)

# TABLE 2: sigma (critical sigma-value) → alpha (right tail area)
sigma_values = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

sigma_col_2 = [f"${sigma}$" for sigma in sigma_values]
alpha_col_2 = []

for sigma in sigma_values:
    # Calculate right tail probability at sigma
    tail_area = 1 - norm.cdf(sigma)
    formatted = utils.number_formatter(tail_area, 3)
    alpha_col_2.append(formatted)

labels_2 = ("$\\alpha$", "$\\sigma$")
content_2 = (alpha_col_2, sigma_col_2)

utils.table_generator(
    n_columns=len(labels_2),
    labels=labels_2,
    content=content_2,
    output_file_name="normal_table_z.tex"
)

# VISUALIZATION: Normal distribution with alpha and sigma
fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))

# Create x values
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

# Plot the curve
ax.plot(x, y, 'k-', linewidth=2, label=r'$\mathcal{N}(z;0, 1)$')

# Example: alpha = 0.05, sigma = 1.645
alpha_example = 0.05
sigma_example = norm.ppf(1 - alpha_example)

# Fill the right tail (alpha region)
x_tail = x[x >= sigma_example]
y_tail = norm.pdf(x_tail)
ax.fill_between(x_tail, 0, y_tail, alpha=0.3, color='C0', label=f'$\\alpha = {alpha_example}$')

# Draw vertical line at sigma
ax.axvline(sigma_example, color='black', linestyle='--', linewidth=2, label=f'$z = {sigma_example:.3f}$')

# Add annotations
ax.annotate('$\\alpha$', xy=(sigma_example + 0.5, 0.05), color='black', weight='bold')

# Labels and formatting
ax.set_xlabel('$z$')
ax.set_ylabel('Probability density')
ax.set_title('Standard normal distribution visualization')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left')
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.45)

plt.savefig('images/normal_table_visualization.pgf', format='pgf')
plt.close()
