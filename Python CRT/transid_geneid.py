#!/usr/bin/env python3

import requests
import csv

# Input and output files
input_file = r"C:/Users/hrjyo/\Downloads/SET_1.txt"   # Your input file
output_file = r"C:/Users/hrjyo/Downloads/SET_1_converted.csv"  # Output CSV

# Ensembl REST API URL
server = "https://rest.ensembl.org"
endpoint = "/lookup/id/"

# Read transcript IDs from input file
with open(input_file, "r") as f:
    transcript_ids = [line.strip() for line in f if line.strip()]

# Open output CSV
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Transcript_ID", "Gene_ID", "Gene_Symbol"])
    
    for tid in transcript_ids:
        url = f"{server}{endpoint}{tid}?expand=1"
        response = requests.get(url, headers={"Content-Type": "application/json"})
        if response.ok:
            data = response.json()
            gene_id = data.get("Parent", "NA")
            gene_symbol = data.get("display_name", "NA")
            writer.writerow([tid, gene_id, gene_symbol])
        else:
            writer.writerow([tid, "NA", "NA"])

print(f"Conversion completed. Output saved to: {output_file}")
