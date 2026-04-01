#count_codons.py
#analyze codon usage in genes containing a user-specified stop codon
#generate a pie chart of in-frame codon distribution

import matplotlib.pyplot as plt
from collections import defaultdict

#get user input for stop codon
print("Please choose a stop codon: TAA, TAG, TGA")
user_stop = input("Enter your choice: ").strip().upper()

#validate input
while user_stop not in ['TAA', 'TAG', 'TGA']:
    print("Invalid input. Please enter TAA, TAG, or TGA")
    user_stop = input("Enter your choice: ").strip().upper()

#read the stop_genes.fa file
input_file = "stop_genes.fa"

#extract sequences that contain the user-specified stop codon
genes_with_stop = []

with open(input_file, 'r') as f:
    current_seq = []
    reading_seq = False
    current_gene = None
    
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            #save previous sequence if it contains the target stop codon
            if reading_seq and current_gene and user_stop in current_gene:
                genes_with_stop.append(''.join(current_seq))
            #start new gene
            current_gene = line[1:]  #remove '>'
            current_seq = []
            reading_seq = True
        elif reading_seq:
            current_seq.append(line)
    
    #save the last gene
    if reading_seq and current_gene and user_stop in current_gene:
        genes_with_stop.append(''.join(current_seq))

print(f"Found {len(genes_with_stop)} genes containing {user_stop}")

#define all possible codons (excluding stop codons)
codons = [a+b+c for a in 'ATGC' for b in 'ATGC' for c in 'ATGC']
stop_codons = ['TAA', 'TAG', 'TGA']
codons = [c for c in codons if c not in stop_codons]

#count in-frame codons
codon_counts = defaultdict(int)

for sequence in genes_with_stop:
    #find all positions of the user-specified stop codon
    stop_positions = []
    pos = 0
    while pos < len(sequence):
        found = sequence.find(user_stop, pos)
        if found == -1:
            break
        stop_positions.append(found)
        pos = found + 1
    
    if not stop_positions:
        continue
    
    #for each stop codon position, find the start codon in frame
    for stop_pos in stop_positions:
        #search backward every 3 bases for a start codon (ATG)
        orf_start = None
        for start_pos in range(stop_pos - 3, -1, -3):
            if start_pos >= 0 and sequence[start_pos:start_pos+3] == 'ATG':
                orf_start = start_pos
                break
        
        if orf_start is not None:
            #count codons within the ORF (excluding the stop codon)
            orf_seq = sequence[orf_start:stop_pos]  #stop codon not included
            for i in range(0, len(orf_seq), 3):
                if i + 3 <= len(orf_seq):
                    codon = orf_seq[i:i+3]
                    if codon in codons:
                        codon_counts[codon] += 1

#generate pie chart - show all 64 codons
if codon_counts:
    #get all 64 possible codons
    all_codons = [a+b+c for a in 'ATGC' for b in 'ATGC' for c in 'ATGC']
    
    #create lists for all codons
    labels = []
    sizes = []
    
    #add each codon with its count (0 if not found)
    for codon in all_codons:
        count = codon_counts.get(codon, 0)
        labels.append(codon)
        sizes.append(count)
    
    #create pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'In-frame Codon Usage in Genes Containing {user_stop} Stop Codon')
    plt.axis('equal')  #make pie chart circular
    
    #save to file
    output_plot = f'codon_usage_{user_stop}.png'
    plt.savefig(output_plot, dpi=300, bbox_inches='tight')
    print(f"Pie chart saved as: {output_plot}")
    
    #uncomment below to also display the chart
    #plt.show()
else:
    print(f"No genes found containing {user_stop}. Cannot generate pie chart.")
