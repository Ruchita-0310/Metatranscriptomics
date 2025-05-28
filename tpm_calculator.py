import os
import pandas as pd

def calculate_tpm(filepath):
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

    df['RPK'] = (df['Reads'] / df['Length']) * 1000
    per_million_scaling_factor = df['RPK'].sum() / 1e6
    df['TPM'] = df['RPK'] / per_million_scaling_factor
    result_df = df[['#Name', 'TPM']].copy()
    return result_df

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

def process_files(directory):
    """
    Processes all .tsv files in the directory and returns a combined TPM DataFrame.
    """
    combined_df = pd.DataFrame()
    for file in os.listdir(directory):
        if file.endswith(".tsv"):
            filepath = os.path.join(directory, file)
            tpm_df = calculate_tpm(filepath)
            if tpm_df is not None:
                tpm_df['Sample'] = os.path.splitext(file)[0]
                combined_df = pd.concat([combined_df, tpm_df], ignore_index=True)
    return combined_df

if __name__ == "__main__":
    work_dir = os.path.dirname(os.path.abspath(__file__))
    tpm_all_df = process_files(work_dir)
    if tpm_all_df is not None and not tpm_all_df.empty:
        tpm_all_path = os.path.join(work_dir, "tpm_all.xlsx")
        save_results(tpm_all_df, tpm_all_path)
    print("Done.")
