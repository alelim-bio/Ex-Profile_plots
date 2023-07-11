import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# Read DESeq2 table output into a DataFrame
deseq2_table = pd.read_csv('Results_DESeq2.csv')

deseq2_table = deseq2_table.dropna()
# deseq2_table = deseq2_table[deseq2_table[]

# Adjust p-values for multiple testing (e.g., using the Benjamini-Hochberg procedure)
deseq2_table['adjusted_pvalue'] = -1 * np.log10(deseq2_table['pvalue'])
deseq2_table['log2_fold_change'] = deseq2_table['log2FoldChange']

# Set thresholds for significance
significance_threshold = 0.05
fold_change_thresholds = [2, 20]  # Add additional fold change thresholds here

# Assign colors based on fold change thresholds
colors = np.full(len(deseq2_table), 'gray')  # Initialize with a default color for all points

for threshold in fold_change_thresholds:
    color = 'red' if threshold == 2 else 'blue'  # Change color based on the threshold value
    colors[deseq2_table['log2_fold_change'].abs() > threshold] = color

# Create the volcano plot
plt.figure(figsize=(10, 6))
plt.scatter(deseq2_table['log2_fold_change'], deseq2_table['adjusted_pvalue'], color=colors, alpha=0.5)
plt.axhline(-np.log10(significance_threshold), color='r', linestyle='--', label='Significance Threshold')
plt.axvline(fold_change_thresholds[0], color='g', linestyle='--', label='Fold Change Threshold')
plt.axvline(-fold_change_thresholds[0], color='g', linestyle='--')
plt.axvline(fold_change_thresholds[1], color='b', linestyle='--', label='Fold Change Threshold')
plt.axvline(-fold_change_thresholds[1], color='b', linestyle='--')
plt.xlabel('Log2 Fold Change')
plt.ylabel('-log10(Adjusted p-value)')
plt.title('Volcano Plot')
plt.legend()
plt.tight_layout()


# Save the figure as a PDF file
# plt.savefig('volcano_plot.pdf', format='pdf')
# Save the figure as a PNG file
plt.savefig('volcano_plot.png', format='png')
