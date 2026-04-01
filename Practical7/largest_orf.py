#largest_orf.py
#identify the longest potential open reading in within gene sequences 

#define the sequence, start and stop codons
seq = "AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG"
start_codon = "AUG"
stop_codons = ["UAA", "UAG", "UGA"]

#create variables
longest_orf = ""
longest_length = 0

for i in range(len(seq)):
    #check if current position is a start codon
    if seq[i:i+3] == start_codon:
        #search for stop codons in this position
        for j in range(i+3,len(seq)-2,3):
            if seq[j:j+3] in stop_codons:
                #find a complete orf
                orf = seq[i:j+3]
                if len(orf) > longest_length:
                    longest_orf = orf
                    longest_length = len(orf)
                break

#output results
print("longest ORF sequence:", longest_orf)
print("longest ORF length:", longest_length)
