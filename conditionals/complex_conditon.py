# Complex Condition
# Matthew Imiolek
# CMPU-353 Bioinformatics

# Open the CSV
csv = open("data.csv")

# Break apart the fields of the CSV
for genes in csv:
    fields = genes.split(",")
    species = fields[0]
    sequence = fields[1]
    gene = fields[2]
    expression = fields[3]
    
    # Print the gene names that match this complex condition
    if (gene.startswith("k") or gene.startswith("h")) and species != "Drosophila melanogaster":
        print(gene)