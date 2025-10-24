import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided image
data = {
    'Category': ['Co-factors & Precursors', 'Modifying enzymes', 'NRPS/PKS', 'Regulatory & Transport Genes', 'RiPPs and peptides', 'Siderophore',	'Terpenoids'],
    'DL': ['0.00675%', '0.00422%', '0.00314%', '0.00342%', '0.00286%', '0.01008%', '0.00065%'],
    'PL': ['0.00003%', '0.00005%', '0.00000%', '0.00006%', '0.00002%', '0.00011%', '0.00001%'],
    'GE': ['0.07034%', '0.10569%', '0.01732%', '0.20831%', '0.07062%', '0.14097%', '0.07685%']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set 'Category' as the index for easier plotting
df = df.set_index('Category')

# Clean the data: remove '%' and convert to float
for col in df.columns:
    df[col] = df[col].str.rstrip('%').astype(float)

# Create the heatmap
# Adjusted the figure size to make the cells thinner by making the plot much wider relative to its height
fig, ax = plt.subplots(figsize=(12, 4))
# Changed the colormap to 'RdBu_r' for high values (dark red) and low values (dark blue)
im = ax.imshow(df.values, cmap='RdBu_r')

# Set labels for the axes
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Rotate the tick labels and set their alignment.
# Changed rotation from 45 to 0 for a straight orientation
plt.setp(ax.get_xticklabels(), rotation=0)

# Add x and y axis labels as requested
ax.set_xlabel('Consortia' , fontsize=14, fontweight='bold')
ax.set_ylabel('Genes Expressed (TPM)', fontsize=14, fontweight='bold')

# Removed the loop that added the numbers to the heatmap cells

# Add a title and colorbar
ax.set_title(" ")
cbar = ax.figure.colorbar(im, ax=ax)
# Updated colorbar label to include '%'
cbar.ax.set_ylabel("Value (%)", rotation=-90, va="bottom")

# Adjust the plot to ensure everything fits
# fig.tight_layout() # Commented out to use plt.subplots_adjust() instead
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Save the plot
# You can change the file path to where you want to save the plot
plot_save_location = "/Users/ruchitasolanki/Downloads/Cyano_paper/RNA_data_analysis/SM_03_result.png"
# plot_save_location = None # Set to None if you only want to display the plot

if plot_save_location:
    # Added dpi=300 to increase the resolution of the saved image
    #plt.savefig(plot_save_location, bbox_inches='tight', dpi=2000)
    print(f"Plot saved to {plot_save_location}")

# Show the plot
plt.show()
