'''
Script that generates the tables for a normal distribution
'''
from scipy.stats import norm
import numpy as np
from asd import utils
import matplotlib.pyplot as plt


def format(value):
    """Format a number with 3 significant figures.
    
    For values < 0.1, use scientific notation.
    For values >= 0.1, use fixed decimal notation.
    """
    if value == 0:
        return "0"
    
    if abs(value) < 0.1:
        # Use scientific notation
        formatted = f"{value:.2e}"
        # Clean up exponent notation: e-0X -> e-X, e+0X -> e+X
        formatted = formatted.replace("e-0", "e-").replace("e+0", "e+")
        return formatted
    else:
        # Use general format with 3 sig figs
        return f"{value:.3g}"


# TABLE 1: alpha (significance level) → delta (critical z-value)
alpha_values = [0.25, 0.1, 0.05, 0.01, 0.001, 0.0001]

alpha_col = [f"${alpha}$" for alpha in alpha_values]
delta_col = []

for alpha in alpha_values:
    # Find z-value such that P(Z > z) = alpha (right tail)
    z_value = norm.ppf(1 - alpha)
    formatted = format(z_value)
    delta_col.append(formatted)

labels_1 = ("$\\alpha$", "$\\delta$")
content_1 = (alpha_col, delta_col)

utils.table_generator(
    n_columns=len(labels_1),
    labels=labels_1,
    content=content_1,
    output_file_name="normal_alpha_delta_table.tex"
)

# TABLE 2: delta (number of sigmas) → alpha (right tail area)
sigma_values = [1, 2, 3, 4, 5, 6]

delta_col_2 = [f"${sigma}\\sigma$" for sigma in sigma_values]
alpha_col_2 = []

for sigma in sigma_values:
    # Calculate right tail probability at z = sigma
    tail_area = 1 - norm.cdf(sigma)
    formatted = format(tail_area)
    alpha_col_2.append(formatted)

labels_2 = ("$\\alpha$", "$\\delta$")
content_2 = (alpha_col_2, delta_col_2)

utils.table_generator(
    n_columns=len(labels_2),
    labels=labels_2,
    content=content_2,
    output_file_name="normal_delta_sigma_table.tex"
)

# VISUALIZATION: Normal distribution with alpha and delta
fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))

# Create x values
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

# Plot the curve
ax.plot(x, y, 'k-', linewidth=2, label='Standard Normal Distribution')

# Example: alpha = 0.05, delta = 1.645
alpha_example = 0.05
delta_example = norm.ppf(1 - alpha_example)

# Fill the right tail (alpha region)
x_tail = x[x >= delta_example]
y_tail = norm.pdf(x_tail)
ax.fill_between(x_tail, 0, y_tail, alpha=0.3, color='red', label=f'$\\alpha = {alpha_example}$')

# Draw vertical line at delta
ax.axvline(delta_example, color='blue', linestyle='--', linewidth=2, label=f'$\\delta = {delta_example:.3f}$')

# Add annotations
ax.annotate('$\\alpha$', xy=(delta_example + 0.5, 0.05), color='red', weight='bold')
ax.annotate('$\\delta$', xy=(delta_example, -0.02), color='blue', weight='bold', ha='center')

# Labels and formatting
ax.set_xlabel('$z$')
ax.set_ylabel('Probability Density')
ax.set_title('Standard Normal Distribution: Alpha and Delta')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_xlim(-4, 4)
ax.set_ylim(-0.03, 0.45)

plt.savefig('images/normal_alpha_delta_visualization.pgf', format='pgf')
plt.close()

