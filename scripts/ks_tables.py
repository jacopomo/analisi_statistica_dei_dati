''' 
Script that generates a LaTeX table of Kolmogorov-Smirnov critical values for various sample sizes and significance levels. 
'''

import numpy as np
from scipy.stats import kstwo, kstwobign
from asd import utils

# significance levels (table columns)
alphas = [0.001, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20]

# sample sizes (table rows)
ns = [1,2,3,4,5,6,7,8,9,10,
      11,12,13,14,15,16,17,18,19,20,
      25,30,35,40,45,50]

# Generate table columns
# First column: sample size n
n_col = [f"${n}$" for n in ns]
n_col.append(r"$n\to\infty$")


# Other columns: Kolmogorov-Smirnov quantiles for each significance level
ks_columns = []
for alpha in alphas:
    col_data = []

    # For each sample size n, compute the critical value such that P(D_n > crit) = alpha
    for n in ns:
        crit = kstwo.ppf(1 - alpha, n)
        col_data.append(utils.number_formatter(crit, 3))
    
    # asymptotic value
    asymptotic = kstwobign.ppf(1 - alpha)
    col_data.append(rf"$\frac{{{utils.number_formatter(asymptotic,3)}}}{{\sqrt{{n}}}}$")

    ks_columns.append(col_data)

# Prepare table labels
labels = (r"\diagbox{$n$}{$\alpha$}",) + tuple(f"${alpha}$" for alpha in alphas)

# Prepare content: tuple of all columns (n first, then KS values for each alpha)
content = tuple([n_col] + ks_columns)

# Generate the table
utils.table_generator(
    n_columns=len(labels), 
    labels=labels, 
    content=content, 
    output_file_name="ks_table.tex"
)