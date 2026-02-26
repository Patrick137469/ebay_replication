import pandas as pd
import numpy as np

# Load pivot tables saved by preprocess.py
treated_pivot = pd.read_csv('temp/treated_pivot.csv', index_col='dma')
untreated_pivot = pd.read_csv('temp/untreated_pivot.csv', index_col='dma')

# Compute DID estimate

# Mean differences
r1_bar = treated_pivot['log_revenue_diff'].mean()
r0_bar = untreated_pivot['log_revenue_diff'].mean()

gamma_hat = r1_bar - r0_bar

# Sample sizes
n1 = len(treated_pivot)
n0 = len(untreated_pivot)

# Variances (pandas var() uses sample variance)
var1 = treated_pivot['log_revenue_diff'].var()
var0 = untreated_pivot['log_revenue_diff'].var()

# Standard error
se = np.sqrt(var1/n1 + var0/n0)

# 95% confidence interval
ci_lower = gamma_hat - 1.96 * se
ci_upper = gamma_hat + 1.96 * se

print("DID Results (Log Scale)")
print("=======================")
print(f"Gamma hat: {gamma_hat:.4f}")
print(f"Std Error: {se:.4f}")
print(f"95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")

# LaTeX table
latex = r"""\begin{table}[h]
\centering
\caption{Difference-in-Differences Estimate of the Effect of Paid Search on Revenue}
\begin{tabular}{lc}
\hline
& Log Scale \\
\hline
Point Estimate ($\hat{\gamma}$) & $%.4f$ \\
Standard Error & $%.4f$ \\
95\%% CI & $[%.4f, \; %.4f]$ \\
\hline
\end{tabular}
\label{tab:did}
\end{table}""" % (gamma_hat, se, ci_lower, ci_upper)

with open('output/tables/did_table.tex', 'w') as f:
    f.write(latex)
