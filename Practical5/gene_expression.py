# Gene expression analysis
import matplotlib.pyplot as plt

# create initial dictionary with 5 genes
gene_expression = {
    "TP53" : 12.4,
    "EGFR" : 15.1,
    "BRCA1" : 8.2,
    "PTEN" : 5.3,
    "ESR1" : 10.7,
}

#print initial dictionary
print("Initial gene expression dictionary:",gene_expression)

#add MYC gene
gene_expression["MYC"]=11.6

#create a variable representing a gene of interest
#pseudocode:
#1. users select a gene of interest by changing the variable below
#2. check if the gene exists in the dictionary
#3. if gene exists: print its expression value
#4. if gene do not exist: print erroe message
gene_of_interest = "EGFR" # the user can modify this to test differrent genes like "TP53","MYC",etc.
print("gene of interest:",{gene_of_interest})
if gene_of_interest in gene_expression:
    print("expression value:",{gene_expression[gene_of_interest]})
else:
    print("ERROR: gene",{gene_of_interest},"not found in the dataset")

#calculate and print average expression
average_expression = sum(gene_expression.values())/len(gene_expression)
print("average gene expression level:",average_expression)

#create bar chart
genes = list(gene_expression.keys())
values = list(gene_expression.values())

plt.figure(figsize=(10, 4))
plt.bar(genes, values, color='steelblue')
plt.title('Gene Expression Levels', fontsize=16)
plt.xlabel('Genes', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.ylim(0, max(values) + 2)  # Add some space on top

# Add value labels on top of bars
for i, v in enumerate(values):
    plt.text(i, v + 0.2, str(v), ha='center', fontsize=10)

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

