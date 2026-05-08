'''
Script that generates the tables for a chi squared integral
'''
from scipy.stats import chi2
from asd import utils


def format(value):
    """Format a number with 3 significant figures.
    
    For values < 0.1, use scientific notation.
    For values >= 0.1, use fixed decimal notation.
    """
    if value == 0:
        return "0"
    
    if abs(value) < 0.1:
        # Use scientific notation with 1 sig fig
        formatted = f"{value:.0e}"
        # Clean up exponent notation: e-0X -> e-X, e+0X -> e+X
        formatted = formatted.replace("e-0", "e-").replace("e+0", "e+")
        return formatted
    else:
        # Use general format with 3 sig figs
        return f"{value:.3g}"


# Degrees of freedom
dof_values = list(range(1, 31))

# P-values for column headers
p_values = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]

# Generate table columns
# First column: degrees of freedom
dof_col = [f"${nu}$" for nu in dof_values]

# Other columns: chi-squared quantiles for each p-value
chi2_columns = []
for p in p_values:
    col_data = []
    for nu in dof_values:
        # chi2.ppf is the quantile function (inverse CDF)
        value = chi2.ppf(p, nu)
        # Format
        formatted = format(value)
        col_data.append(formatted)
    chi2_columns.append(col_data)

# Prepare table labels
labels = ("$\\nu/p$",) + tuple(f"${p}$" for p in p_values)

# Prepare content: tuple of all columns (dof first, then chi2 values for each p-value)
content = tuple([dof_col] + chi2_columns)

# Generate the table
utils.table_generator(
    n_columns=len(labels), 
    labels=labels, 
    content=content, 
    output_file_name="chi2_table.tex"
)