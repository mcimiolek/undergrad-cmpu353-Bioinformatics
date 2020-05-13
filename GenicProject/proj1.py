#-----------------------------------------------------------------
# BIOL/CMPU-377 
# Spring 2020
# Project 1
# DNA: Playing with Strings
# Author: Matthew Imiolek
#-----------------------------------------------------------------
#
# Summary: This Python program isolates the upstream and genic
#          regions of a sequence. A report is printed, a sample
#          of which is saved in file: genic-report.txt
#
#-----------------------------------------------------------------

print("\n+++++++++ Upstream and Genic Report ++++++++++++++++\n")

# upstream and start of a gene ... 
some_sequence = "cgccatataatgctcgtccgcgcccta"
 
print("Starting sequence is: " + some_sequence)

# convert all nucleotides to uppercase
some_sequence_upper = some_sequence.upper()
print("Converted to uppercase: " + some_sequence_upper)

# get the length of sequence
seq_length = len(some_sequence)
print("Length of starting sequence is: " + str(seq_length))
 
print("\n----------------------------------------------------\n")
 
# get the position of the start codon "ATG" and the next two codons
ATG_position = some_sequence_upper.find("ATG")
print("ATG start codon begins in position (bp) " + str(ATG_position+1))

codon_2_pos = ATG_position + 3
codon_2 = some_sequence[codon_2_pos:codon_2_pos+3]
print("\tfollowed by " + codon_2 + " in position (bp) " + str(codon_2_pos+1))

codon_3_pos = codon_2_pos + 3
codon_3 =  some_sequence[codon_3_pos:codon_3_pos+3]
print("\tfollowed by " + codon_3 + " in position (bp) " + str(codon_3_pos+1))
 
print("\n----------------------------------------------------\n")

# get the upstream and genic sequences
upstream_seq, ATG, genic_seq =  some_sequence_upper.partition("ATG")

print("Upstream sequence is: " + upstream_seq)

print("\nUpstream length is: " + str(len(upstream_seq)))

print("\n----------------------------------------------------\n")

print("Gene sequence is: " + ATG + genic_seq)

print("\nGene sequence length is: " + str(len(ATG + genic_seq)))

print("\n----------------------------------------------------\n")

print("Gene + Strand: " + ATG + genic_seq + "\n")

# Compute the reverse complement sequence
reverse_seq = ATG + genic_seq
reverse_seq = reverse_seq[::-1]

# Now swap A's and T's, C's and G's
# hint #1: convert reverse_seq to lower case, then use
#          replace() method to complement nucleotides one at a time.
# hint #2: replace "a"s with "T"s, "t"s with "A"s, 
#          "c"s with "G"s, and "g"s with "C"s
reverse_seq = reverse_seq.lower()
reverse_seq = reverse_seq.replace("a", "T")
reverse_seq = reverse_seq.replace("t", "A")
reverse_seq = reverse_seq.replace("c", "G")
reverse_seq = reverse_seq.replace("g", "C")  

print("\nGene - Strand: " + reverse_seq.upper())

print("\n----------------------------------------------------\n")

# Print sequence with ATG highlighted
print("ATG highlighted: " + some_sequence.replace("atg", "ATG", 1))

# Compute AT-richness of upstream sequence
number_A = upstream_seq.count("A")
number_T = upstream_seq.count("T")

print("\nAT-richness:")
print("A: " + str(number_A))
print("T: " + str(number_T))

print("\n----------------------------------------------------\n")
