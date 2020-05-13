# AT Content
# Matthew Imiolek
# CMPU-353 Bioinformatics

# Function which will be used to get the AT content (a percent of the whole)
# Returns a number (float)
def at_content(seq):
    # the length of the sequence of DNA
    length = len(seq)

    # Get the counts
    a_count = seq.upper().count("A")
    t_count = seq.upper().count("T")

    # Compute the content
    content = (a_count + t_count) / length

    return content

# Open the CSV
csv = open("data.csv")

# Break apart the fields of the CSV
for genes in csv:
    fields = genes.split(",")
    species = fields[0]
    sequence = fields[1]
    gene = fields[2]
    expression = fields[3]

    # print the name of the gene if the requirements are met
    if at_content(sequence) < 0.5 and int(expression) > 200:
        print(gene)