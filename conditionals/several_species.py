# Several Species
# Matthew Imiolek
# CMPU-353 Bioinformatics

# Open the CSV
csv = open("data.csv")

# Break apart the fields of the CSV, and get the genes for the requested species
for genes in csv:
    fields = genes.split(",")
    species = fields[0]
    sequence = fields[1]
    gene = fields[2]
    expression = fields[3]
    if species == "Drosophila melanogaster" or species == "Drosophila simulans":
        print(gene)