import os
import pandas as pd

def calculate_tpm(filepath):
    """
    Calculates Transcripts Per Million (TPM) from a file containing gene expression data.

    Args:
        filepath (str): Path to the input file.

    Returns:
        pandas.DataFrame: A DataFrame with gene names and their corresponding TPM values,
                          or None if the file doesn't contain the required columns.
    """
    try:
        df = pd.read_csv(filepath, sep='\t', skiprows=4)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None

    required_columns = ['#Name', 'Length', 'Reads']
    if not all(col in df.columns for col in required_columns):
        print(f"Error: File {filepath} is missing required columns: {required_columns}")
        return None

    # Calculate Reads Per Kilobase (RPK)
    df['RPK'] = (df['Reads'] / df['Length']) * 1000

    # Calculate scaling factor for TPM normalization
    per_million_scaling_factor = df['RPK'].sum() / 1e6

    # Calculate Transcripts Per Million (TPM)
    df['TPM'] = df['RPK'] / per_million_scaling_factor

    # Extract the required columns
    result_df = df[['#Name', 'TPM']].copy()
    return result_df

def process_files(directory):
  """
    Saves the given DataFrame to an Excel file.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        output_path (str): Path to the output Excel file.
    """
    try:
        df.to_excel(output_path, index=False)
        print(f"TPM results saved to {output_path}")
    except Exception as e:
        print(f"Error saving to Excel: {e}")

if __name__ == "__main__":
    work_dir = os.path.dirname(os.path.abspath(__file__))  # Use current directory
    # If you want to use a specific directory, uncomment and modify the line below.
    # work_dir = r"D:\OneDrive - University of Calgary\Exp_Sediment\Experiments\Molecular_biology\2025_Apr\seal"

    tpm_all_df = process_files(work_dir)
    if tpm_all_df is not None:
        tpm_all_path = os.path.join(work_dir, "tpm_all.xlsx")
        save_results(tpm_all_df, tpm_all_path)
    print("Done.")
  
