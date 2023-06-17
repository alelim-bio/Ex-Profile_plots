"""
AtoI Mutation Analysis Script
Date: June 16, 2023

Description:
    This script reads a FASTA file containing transcript sequences, a CSV file containing CDS positions,
    and a TXT file containing inosine positions. It identifies mutations caused by inosine (I) to guanosine (G) conversion,
    extracts the coding sequences, translates them into protein sequences, and analyzes the mutations for synonymous and
    non-synonymous changes.

"""
import csv
import pandas as pd

def read_fasta_file(filename):
    sequences = {}
    current_sequence = ''
    current_id = ''
    with open(filename) as file:
        for line in file:
            if line.startswith('>'):
                if current_id != '':
                    sequences[current_id] = current_sequence
                    current_sequence = ''
                current_id = line.strip()[1:]
            else:
                current_sequence += line.strip()
        if current_id != '':
            sequences[current_id] = current_sequence
    return sequences

def read_cds_positions(filename):
    cds_positions = {}
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader, None)  # Read and ignore the header if present
        for line in reader:
            transcript_id, start, end = line
            cds_positions[transcript_id] = (int(start), int(end))
    return cds_positions

def read_inosine_positions(filename):
    inosine_positions = {}
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader, None)  # Read and ignore the header if present
        for line in reader:
            transcript_id, position = line
            position = int(position)
            if transcript_id not in inosine_positions:
                inosine_positions[transcript_id] = []
            inosine_positions[transcript_id].append(position)
    return inosine_positions

def extract_coding_sequence(transcript_sequence, cds_start, cds_end):
    coding_sequence = transcript_sequence[cds_start - 1:cds_end]
    return coding_sequence[:len(coding_sequence) // 3 * 3]  # Remove incomplete codons

def translate_sequence(nucleotide_sequence):
    codon_table = {
        'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAT': 'N',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGT': 'S',
        'ATA': 'I', 'ATC': 'I', 'ATG': 'M', 'ATT': 'I',
        'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAT': 'H',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAT': 'D',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'TAA': '*', 'TAC': 'Y', 'TAG': '*', 'TAT': 'Y',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TGA': '*', 'TGC': 'C', 'TGG': 'W', 'TGT': 'C',
        'TTA': 'L', 'TTC': 'F', 'TTG': 'L', 'TTT': 'F'
    }
    protein_sequence = ''
    for i in range(0, len(nucleotide_sequence), 3):
        codon = nucleotide_sequence[i:i + 3]
        amino_acid = codon_table.get(codon, 'X')
        protein_sequence += amino_acid
    return protein_sequence

def classify_mutation(original_codon, mutated_codon):
    if original_codon == mutated_codon:
        return "No Mutation"
    else:
        return "Synonymous" if translate_sequence(original_codon) == translate_sequence(mutated_codon) else "Non-Synonymous"

# Read the input files
sequences = read_fasta_file('output.fasta')
cds_positions = read_cds_positions('coordinates_cds.csv')
inosine_positions = read_inosine_positions('AtoI_positions.txt')

# Create the table data list
table_data = []

# Process each transcript sequence
for seq_id, transcript_sequence in sequences.items():
    if seq_id not in cds_positions:
        continue
    if seq_id not in inosine_positions:
        continue

    # Extract the coding sequence
    cds_start, cds_end = cds_positions[seq_id]
    coding_sequence = extract_coding_sequence(transcript_sequence, cds_start, cds_end)

    # Create a copy of the transcript sequence to mutate
    mutated_sequence = list(transcript_sequence)

    # Get the positions to mutate
    positions_to_mutate = inosine_positions[seq_id]

    for transcript_position in positions_to_mutate:
        # Mutate the corresponding position in the transcript sequence
        mutated_sequence[transcript_position - 1] = 'G'

    # Convert the mutated sequence back to a string
    mutated_sequence = ''.join(mutated_sequence)

    # Extract the coding sequence from the mutated transcript sequence
    mutated_coding_sequence = extract_coding_sequence(mutated_sequence, cds_start, cds_end)

    # Translate the sequences
    original_protein_sequence = translate_sequence(coding_sequence)
    mutated_protein_sequence = translate_sequence(mutated_coding_sequence)

    for i in range(len(coding_sequence) // 3):
        original_codon = coding_sequence[i * 3: (i + 1) * 3]
        mutated_codon = mutated_coding_sequence[i * 3: (i + 1) * 3]
        mutation_classification = classify_mutation(original_codon, mutated_codon)

        # Check if the codon has mutated
        if mutation_classification != "No Mutation":
            transcript_position = cds_start + i * 3 + 1
            codon_position = (transcript_position - cds_start) // 3
            coding_position = (transcript_position - cds_start) + 1

            # Add the row to the table data
            table_data.append([
                seq_id,
                original_protein_sequence,
                mutated_protein_sequence,
                transcript_position,
                coding_position,
                original_codon,
                mutated_codon,
                original_protein_sequence[codon_position],
                mutated_protein_sequence[codon_position],
                "S" if mutation_classification == "Synonymous" else "N"
            ])

# Create a DataFrame from the table data
columns = [
    "Transcript ID",
    "Original Protein Sequence",
    "Mutated Protein Sequence",
    "Position in Transcript",
    "Position in Coding Sequence",
    "Original Codon",
    "Mutated Codon",
    "Original Amino Acid",
    "Mutated Amino Acid",
    "Mutation Type"
]
df = pd.DataFrame(table_data, columns=columns)

# Print the DataFrame
print(df.iloc[0]["Original Protein Sequence"])
df.to_csv("mutation_table.csv", index=False)
