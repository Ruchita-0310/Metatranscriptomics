import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_bubble_plot_from_excel_sheet(excel_file_path, sheet_name, category_col, value_cols,
                                  title="Bubble Plot", x_label="X-axis", y_label="Y-axis",
                                  save_path=None):
    """
    Generates a bubble plot from data in a specific sheet of an Excel file,
    with categorical X and Y axes, and a custom size legend, matching the provided image style.

    Args:
        excel_file_path (str): The path to your Excel file (e.g., 'data.xlsx').
        sheet_name (str): The name of the sheet containing the data (e.g., 'plot').
        category_col (str): The name of the column to use for the Y-axis categories (e.g., 'Category').
        value_cols (list): A list of column names to use for X-axis categories and bubble values (e.g., ['PL', 'DL', 'GE']).
        title (str, optional): The title of the plot. Defaults to "Bubble Plot".
        x_label (str, optional): The label for the X-axis. Defaults to "X-axis".
        y_label (str, optional): The label for the Y-axis. Defaults to "Y-axis".
        save_path (str, optional): If provided, the path (including filename and extension, e.g., 'my_bubble_plot.png')
                                   where the plot will be saved. If None, the plot will only be displayed.
    """
    try:
        # 1. Read the Excel file into a pandas DataFrame, specifying the sheet name
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        print(f"Successfully loaded data from '{excel_file_path}' - Sheet: '{sheet_name}'")
        print("Columns available:", df.columns.tolist())

        # Check if required columns exist
        required_cols = [category_col] + value_cols
        if not all(col in df.columns for col in required_cols):
            missing_cols = [col for col in required_cols if col not in df.columns]
            raise ValueError(f"Missing required columns in Excel sheet: {missing_cols}")

        # Melt the DataFrame to long format for easier plotting
        melted_df = df.melt(id_vars=[category_col], value_vars=value_cols,
                            var_name='Consortia', value_name='Value')

        # Drop rows where 'Value' is NaN, as these won't be plotted
        melted_df.dropna(subset=['Value'], inplace=True)

        # --- Dynamically determine Y-axis categories and their order ---
        # y_data_order = sorted(melted_df[category_col].unique().tolist())
        y_data_order = melted_df[category_col].unique().tolist()
        y_display_names = y_data_order
        y_display_map = dict(zip(y_data_order, y_display_names))

        melted_df[category_col] = pd.Categorical(melted_df[category_col], categories=y_data_order, ordered=True)
        melted_df.sort_values(by=category_col, inplace=True)

        # Define the order for X-axis categories
        x_order = ['DL', 'PL', 'GE']
        melted_df['Consortia'] = pd.Categorical(melted_df['Consortia'], categories=x_order, ordered=True)

        # Map categorical values to numerical positions for plotting
        melted_df['x_pos'] = melted_df['Consortia'].cat.codes
        melted_df['y_pos'] = melted_df[category_col].cat.codes

        unique_x_categories = melted_df['Consortia'].cat.categories
        unique_y_categories_display = [y_display_map[cat] for cat in melted_df[category_col].cat.categories]
        print(f"Number of unique Y-axis categories: {len(unique_y_categories_display)}")

        # --- Bubble Size Scaling for Plot Bubbles ---
        min_data_value = melted_df['Value'].min()
        max_data_value = melted_df['Value'].max()

        min_visual_size_plot = 10
        max_visual_size_plot = 4000

        if min_data_value == max_data_value:
            melted_df['scaled_size'] = (min_visual_size_plot + max_visual_size_plot) / 2
            print("Warning: All data values for plot bubble size are identical. Using a uniform size.")
        else:
            melted_df['scaled_size'] = np.interp(melted_df['Value'],
                                                 (min_data_value, max_data_value),
                                                 (min_visual_size_plot, max_visual_size_plot))

        # --- Plotting ---
        fig_height = max(6, len(unique_y_categories_display) * 0.6 + 2)
        fig, ax = plt.subplots(figsize=(8, fig_height))

        num_categories_y = len(unique_y_categories_display)
        colors = plt.colormaps['Dark2']

        # NEW: Introduce a spacing factor for the x-axis
        x_spacing_factor = 0.02  # Adjust this value to change the spacing. A smaller value decreases the space.

        for i, row in melted_df.iterrows():
            y_cat_index = row['y_pos']
            # Apply the spacing factor to the x-position
            x_cat_index = row['x_pos'] * x_spacing_factor
            bubble_size = row['scaled_size']
            category_color = colors(y_cat_index % colors.N)

            ax.scatter(x_cat_index, y_cat_index,
                        s=bubble_size,
                        color=category_color,
                        alpha=0.8,
                        edgecolors='black',
                        linewidth=1.0)

        # --- Set X and Y axis ticks and labels ---
        # Apply the spacing factor to the tick locations as well
        ax.set_xticks(np.arange(len(unique_x_categories)) * x_spacing_factor)
        ax.set_xticklabels(unique_x_categories, fontsize=12)
        ax.set_yticks(range(len(unique_y_categories_display)))
        ax.set_yticklabels(unique_y_categories_display, fontsize=12)

        ax.set_xlabel(x_label, fontsize=14, fontweight='bold')
        ax.set_ylabel(y_label, fontsize=14, fontweight='bold')
        ax.set_title(title, fontsize=16)

        ax.grid(False)

        # --- Adjust X and Y axis limits to reduce spacing and prevent cutoff ---
        # Adjust the x-limit based on the spacing factor
        ax.set_xlim(-0.5 * x_spacing_factor, (len(unique_x_categories) - 0.5) * x_spacing_factor)
        # ax.set_xlim(-0.5, 0.75)
        ax.set_ylim(-0.5, len(unique_y_categories_display) - 0.5)

