#stop_codons.py
#extract genes that contain in-frame stop codons
#header line shows ONLY the stop codon that gives the longest ORF

import re

input_file = "Saccharomyces_cerevisiae.R64-1-1.cDNA.all.fa"
output_file = "stop_genes.fa"

stop_codons = ['TAA', 'TAG', 'TGA']

#read all genes
genes = {}

with open(input_file, 'r') as f:
    name = None
    seq = []
    
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('>'):
            if name and seq:
                genes[name] = ''.join(seq)
            
            header = line[1:]
            name = header.split()[0]
            if 'gene:' in header:
                m = re.search(r'gene:(\S+)', header)
                if m:
                    name = m.group(1)
            seq = []
        else:
            clean = re.sub(r'[^ATCGatcg]', '', line).upper()
            if clean:
                seq.append(clean)
    
    if name and seq:
        genes[name] = ''.join(seq)

print(f"Total genes: {len(genes)}")

#find genes with in-frame stop codons
result = {}

for gene_name, seq in genes.items():
    #find all ATG positions
    atgs = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            atgs.append(i)
    
    if not atgs:
        continue
    
    #for each stop codon, find all in-frame occurrences and calculate ORF length
    best_stop = None
    best_length = 0
    best_atg = None
    
    for stop in stop_codons:
        #find all positions of this stop codon
        for i in range(len(seq) - 2):
            if seq[i:i+3] == stop:
                #check if in-frame with any ATG
                for atg in atgs:
                    if i > atg and (i - atg) % 3 == 0:
                        orf_length = i - atg + 3
                        if orf_length > best_length:
                            best_length = orf_length
                            best_stop = stop
                        break
    
    #save gene with only the best stop codon
    if best_stop:
        name_new = f"{gene_name}_{best_stop}"
        result[name_new] = seq

print(f"Genes with in-frame stop codons: {len(result)}")

#write output
with open(output_file, 'w') as f:
    for name, seq in result.items():
        f.write(f">{name}\n")
        for i in range(0, len(seq), 60):
            f.write(seq[i:i+60] + "\n")

print(f"Saved to {output_file}")