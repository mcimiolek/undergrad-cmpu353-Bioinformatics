# Length Range
# Matthew Imiolek
# CMPU-353 Bioinformatics

# Open the CSV
csv = open("data.csv")

# Break apart the fields of the CSV
for genes in csv:
    fields = genes.rstrip("\n").split(",")
    species = fields[0]
    sequence = fields[1]
    gene = fields[2]
    expression = fields[3]
    
    # Get the length of each sequence
    length = len(sequence)
    
    # If the length of a sequence if > 90 and < 110 print the name
    if length > 90 and length < 110:
    	print(gene)