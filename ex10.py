# analyze-insulin.py

import os
import re

# Read the source file containing the full insulin sequence
with open('ex10_preproinsulin-seq.txt', 'r') as file:
    full_sequence = file.read()

# Remove "ORIGIN," "1," "61," "//," spaces, and return carriages
sequence_cleaned = re.sub(r'[^a-z]', '', full_sequence.lower())

# Create separate files for different insulin segments
output_dir = 'ex10_insulin-sequences'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create separate files for insulin segments if they don't exist
lsinsulin_path = os.path.join(output_dir, 'ex10_lsinsulin-seq-clean.txt')
if not os.path.exists(lsinsulin_path):
    with open(lsinsulin_path, 'w') as file:
        # Amino acids 1-24
        ls_sequence = sequence_cleaned[:24]
        file.write(ls_sequence)

binsulin_path = os.path.join(output_dir, 'ex10_binsulin-seq-clean.txt')
if not os.path.exists(binsulin_path):
    with open(binsulin_path, 'w') as file:
        # Amino acids 25-54
        b_sequence = sequence_cleaned[24:54]
        file.write(b_sequence)

cinsulin_path = os.path.join(output_dir, 'ex10_cinsulin-seq-clean.txt')
if not os.path.exists(cinsulin_path):
    with open(cinsulin_path, 'w') as file:
        # Amino acids 55-89
        c_sequence = sequence_cleaned[54:89]
        file.write(c_sequence)

ainsulin_path = os.path.join(output_dir, 'ex10_ainsulin-seq-clean.txt')
if not os.path.exists(ainsulin_path):
    with open(ainsulin_path, 'w') as file:
        # Amino acids 90-110
        a_sequence = sequence_cleaned[89:110]
        file.write(a_sequence)

# Verify the lengths of the saved sequences
print(f"Length of {lsinsulin_path}: {len(ls_sequence)}")
print(f"Length of {binsulin_path}: {len(b_sequence)}")
print(f"Length of {cinsulin_path}: {len(c_sequence)}")
print(f"Length of {ainsulin_path}: {len(a_sequence)}")
