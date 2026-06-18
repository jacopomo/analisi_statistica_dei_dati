'''
Script that generates two LaTeX tables of chi-squared values for various degrees of freedom and p-values.
The first table (chi2_table_high.tex) contains chi-squared values for upper-tail probabilities above 0.5
The second table (chi2_table_low.tex) contains chi-squared values for upper-tail probabilities below 0.5
Then, it generates two visualizations of the chi-squared distribution with shaded areas corresponding to specific upper-tail probabilities (0.75 and 0.25).
'''
from scipy.stats import chi2
import numpy as np
from asd import utils
import matplotlib.pyplot as plt

# Degrees of freedom (table columns)
dof_values = list(range(1, 26))

# Chi2-values for upper-tail probabilities (table rows)
chi2_values_high = [0.999, 0.995, 0.99, 0.95, 0.90, 0.75, 0.50]
chi2_values_low = [0.50, 0.25, 0.10, 0.05, 0.01, 0.005, 0.001]

# Generate table columns
# First column: degrees of freedom
dof_col = [f"${nu}$" for nu in dof_values]

# Other columns: chi-squared quantiles for each p-value
chi2_columns_h, chi2_columns_l = [], []
for h,l in zip(chi2_values_high, chi2_values_low):
    col_data_h, col_data_l = [], [] 
    for nu in dof_values:
        # chi2.ppf is the quantile function (inverse CDF)
        # We want the value such that P(X > value) = v, which is equivalent to 1 - P(X <= value)
        high, low = chi2.ppf(1-h, nu), chi2.ppf(1-l, nu)
        # Format
        high, low = utils.number_formatter(high, 3), utils.number_formatter(low, 3)
        col_data_h.append(high), col_data_l.append(low)
    chi2_columns_h.append(col_data_h), chi2_columns_l.append(col_data_l)

# Prepare table labels
labels_h = (r"\diagbox{$\nu$}{$p$}",) + tuple(f"${v}$" for v in chi2_values_high)
labels_l = (r"\diagbox{$\nu$}{$p$}",) + tuple(f"${v}$" for v in chi2_values_low)

# Prepare content: tuple of all columns (dof first, then chi2 values for each p-value)
content_h = tuple([dof_col] + chi2_columns_h)
content_l = tuple([dof_col] + chi2_columns_l)

# Generate the tables
utils.table_generator(
    n_columns=len(labels_h), 
    labels=labels_h, 
    content=content_h, 
    output_file_name="chi2_table_high.tex"
)

utils.table_generator(
    n_columns=len(labels_l), 
    labels=labels_l, 
    content=content_l, 
    output_file_name="chi2_table_low.tex"
)


# VISUALIZATION: Chi2 distribution, low and high
# Example: upper tail integral = 0.75 and 0.25 find the corresponding chi2 value and shade the area under the curve
integral_example = [0.75, 0.25]
for i in integral_example:
    chi2_example = chi2.ppf(1 - i, 3)  # Example with 3 degrees of freedom
    fig, ax = utils.pgf_generator(figsize=(3.4, 2.2))

    # Create x values
    x = np.linspace(0, 5, 1000)
    nu=3  # Example degrees of freedom
    y = chi2.pdf(x,nu)

    # Plot the curve
    ax.plot(x, y, '-', linewidth=2, label=r'$\chi^2$ distribution', color="black")

    chi2_example = chi2.ppf(1 - i, nu)

    # Fill the upper tail
    chi_tail = x[x >= chi2_example]
    y_tail = chi2.pdf(chi_tail,nu)
    ax.fill_between(chi_tail, 0, y_tail, alpha=0.3, color='C0', label=f'$Area = {i}$')

    # Draw vertical line at chi2
    ax.axvline(chi2_example, color='black', linestyle='--', linewidth=2)

    # Labels and formatting
    ax.legend(loc='upper right')
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 0.3)

    # Remove ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Save
    if i > 0.5:
        plt.savefig('images/chi2_table_visualization_high.pgf', format='pgf')
    else:
        plt.savefig('images/chi2_table_visualization_low.pgf', format='pgf')
    plt.close()