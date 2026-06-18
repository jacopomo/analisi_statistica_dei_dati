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


# TABLE 1: alpha (significance level) → z (critical z-value)
alpha_values = [0.25, 0.1, 0.05, 0.025, 0.01, 0.001]

alpha_col = [f"${alpha}$" for alpha in alpha_values]
z_col = []

for alpha in alpha_values:
    # Find z-value such that P(Z > z) = alpha (right tail)
    z_value = norm.ppf(1 - alpha)
    formatted = format(z_value)
    z_col.append(formatted)

labels_1 = ("$\\alpha$", "$z$")
content_1 = (alpha_col, z_col)

utils.table_generator(
    n_columns=len(labels_1),
    labels=labels_1,
    content=content_1,
    output_file_name="normal_table_a.tex"
)

# TABLE 2: z (critical z-value) → alpha (right tail area)
z_values = [1, 2, 3, 4, 5, 6]

z_col_2 = [f"${z}\\sigma$" for z in z_values]
alpha_col_2 = []

for z in z_values:
    # Calculate right tail probability at z = sigma
    tail_area = 1 - norm.cdf(z)
    formatted = format(tail_area)
    alpha_col_2.append(formatted)

labels_2 = ("$\\alpha$", "$z$")
content_2 = (alpha_col_2, z_col_2)

utils.table_generator(
    n_columns=len(labels_2),
    labels=labels_2,
    content=content_2,
    output_file_name="normal_table_z.tex"
)

# VISUALIZATION: Normal distribution with alpha and z
fig, ax = utils.pgf_generator(figsize=(5.5, 3.5))

# Create x values
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

# Plot the curve
ax.plot(x, y, 'k-', linewidth=2, label=r'$\mathcal{N}(z;0, 1)$')

# Example: alpha = 0.025, z = 1.96
alpha_example = 0.025
z_example = norm.ppf(1 - alpha_example)

# Fill the right tail (alpha region)
x_tail = x[x >= z_example]
y_tail = norm.pdf(x_tail)
ax.fill_between(x_tail, 0, y_tail, alpha=0.3, color='C0', label=f'$\\alpha = {alpha_example}$')

# Draw vertical line at z
ax.axvline(z_example, color='black', linestyle='--', linewidth=2, label=f'$z = {z_example:.3f}$')

# Add annotations
ax.annotate('$\\alpha$', xy=(z_example + 0.5, 0.05), color='black', weight='bold')

# Labels and formatting
ax.set_xlabel('$z$')
ax.set_ylabel('Probability density')
ax.set_title('Standard normal distribution: $\\alpha$ and z')
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left')
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.45)

plt.savefig('images/normal_table_visualization.pgf', format='pgf')
plt.close()
