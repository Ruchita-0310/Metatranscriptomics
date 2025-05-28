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
    Processes all relevant files in the given directory to calculate TPM and
    merges the results into a single DataFrame.

    Args:
        directory (str): Path to the directory containing the input files.

    Returns:
         pandas.DataFrame: A DataFrame containing TPM values for all processed samples,
                          or None if no valid files were found.
    """
    all_results = []
    for filename in os.listdir(directory):
        if filename.startswith("sealrpkm_") and filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            result_df = calculate_tpm(filepath)
            if result_df is not None:  # Only process valid files
                sample_name = os.path.splitext(filename)[0]
                result_df = result_df.rename(columns={'TPM': sample_name})
                all_results.append(result_df)

    if not all_results:
        print("No valid 'sealrpkm_*.txt' files found to process.")
        return None

    # Merge all DataFrames on '#Name'
    tpm_all = all_results[0]
    for df in all_results[1:]:
        tpm_all = pd.merge(tpm_all, df, on='#Name', how='outer')
    tpm_all = tpm_all.fillna(0)  # Fill NaN values with 0
    return tpm_all

def save_results(df, output_path):
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
    work_dir = os.path.dirname(os.path.abspath(__file__))  
    tpm_all_df = process_files(work_dir)
    if tpm_all_df is not None:
        tpm_all_path = os.path.join(work_dir, "tpm_all.xlsx")
        save_results(tpm_all_df, tpm_all_path)
    print("Done.")