# --- Create Custom Size Legend ---
        legend_values_percent = [0.1, 1, 5, 15]
        legend_s_values_manual = [3.5, 350, 1800, 4000]

        legend_elements = []
        for i, val_percent in enumerate(legend_values_percent):
            s_val = legend_s_values_manual[i]
            marker_size_for_legend = np.sqrt(s_val) * 1

            label_text = f'{val_percent:.2f}' if val_percent < 1 else f'{int(val_percent)}'

            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w',
                                              label=label_text,
                                              markersize=marker_size_for_legend,
                                              markerfacecolor='white',
                                              markeredgecolor='black',
                                              markeredgewidth=1.5,
                                              alpha=0.8))

        legend1 = ax.legend(handles=legend_elements,
                            title='Value (%)',
                            loc='center left',
                            bbox_to_anchor=(1.05, 0.5),
                            frameon=False,
                            labelspacing=1,
                            handletextpad=3.0,
                            fontsize=15,
                            title_fontsize=12)

        ax.add_artist(legend1)

        fig.tight_layout(rect=[0, 0, 0.65, 1])

        # --- Save the plot if save_path is provided ---
        if save_path:
            try:
                # Force a redraw of the canvas before saving
                fig.canvas.draw()
                # Save the plot using the figure object
                fig.savefig(save_path, dpi=1000) #, bbox_inches='tight')
                print(f"Plot saved successfully to: {save_path}")
            except Exception as e:
                print(f"Error saving plot to {save_path}: {e}")

        plt.show() # Display the plot after saving (or if not saving)
        plt.close(fig) # Explicitly close the figure to free up memory

    except FileNotFoundError:
        print(f"Error: The Excel file '{excel_file_path}' was not found. Please check the path.")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Column not found: {e}. Please ensure the column names are correct and case-sensitive.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- How to use the function ---
if __name__ == "__main__":
    excel_file = "01_sodalinema_TPM_all.xlsx"
    sheet_to_use = "plot"
    category_column = 'Category'
    value_columns_for_call = ['DL', 'PL', 'GE']

    plot_save_location = "final_results.png"
    # plot_save_location = None # Set to None if you only want to display the plot

    create_bubble_plot_from_excel_sheet(
        excel_file_path=excel_file,
        sheet_name=sheet_to_use,
        category_col=category_column,
        value_cols=value_columns_for_call,
        title='',
        x_label='Consortia',
        y_label='Genes Expressed (TPM)',
        save_path=plot_save_location
    )
    
