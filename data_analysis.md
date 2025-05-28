# 1. Mapping
[Seal.sh - BBMap](https://archive.jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/seal-guide/)
```
#!/bin/bash

# Expand the .fa reference files into a comma-separated list
ref_files=$(ls /work/ebg_lab/gm/RS/metatranscriptomics/ref_seq/*.fa | tr '\n' ',')
ref_files=${ref_files%,}  # Remove trailing comma

# Loop through your samples
for sample in RS-PL4-1-RNA_S15 RS-PL4-2-RNA_S16 RS-PL4-3-RNA_S17
do
  # Loop through the read pairs (R1 and R2)
  for read in R1 R2
  do
    # Construct the input file names using wildcards for the lane
    file1="${sample}_L001_${read}_001.fastq.gz"
    file2="${sample}_L002_${read}_001.fastq.gz"
    # Construct the output file name
    merged_file="${sample}_${read}_merged.fastq.gz"

    # Check if the input files exist
    if [ -f "$file1" ] && [ -f "$file2" ]; then
      # Concatenate the files using cat
      cat "$file1" "$file2" > "$merged_file"
      echo "Merged $file1 and $file2 into $merged_file"
    else
      echo "Error: One or both of the input files ($file1, $file2) do not exist for sample $sample and read $read. Skipping."
      continue
    fi

    # Run seal.sh
    echo "Running seal.sh on $merged_file..."
    seal.sh \
      in="$merged_file" \
      ref="$ref_files" \
      stats="sealstats_${sample}_${read}.txt"  \
      rpkm="sealrpkm_${sample}_${read}.txt" \
      ambig=random
    echo "Done with seal.sh for $merged_file."
  done
  echo "Done with sample $sample."
done

echo "Finished concatenating files and running seal.sh."
```
Use annotated bins [sqlite_to_fasta.py](https://github.com/Ruchita-0310/Metatranscriptomics/blob/main/sqlite_to_fasta.py).        
To use sqlite_to_fasta.py you need to follow:
```
conda create -n test_env
conda activate test_env
pip install metaerg
python3 sqlite_to_fasta.py
```
Now that you have Reads Per Kilobase Million (RPKM), you need to convert that into Transcript Per Million (TPM). You could use [tpm_calculator.py](https://github.com/Ruchita-0310/Metatranscriptomics/blob/main/tpm_calculator.py).              
```
conda create new_env
conda activate new_env
conda install pandas
conda install openpyxl
python3 tpm_calculator.py
```
